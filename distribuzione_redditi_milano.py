#fonte https://dati.comune.milano.it/dataset/ds531_distribuzione-del-reddito-complessivo-delle-persone-fisiche/resource/5d8f2401-5ec5-4efd-afb7-6ae543fd1029?inner_span=True
import pandas as pd
import json
import matplotlib.pyplot as plt

# Il tuo JSON
json_data = '''[
  {
    "Anno": 2020,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 456,
    "Ammontare in euro": -3219045
  },
  {
    "Anno": 2020,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 241948,
    "Ammontare in euro": 1095992447
  },
  {
    "Anno": 2020,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 102265,
    "Ammontare in euro": 1278052047
  },
  {
    "Anno": 2020,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 225439,
    "Ammontare in euro": 4605079255
  },
  {
    "Anno": 2020,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 267489,
    "Ammontare in euro": 9773307243
  },
  {
    "Anno": 2020,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 52028,
    "Ammontare in euro": 3321778565
  },
  {
    "Anno": 2020,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 45235,
    "Ammontare in euro": 4186470856
  },
  {
    "Anno": 2020,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 34665,
    "Ammontare in euro": 9816834893
  },
  {
    "Anno": 2019,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 316,
    "Ammontare in euro": -3846576
  },
  {
    "Anno": 2019,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 238111,
    "Ammontare in euro": 1087037744
  },
  {
    "Anno": 2019,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 101413,
    "Ammontare in euro": 1266215969
  },
  {
    "Anno": 2019,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 240092,
    "Ammontare in euro": 4910759985
  },
  {
    "Anno": 2019,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 276262,
    "Ammontare in euro": 10075891655
  },
  {
    "Anno": 2019,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 53238,
    "Ammontare in euro": 3398464192
  },
  {
    "Anno": 2019,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 45369,
    "Ammontare in euro": 4194927285
  },
  {
    "Anno": 2019,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 35423,
    "Ammontare in euro": 10307853897
  },
  {
    "Anno": 2018,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 412,
    "Ammontare in euro": -3348729
  },
  {
    "Anno": 2018,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 236486,
    "Ammontare in euro": 1112491928
  },
  {
    "Anno": 2018,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 104043,
    "Ammontare in euro": 1299342731
  },
  {
    "Anno": 2018,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 245212,
    "Ammontare in euro": 5014246181
  },
  {
    "Anno": 2018,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 275918,
    "Ammontare in euro": 10059066334
  },
  {
    "Anno": 2018,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 53001,
    "Ammontare in euro": 3381773939
  },
  {
    "Anno": 2018,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 44602,
    "Ammontare in euro": 4129561136
  },
  {
    "Anno": 2018,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 35234,
    "Ammontare in euro": 10162649434
  },
  {
    "Anno": 2017,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 5161,
    "Ammontare in euro": -147776538
  },
  {
    "Anno": 2017,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 237544,
    "Ammontare in euro": 1122607980
  },
  {
    "Anno": 2017,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 104034,
    "Ammontare in euro": 1299218938
  },
  {
    "Anno": 2017,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 246735,
    "Ammontare in euro": 5035845250
  },
  {
    "Anno": 2017,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 265512,
    "Ammontare in euro": 9652942821
  },
  {
    "Anno": 2017,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 50216,
    "Ammontare in euro": 3204244127
  },
  {
    "Anno": 2017,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 41845,
    "Ammontare in euro": 3866422921
  },
  {
    "Anno": 2017,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 32538,
    "Ammontare in euro": 9280409471
  },
  {
    "Anno": 2016,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 3308,
    "Ammontare in euro": -36338697
  },
  {
    "Anno": 2016,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 234867,
    "Ammontare in euro": 1116913552
  },
  {
    "Anno": 2016,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 104603,
    "Ammontare in euro": 1306727578
  },
  {
    "Anno": 2016,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 249131,
    "Ammontare in euro": 5082613094
  },
  {
    "Anno": 2016,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 260455,
    "Ammontare in euro": 9442351944
  },
  {
    "Anno": 2016,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 48935,
    "Ammontare in euro": 3122298134
  },
  {
    "Anno": 2016,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 40549,
    "Ammontare in euro": 3740201710
  },
  {
    "Anno": 2016,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 31088,
    "Ammontare in euro": 8750443743
  },
  {
    "Anno": 2015,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 3284,
    "Ammontare in euro": -35651521
  },
  {
    "Anno": 2015,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 239146,
    "Ammontare in euro": 1134421205
  },
  {
    "Anno": 2015,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 103708,
    "Ammontare in euro": 1296934603
  },
  {
    "Anno": 2015,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 248321,
    "Ammontare in euro": 5057285026
  },
  {
    "Anno": 2015,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 258944,
    "Ammontare in euro": 9393031835
  },
  {
    "Anno": 2015,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 47723,
    "Ammontare in euro": 3045682216
  },
  {
    "Anno": 2015,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 39927,
    "Ammontare in euro": 3687646265
  },
  {
    "Anno": 2015,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 30316,
    "Ammontare in euro": 8518112697
  },
  {
    "Anno": 2014,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 3979,
    "Ammontare in euro": -38797290
  },
  {
    "Anno": 2014,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 237201,
    "Ammontare in euro": 1120261085
  },
  {
    "Anno": 2014,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 102525,
    "Ammontare in euro": 1282749594
  },
  {
    "Anno": 2014,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 253601,
    "Ammontare in euro": 5162334584
  },
  {
    "Anno": 2014,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 250904,
    "Ammontare in euro": 9067391931
  },
  {
    "Anno": 2014,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 46205,
    "Ammontare in euro": 2948695112
  },
  {
    "Anno": 2014,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 38417,
    "Ammontare in euro": 3545615998
  },
  {
    "Anno": 2014,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 28780,
    "Ammontare in euro": 8142749247
  },
  {
    "Anno": 2013,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 4231,
    "Ammontare in euro": -40589252
  },
  {
    "Anno": 2013,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 231565,
    "Ammontare in euro": 1109441397
  },
  {
    "Anno": 2013,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 104271,
    "Ammontare in euro": 1305419307
  },
  {
    "Anno": 2013,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 257827,
    "Ammontare in euro": 5236175425
  },
  {
    "Anno": 2013,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 245903,
    "Ammontare in euro": 8861696738
  },
  {
    "Anno": 2013,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 44857,
    "Ammontare in euro": 2862493932
  },
  {
    "Anno": 2013,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 36817,
    "Ammontare in euro": 3403353134
  },
  {
    "Anno": 2013,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 27669,
    "Ammontare in euro": 7643107036
  },
  {
    "Anno": 2012,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 4211,
    "Ammontare in euro": -41187764
  },
  {
    "Anno": 2012,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 235896,
    "Ammontare in euro": 1150813145
  },
  {
    "Anno": 2012,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 109037,
    "Ammontare in euro": 1367289064
  },
  {
    "Anno": 2012,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 259959,
    "Ammontare in euro": 5263818217
  },
  {
    "Anno": 2012,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 239653,
    "Ammontare in euro": 8665114919
  },
  {
    "Anno": 2012,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 44346,
    "Ammontare in euro": 2830658359
  },
  {
    "Anno": 2012,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 36641,
    "Ammontare in euro": 3386773375
  },
  {
    "Anno": 2012,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 27328,
    "Ammontare in euro": 7599383167
  },
  {
    "Anno": 2011,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 3378,
    "Ammontare in euro": -35240653
  },
  {
    "Anno": 2011,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 244114,
    "Ammontare in euro": 1146058430
  },
  {
    "Anno": 2011,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 109381,
    "Ammontare in euro": 1373127334
  },
  {
    "Anno": 2011,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 259032,
    "Ammontare in euro": 5242581952
  },
  {
    "Anno": 2011,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 238959,
    "Ammontare in euro": 8608800663
  },
  {
    "Anno": 2011,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 44508,
    "Ammontare in euro": 2840034361
  },
  {
    "Anno": 2011,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 37235,
    "Ammontare in euro": 3445101975
  },
  {
    "Anno": 2011,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 28240,
    "Ammontare in euro": 7923965663
  },
  {
    "Anno": 2010,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 3612,
    "Ammontare in euro": -36278202
  },
  {
    "Anno": 2010,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 246097,
    "Ammontare in euro": 1163273499
  },
  {
    "Anno": 2010,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 112531,
    "Ammontare in euro": 1414689429
  },
  {
    "Anno": 2010,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 264861,
    "Ammontare in euro": 5348909629
  },
  {
    "Anno": 2010,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 233631,
    "Ammontare in euro": 8424140434
  },
  {
    "Anno": 2010,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 42883,
    "Ammontare in euro": 2735502947
  },
  {
    "Anno": 2010,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 35497,
    "Ammontare in euro": 3286743767
  },
  {
    "Anno": 2010,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 26938,
    "Ammontare in euro": 7465240953
  },
  {
    "Anno": 2009,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 3767,
    "Ammontare in euro": -40805702
  },
  {
    "Anno": 2009,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 243445,
    "Ammontare in euro": 1163249833
  },
  {
    "Anno": 2009,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 113778,
    "Ammontare in euro": 1432493095
  },
  {
    "Anno": 2009,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 269042,
    "Ammontare in euro": 5425863696
  },
  {
    "Anno": 2009,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 231319,
    "Ammontare in euro": 8318478480
  },
  {
    "Anno": 2009,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 41674,
    "Ammontare in euro": 2659430898
  },
  {
    "Anno": 2009,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 34636,
    "Ammontare in euro": 3213239107
  },
  {
    "Anno": 2009,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 25768,
    "Ammontare in euro": 7064058827
  },
  {
    "Anno": 2008,
    "Classi di reddito complessivo in euro": "minore o uguale a 0 ",
    "Frequenza persone fisiche": 3496,
    "Ammontare in euro": -35378866
  },
  {
    "Anno": 2008,
    "Classi di reddito complessivo in euro": "da 0 a 10.000",
    "Frequenza persone fisiche": 246479,
    "Ammontare in euro": 1199414590
  },
  {
    "Anno": 2008,
    "Classi di reddito complessivo in euro": "da 10.000 a 15.000",
    "Frequenza persone fisiche": 120895,
    "Ammontare in euro": 1524301878
  },
  {
    "Anno": 2008,
    "Classi di reddito complessivo in euro": "da 15.000 a 26.000",
    "Frequenza persone fisiche": 273948,
    "Ammontare in euro": 5508714727
  },
  {
    "Anno": 2008,
    "Classi di reddito complessivo in euro": "da 26.000 a 55.000",
    "Frequenza persone fisiche": 227021,
    "Ammontare in euro": 8180792956
  },
  {
    "Anno": 2008,
    "Classi di reddito complessivo in euro": "da 55.000 a 75.000",
    "Frequenza persone fisiche": 41460,
    "Ammontare in euro": 2646926945
  },
  {
    "Anno": 2008,
    "Classi di reddito complessivo in euro": "da 75.000 a 120.000",
    "Frequenza persone fisiche": 34044,
    "Ammontare in euro": 3159763370
  },
  {
    "Anno": 2008,
    "Classi di reddito complessivo in euro": "oltre 120.000",
    "Frequenza persone fisiche": 26730,
    "Ammontare in euro": 7576923127
  }
]
'''

# Carica il JSON in una lista di dizionari
data = json.loads(json_data)

# Crea un DataFrame da una lista di dizionari
df = pd.DataFrame(data)

# Ora `df` è il tuo DataFrame che puoi utilizzare in pandas
df
