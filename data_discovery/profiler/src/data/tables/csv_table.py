import os
from data.tables.i_table import ITable


class CSVTable(ITable):

    def __init__(self, table_name: str, dataset_name: str, dataset_path: str, origin: str):
        self.table_name = table_name
        self.dataset_name = dataset_name
        self.table_path = os.path.abspath(dataset_path) + '/' + table_name
        self.origin = origin

    def get_table_path(self):
        return self.table_path

    def get_dataset_name(self):
        return self.dataset_name

    def get_table_name(self):
        return self.table_name

    def get_origin(self):
        return self.origin

    def get_type(self):
        return self.type

