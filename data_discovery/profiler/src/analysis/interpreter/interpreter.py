from analysis.utils import init_spark, get_columns
from data.raw_data import RawData
from data.tables.csv_table import ITable
from pyspark.rdd import RDD
from pyspark.sql import DataFrame
from pyspark.sql import functions as f
from utils import generate_id
import re


class Interpreter:

    def __init__(self, table: ITable):
        self.spark = init_spark()
        self.table = table
        if table.get_type() == 'csv':
            self.tableDF = self.spark.read.option("maxColumns", 100000).csv(table.get_table_path(), inferSchema=True,

                                                                            header=True, multiLine=True)
        # TODO: investigate why .parquet empty columns create problem (works with .csv fine!)
        elif table.get_type() == 'parquet':
            self.tableDF = self.spark.read.option("maxColumns", 100000).parquet(table.get_table_path(),
                                                                                inferSchema=True, header=True,
                                                                                multiLine=True)
        regex = re.compile(r'^_c[0-9]*$')
        cols = list(filter(lambda x: not regex.match(x), self.tableDF.columns))
        self.tableDF = self.tableDF.select(*['`' + c + '`' for c in cols])
        # self.columns_rdd = get_columns_in_rdd(self.tableDF)
        for pair in self.tableDF.dtypes:
            if pair[1] == 'timestamp':
                self.tableDF = self.tableDF.withColumn(pair[0], f.from_unixtime(f.unix_timestamp(pair[0]),
                                                                                "yyyy-MM-dd HH:mm:ss"))
        self.columns_types = self.tableDF.dtypes

    def get_columns(self) -> RDD:
        return self.columns

    def get_columns_types(self) -> list:
        return self.columns_types

    def get_tableDF(self) -> DataFrame:
        return self.tableDF

    def get_numerical_column_names(self) -> list:
        dtypes = ['int', 'float', 'double', 'bigint', 'smallint', 'tinyint']
        numerical_colname_types = filter(lambda x: x[1] in dtypes, self.columns_types)
        return list(map(lambda x: '`' + x[0] + '`', numerical_colname_types))

    def get_textual_column_names(self) -> list:
        textual_colname_types = filter(lambda x: x[1] == 'string', self.columns_types)
        return list(map(lambda x: '`' + x[0] + '`', list(textual_colname_types)))

    def get_numerical_columns(self) -> DataFrame:
        numerical_column_names = self.get_numerical_column_names()
        return self.tableDF.select(numerical_column_names)

    def get_textual_columns(self) -> DataFrame:
        textual_column_names = self.get_textual_column_names()
        return self.tableDF.select(textual_column_names)

    def get_raw_data(self):
        self.columns = get_columns(self.tableDF)
        dataset_name = self.table.get_dataset_name()
        table_name = self.table.get_table_name()
        path = self.table.get_table_path()
        origin = self.table.get_origin()
        for column_name, data in self.columns:
            rid = generate_id(dataset_name, table_name, column_name)
            raw_data = RawData(rid, origin, dataset_name, path, table_name, column_name, data)
            yield raw_data