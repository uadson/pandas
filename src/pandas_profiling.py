import pandas as pd

import pandas_profiling

from models import Analysis


data = Analysis()
file = data.get_data()
dataset = pd.read_csv(file, sep=',', header=0)


profile = pandas_profiling.ProfileReport(dataset)


