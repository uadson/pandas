import pandas as pd

from models import Analysis


data = Analysis()
file = data.get_data()
dataset = pd.read_csv(file, sep=',', header=0)

"""
1 - kc_house_data.csv

Select dataset: 1
"""

# output:
# Tipo de objeto
print(type(dataset))
# <class 'pandas.core.frame.DataFrame'>

# Amostra dos 5 primeiros itens
print(dataset.head())
"""
           id             date     price  bedrooms  bathrooms  ...  zipcode      lat     long  sqft_living15  sqft_lot15
0  7129300520  20141013T000000  221900.0       3.0       1.00  ...    98178  47.5112 -122.257           1340        5650
1  6414100192  20141209T000000  538000.0       3.0       2.25  ...    98125  47.7210 -122.319           1690        7639
2  5631500400  20150225T000000  180000.0       2.0       1.00  ...    98028  47.7379 -122.233           2720        8062
3  2487200875  20141209T000000  604000.0       4.0       3.00  ...    98136  47.5208 -122.393           1360        5000
4  1954400510  20150218T000000  510000.0       3.0       2.00  ...    98074  47.6168 -122.045           1800        7503

[5 rows x 21 columns]
"""

# Amostra dos dados tendo a data como indice da tabela
dataset = pd.read_csv(file, sep=',', index_col='date')
print(dataset)
"""
                         id     price  bedrooms  bathrooms  sqft_living  sqft_lot  floors  waterfront  view  condition  grade  sqft_above  sqft_basement  yr_built  yr_renovated  zipcode      lat     long  sqft_living15  sqft_lot15
date
20141013T000000  7129300520  221900.0       3.0       1.00         1180      5650     1.0           0     0          3      7        1180              0      1955             0    98178  47.5112 -122.257           1340        5650
20141209T000000  6414100192  538000.0       3.0       2.25         2570      7242     2.0           0     0          3      7        2170            400      1951          1991    98125  47.7210 -122.319           1690        7639
20150225T000000  5631500400  180000.0       2.0       1.00          770     10000     1.0           0     0          3      6         770              0      1933             0    98028  47.7379 -122.233           2720        8062
20141209T000000  2487200875  604000.0       4.0       3.00         1960      5000     1.0           0     0          5      7        1050            910      1965             0    98136  47.5208 -122.393           1360        5000
20150218T000000  1954400510  510000.0       3.0       2.00         1680      8080     1.0           0     0          3      8        1680              0      1987             0    98074  47.6168 -122.045           1800        7503
...                     ...       ...       ...        ...          ...       ...     ...         ...   ...        ...    ...         ...            ...       ...           ...      ...      ...      ...            ...         ...
20140521T000000   263000018  360000.0       3.0       2.50         1530      1131     3.0           0     0          3      8        1530              0      2009             0    98103  47.6993 -122.346           1530        1509
20150223T000000  6600060120  400000.0       4.0       2.50         2310      5813     2.0           0     0          3      8        2310              0      2014             0    98146  47.5107 -122.362           1830        7200
20140623T000000  1523300141  402101.0       2.0       0.75         1020      1350     2.0           0     0          3      7        1020              0      2009             0    98144  47.5944 -122.299           1020        2007
20150116T000000   291310100  400000.0       3.0       2.50         1600      2388     2.0           0     0          3      8        1600              0      2004             0    98027  47.5345 -122.069           1410        1287
20141015T000000  1523300157  325000.0       2.0       0.75         1020      1076     2.0           0     0          3      7        1020              0      2008             0    98144  47.5941 -122.299           1020        1357

[21613 rows x 20 columns]
"""

# Amostra dos dados com base nos filtros estabelecidos para colunas
dataset = pd.read_csv(file, sep=',', usecols=['id', 'date', 'price', 'bedrooms'])
print(dataset.head())
"""
           id             date     price  bedrooms
0  7129300520  20141013T000000  221900.0       3.0
1  6414100192  20141209T000000  538000.0       3.0
2  5631500400  20150225T000000  180000.0       2.0
3  2487200875  20141209T000000  604000.0       4.0
4  1954400510  20150218T000000  510000.0       3.0
"""

# Nome das colunas
print(dataset.columns)
# Index(['id', 'date', 'price', 'bedrooms'], dtype='object')

# Contagem dos itens por coluna
print(dataset.count())
"""
id          21613
date        21613
price       21613
bedrooms    21609
dtype: int64
"""

# Descrição dos dados da tabela
print(dataset.describe())
"""
                 id         price      bedrooms
count  2.161300e+04  2.161300e+04  21609.000000
mean   4.580302e+09  5.400881e+05      3.370910
std    2.876566e+09  3.671272e+05      0.930084
min    1.000102e+06  7.500000e+04      0.000000
25%    2.123049e+09  3.219500e+05      3.000000
50%    3.904930e+09  4.500000e+05      3.000000
75%    7.308900e+09  6.450000e+05      4.000000
max    9.900000e+09  7.700000e+06     33.000000
"""

# Amostra dos 5 últimos dados
print(dataset.tail())
"""

               id             date     price  bedrooms
21608   263000018  20140521T000000  360000.0       3.0
21609  6600060120  20150223T000000  400000.0       4.0
21610  1523300141  20140623T000000  402101.0       2.0
21611   291310100  20150116T000000  400000.0       3.0
21612  1523300157  20141015T000000  325000.0       2.0
"""

# Amostra de 5 dados aleatoriamente
print(dataset.sample(5))
"""
id             date     price  bedrooms
12830  3751600146  20141023T000000  166000.0       1.0
9884   7183000060  20150325T000000  260000.0       4.0
15155  3754700420  20150401T000000  375000.0       3.0
6046   1207200010  20150318T000000  245000.0       4.0
12562  1562000120  20140512T000000  660000.0       4.0
"""

# Quantidade de linhas, quantidade de colunas
print(dataset.shape)
# (21613, 4)

# Informações gerais sobre o dataset
print(dataset.info())
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 21613 entries, 0 to 21612
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype
---  ------    --------------  -----
 0   id        21613 non-null  int64
 1   date      21613 non-null  object
 2   price     21613 non-null  float64
 3   bedrooms  21609 non-null  float64
dtypes: float64(2), int64(1), object(1)
memory usage: 675.5+ KB
None
"""