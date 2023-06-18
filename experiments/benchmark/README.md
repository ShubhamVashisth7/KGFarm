# Benchmark Datasets
KGFarm is evaluated against state-of-the-art on the 130 datasets shown bellow:

|Dataset ID|Dataset                               |ML task    |Size (in MB)|# Rows |# Columns|# Categorical features|# Numerical features|# Columns with missing values|Target                            |Source|Papers          |
|----------|--------------------------------------|-----------|------------|-------|---------|----------------------|--------------------|-----------------------------|----------------------------------|------|----------------|
|1         |jm1                                   |binary     |1.754       |10885  |22       |5                     |17                  |5                            |defects                           |OpenML|VolcanoML       |
|2         |hepatitis                             |binary     |0.008       |155    |20       |0                     |20                  |0                            |Class                             |UCI   |LFE             |
|3         |cleveland_heart_disease               |binary     |0.012       |303    |15       |0                     |15                  |2                            |condition                         |UCI   |                |
|4         |albert                                |binary     |256.302     |425240 |79       |25                    |54                  |45                           |class                             |AutoML|FLAML           |
|5         |adult                                 |binary     |5.59        |48842  |15       |9                     |6                   |2                            |class                             |AutoML|FLAML, AL       |
|6         |higgs                                 |binary     |21.694      |98050  |29       |9                     |20                  |9                            |class                             |AutoML|FLAML, VolcanoML|
|7         |titanic                               |binary     |0.082       |891    |12       |5                     |7                   |4                            |Survived                          |Kaggle|AL              |
|8         |APSFailure                            |binary     |99.152      |76000  |171      |170                   |1                   |169                          |class                             |AutoML|FLAML           |
|9         |credit-g                              |binary     |0.16        |1000   |21       |14                    |7                   |3                            |class                             |AutoML|FLAML           |
|10        |credit                                |binary     |0.031       |690    |16       |9                     |7                   |7                            |A16                               |UCI   |                |
|11        |horsecolic                            |binary     |0.019       |300    |28       |0                     |28                  |21                           |surgery                           |UCI   |                |
|12        |housevotes84                          |binary     |0.017       |435    |17       |17                    |0                   |16                           |Class                             |UCI   |                |
|13        |breastcancerwisconsin                 |binary     |0.02        |699    |11       |0                     |11                  |1                            |diagnosis                         |UCI   |LFE             |
|14        |Pima-indians-subset                   |binary     |0.023       |768    |9        |0                     |9                   |0                            |Outcome                           |UCI   |LFE             |
|15        |Diabetes                              |binary     |0.023       |768    |9        |0                     |9                   |0                            |Outcome                           |UCI   |LFE, AutoLearn  |
|16        |Madelon                               |binary     |4.969       |2600   |501      |0                     |501                 |0                            |Class                             |UCI   |LFE             |
|17        |Spectf-heart                          |binary     |0.01        |80     |45       |0                     |45                  |0                            |OVERALL_DIAGNOSIS                 |UCI   |LFE             |
|18        |Sonar                                 |binary     |0.082       |208    |61       |0                     |61                  |0                            |Class                             |UCI   |LFE, AutoLearn  |
|19        |AP-omentum-ovary                      |binary     |19.148      |275    |10936    |0                     |10936               |0                            |Tissue                            |UCI   |LFE             |
|20        |Credit-a                              |binary     |0.044       |690    |6        |0                     |6                   |0                            |Class                             |UCI   |LFE             |
|21        |AP-omentum-lung                       |binary     |14.171      |203    |10936    |0                     |10936               |0                            |Tissue                            |UCI   |LFE             |
|22        |Hepatitis                             |binary     |0.008       |155    |20       |0                     |20                  |0                            |Class                             |UCI   |LFE             |
|23        |Labor                                 |binary     |0.003       |60     |18       |0                     |18                  |0                            |class'                            |UCI   |LFE             |
|24        |Spambase                              |binary     |0.671       |4601   |58       |0                     |58                  |0                            |Class                             |UCI   |LFE             |
|25        |Ionosphere                            |binary     |0.078       |351    |35       |0                     |35                  |0                            |column_ai                         |UCI   |LFE, AutoLearn  |
|26        |Gisette                               |binary     |121.912     |13500  |5000     |0                     |5000                |0                            |labels                            |UCI   |LFE             |
|27        |ozone-level-8hr                       |binary     |1.411       |2534   |73       |0                     |73                  |0                            |Class                             |OpenML|VolcanoML       |
|28        |eeg-eye-state                         |binary     |1.714       |14980  |15       |0                     |15                  |0                            |Class                             |OpenML|VolcanoML       |
|29        |guillermo                             |binary     |655.67      |20000  |4297     |0                     |4297                |0                            |class                             |AutoML|FLAML           |
|30        |kc1                                   |binary     |0.34        |2109   |22       |0                     |22                  |0                            |defects                           |AutoML|FLAML, VolcanoML|
|31        |blood-transfusion-service-center      |binary     |0.029       |748    |5        |0                     |5                   |0                            |Class                             |AutoML|FLAML           |
|32        |mc1                                   |binary     |2.754       |9466   |39       |0                     |39                  |0                            |c                                 |OpenML|VolcanoML       |
|33        |pc4                                   |binary     |0.413       |1458   |38       |0                     |38                  |0                            |c                                 |OpenML|AL, VolcanoML   |
|34        |pollen_871                            |binary     |0.176       |3848   |6        |1                     |5                   |0                            |binaryClass                       |OpenML|VolcanoML       |
|35        |numerai28.6                           |binary     |16.167      |96320  |22       |0                     |22                  |0                            |attribute_21                      |AutoML|FLAML           |
|36        |delta_ailerons                        |binary     |0.326       |7129   |6        |1                     |5                   |0                            |binaryClass                       |OpenML|VolcanoML       |
|37        |Hill_Valley_with_noise                |binary     |0.934       |1212   |101      |0                     |101                 |0                            |target                            |PMLB  |AL              |
|38        |airlines                              |binary     |32.921      |539383 |8        |3                     |5                   |2                            |Delay                             |AutoML|FLAML           |
|39        |Hill_Valley_without_noise             |binary     |0.934       |1212   |101      |0                     |101                 |0                            |target                            |PMLB  |AL              |
|40        |quake                                 |binary     |0.067       |2178   |4        |1                     |3                   |0                            |binaryClass                       |OpenML|AL, VolcanoML   |
|41        |mammography                           |binary     |0.597       |11183  |7        |1                     |6                   |0                            |class                             |OpenML|VolcanoML       |
|42        |puma32H_752                           |binary     |2.063       |8192   |33       |1                     |32                  |0                            |binaryClass                       |OpenML|VolcanoML       |
|43        |christine                             |binary     |67.667      |5418   |1637     |0                     |1637                |0                            |class                             |AutoML|FLAML           |
|44        |ailerons                              |binary     |4.301       |13750  |41       |1                     |40                  |0                            |binaryClass                       |OpenML|VolcanoML       |
|45        |sylvine                               |binary     |0.821       |5124   |21       |0                     |21                  |0                            |class                             |AutoML|FLAML           |
|46        |space_ga_737                          |binary     |0.166       |3107   |7        |1                     |6                   |0                            |binaryClass                       |OpenML|VolcanoML       |
|47        |MiniBooNE                             |binary     |49.74       |130064 |51       |0                     |51                  |0                            |signal                            |AutoML|FLAML           |
|48        |kin8nm_807                            |binary     |0.563       |8192   |9        |1                     |8                   |0                            |binaryClass                       |OpenML|VolcanoML       |
|49        |puma8NH_816                           |binary     |0.563       |8192   |9        |1                     |8                   |0                            |binaryClass                       |OpenML|VolcanoML       |
|50        |phoneme                               |binary     |0.247       |5404   |6        |0                     |6                   |0                            |Class                             |AutoML|FLAML, VolcanoML|
|51        |waveform-5000                         |binary     |1.564       |5000   |41       |1                     |40                  |0                            |binaryClass                       |OpenML|VolcanoML       |
|52        |jasmine                               |binary     |3.301       |2984   |145      |0                     |145                 |0                            |class                             |AutoML|FLAML           |
|53        |Australian                            |binary     |0.079       |690    |15       |0                     |15                  |0                            |A15                               |AutoML|FLAML           |
|54        |electricity                           |binary     |3.111       |45312  |9        |1                     |8                   |0                            |class                             |OpenML|VolcanoML       |
|55        |delta_elevators                       |binary     |0.508       |9517   |7        |1                     |6                   |0                            |binaryClass                       |OpenML|VolcanoML       |
|56        |bank32nh_833                          |binary     |2.063       |8192   |33       |1                     |32                  |0                            |binaryClass                       |OpenML|VolcanoML       |
|57        |cpu_small_735                         |binary     |0.813       |8192   |13       |1                     |12                  |0                            |binaryClass                       |OpenML|VolcanoML       |
|58        |wind_847                              |binary     |0.752       |6574   |15       |1                     |14                  |0                            |binaryClass                       |OpenML|VolcanoML       |
|59        |fri_c1_1000_25                        |binary     |0.198       |1000   |26       |1                     |25                  |0                            |binaryClass                       |OpenML|AL              |
|60        |cpu_act_761                           |binary     |1.375       |8192   |22       |1                     |21                  |0                            |binaryClass                       |OpenML|VolcanoML       |
|61        |breast_cancer_wisconsin               |binary     |0.135       |569    |31       |0                     |31                  |0                            |target                            |PMLB  |AL              |
|62        |spambase                              |binary     |2.036       |4601   |58       |0                     |58                  |0                            |target                            |PMLB  |AL, VolcanoML   |
|63        |ionosphere                            |binary     |0.094       |351    |35       |0                     |35                  |0                            |target                            |PMLB  |AL              |
|64        |nomao                                 |binary     |31.291      |34465  |119      |0                     |119                 |0                            |Class                             |AutoML|FLAML           |
|65        |kr-vs-kp                              |binary     |0.902       |3196   |37       |37                    |0                   |0                            |class                             |AutoML|FLAML           |
|66        |Amazon_employee_access                |binary     |2.5         |32769  |10       |0                     |10                  |0                            |target                            |AutoML|FLAML           |
|67        |OVA_Breast                            |binary     |128.919     |1545   |10937    |1                     |10936               |0                            |Tissue                            |OpenML|AL              |
|68        |analcatdata_supreme                   |binary     |0.247       |4052   |8        |1                     |7                   |0                            |binaryClass                       |OpenML|VolcanoML       |
|69        |page-blocks                           |binary     |0.459       |5473   |11       |1                     |10                  |0                            |binaryClass                       |OpenML|VolcanoML       |
|70        |riccardo                              |binary     |655.67      |20000  |4297     |0                     |4297                |0                            |class                             |AutoML|FLAML           |
|71        |MagicTelescope                        |binary     |1.741       |19020  |12       |1                     |11                  |0                            |class:                            |OpenML|AL              |
|72        |abalone                               |multi-class|0.287       |4177   |9        |1                     |8                   |0                            |Class_number_of_rings             |OpenML|VolcanoML       |
|73        |fabert                                |multi-class|50.338      |8237   |801      |0                     |801                 |0                            |class                             |AutoML|FLAML           |
|74        |robert                                |multi-class|549.393     |10000  |7201     |0                     |7201                |0                            |class                             |AutoML|FLAML           |
|75        |helena                                |multi-class|13.927      |65196  |28       |0                     |28                  |0                            |class                             |AutoML|FLAML           |
|76        |kropt                                 |multi-class|1.498       |28056  |7        |4                     |3                   |0                            |game                              |OpenML|AL, VolcanoML   |
|77        |volkert                               |multi-class|80.522      |58310  |181      |0                     |181                 |0                            |class                             |AutoML|FLAML           |
|78        |dilbert                               |multi-class|152.664     |10000  |2001     |0                     |2001                |0                            |class                             |AutoML|FLAML           |
|79        |Fashion-MNIST                         |multi-class|419.235     |70000  |785      |0                     |785                 |0                            |class                             |AutoML|FLAML           |
|80        |wine_quality_white                    |multi-class|0.449       |4898   |12       |0                     |12                  |0                            |target                            |PMLB  |AL              |
|81        |wine_quality_red                      |multi-class|0.147       |1599   |12       |0                     |12                  |0                            |target                            |PMLB  |AL              |
|82        |jannis                                |multi-class|35.136      |83733  |55       |0                     |55                  |0                            |class                             |AutoML|FLAML           |
|83        |vehicle                               |multi-class|0.123       |846    |19       |1                     |18                  |0                            |Class                             |AutoML|FLAML           |
|84        |connect-4                             |multi-class|22.163      |67557  |43       |0                     |43                  |0                            |class                             |AutoML|FLAML           |
|85        |cnae-9                                |multi-class|7.062       |1080   |857      |0                     |857                 |0                            |Class                             |AutoML|FLAML           |
|86        |glass                                 |multi-class|0.016       |205    |10       |0                     |10                  |0                            |target                            |PMLB  |AL              |
|87        |mnist_784                             |multi-class|419.235     |70000  |785      |0                     |785                 |0                            |class                             |OpenML|AL, VolcanoML   |
|88        |jungle_chess_2pcs_raw_endgame_complete|multi-class|2.394       |44819  |7        |1                     |6                   |0                            |class                             |AutoML|FLAML           |
|89        |satimage                              |multi-class|1.815       |6430   |37       |0                     |37                  |0                            |class                             |OpenML|VolcanoML       |
|90        |shuttle                               |multi-class|4.425       |58000  |10       |0                     |10                  |0                            |class                             |AutoML|FLAML           |
|91        |dionis                                |multi-class|193.691     |416188 |61       |0                     |61                  |0                            |class                             |AutoML|FLAML           |
|92        |covertype                             |multi-class|243.802     |581012 |55       |0                     |55                  |0                            |class                             |AutoML|FLAML, AL       |
|93        |splice                                |multi-class|1.509       |3190   |62       |62                    |0                   |1                            |Class                             |OpenML|AL              |
|94        |segment                               |multi-class|0.353       |2310   |20       |1                     |19                  |0                            |class                             |AutoML|FLAML, VolcanoML|
|95        |car_evaluation                        |multi-class|0.29        |1728   |22       |0                     |22                  |0                            |target                            |PMLB  |AL              |
|96        |mfeat-factors                         |multi-class|3.311       |2000   |217      |0                     |217                 |0                            |class                             |AutoML|FLAML           |
|97        |optdigits                             |multi-class|2.787       |5620   |65       |0                     |65                  |0                            |class                             |OpenML|VolcanoML       |
|98        |pendigits                             |multi-class|1.426       |10992  |17       |0                     |17                  |0                            |class                             |OpenML|VolcanoML       |
|99        |debutanizer                           |regression |0.146       |2394   |8        |0                     |8                   |0                            |y                                 |OpenML|VolcanoML       |
|100       |witmer_census_1980                    |regression |0.002       |50     |6        |1                     |5                   |1                            |HSPerc                            |OpenML|VolcanoML       |
|101       |bng_breastTumor                       |regression |8.899       |116640 |10       |0                     |10                  |0                            |target                            |PMLB  |FLAML           |
|102       |puma32H_308                           |regression |2.063       |8192   |33       |0                     |33                  |0                            |thetadd6                          |OpenML|VolcanoML       |
|103       |kin8nm_189                            |regression |0.563       |8192   |9        |0                     |9                   |0                            |y                                 |OpenML|VolcanoML       |
|104       |poker                                 |regression |86.022      |1025010|11       |0                     |11                  |0                            |target                            |PMLB  |FLAML           |
|105       |pollen_529                            |regression |0.176       |3848   |6        |0                     |6                   |0                            |DENSITY                           |OpenML|VolcanoML       |
|106       |bng_lowbwt                            |regression |2.373       |31104  |10       |0                     |10                  |0                            |target                            |PMLB  |FLAML           |
|107       |bank32nh_558                          |regression |2.063       |8192   |33       |0                     |33                  |0                            |rej                               |OpenML|VolcanoML       |
|108       |space_ga_507                          |regression |0.166       |3107   |7        |0                     |7                   |0                            |ln(VOTES/POP)                     |OpenML|VolcanoML       |
|109       |bng_echomonths                        |regression |1.335       |17496  |10       |0                     |10                  |0                            |target                            |PMLB  |FLAML           |
|110       |house_16H                             |regression |2.955       |22784  |17       |0                     |17                  |0                            |target                            |PMLB  |FLAML           |
|111       |mercedes-benz-greener-manufacturing   |regression |12.139      |4209   |378      |8                     |370                 |0                            |y                                 |Kaggle|AL              |
|112       |bng_pbc                               |regression |144.959     |1000000|19       |0                     |19                  |0                            |target                            |PMLB  |FLAML           |
|113       |bng_pwLinear                          |regression |14.867      |177147 |11       |0                     |11                  |0                            |target                            |PMLB  |FLAML           |
|114       |puma8NH_225                           |regression |0.563       |8192   |9        |0                     |9                   |0                            |thetadd3                          |OpenML|VolcanoML       |
|115       |house_8L                              |regression |1.565       |22784  |9        |0                     |9                   |0                            |target                            |PMLB  |FLAML           |
|116       |rainfall_bangladesh                   |regression |0.511       |16755  |4        |2                     |2                   |1                            |Rainfall                          |OpenML|VolcanoML       |
|117       |houses                                |regression |1.417       |20640  |9        |0                     |9                   |0                            |target                            |PMLB  |FLAML           |
|118       |wind_503                              |regression |0.752       |6574   |15       |0                     |15                  |0                            |MAL                               |OpenML|VolcanoML       |
|119       |socmob                                |regression |0.053       |1156   |6        |4                     |2                   |2                            |counts_for_sons_current_occupation|OpenML|VolcanoML       |
|120       |bng_pharynx                           |regression |83.923      |1000000|11       |0                     |11                  |0                            |target                            |PMLB  |FLAML           |
|121       |sulfur                                |regression |0.539       |10081  |7        |0                     |7                   |0                            |y1                                |OpenML|VolcanoML       |
|122       |fried                                 |regression |3.422       |40768  |11       |0                     |11                  |0                            |target                            |PMLB  |FLAML           |
|123       |bank8FM                               |regression |0.563       |8192   |9        |0                     |9                   |0                            |rej                               |OpenML|VolcanoML       |
|124       |2dplanes                              |regression |3.422       |40768  |11       |0                     |11                  |0                            |target                            |PMLB  |FLAML           |
|125       |weather_izmir                         |regression |0.112       |1461   |10       |0                     |10                  |0                            |Mean_temperature                  |OpenML|VolcanoML       |
|126       |stock                                 |regression |0.073       |950    |10       |0                     |10                  |0                            |company10                         |OpenML|VolcanoML       |
|127       |cpu_small_227                         |regression |0.813       |8192   |13       |0                     |13                  |0                            |usr                               |OpenML|VolcanoML       |
|128       |cpu_act_573                           |regression |1.375       |8192   |22       |0                     |22                  |0                            |usr                               |OpenML|VolcanoML       |
|129       |pol                                   |regression |5.608       |15000  |49       |0                     |49                  |0                            |target                            |PMLB  |FLAML           |
|130       |mv                                    |regression |3.733       |40768  |12       |0                     |12                  |0                            |target                            |PMLB  |FLAML           |