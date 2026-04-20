# -*- coding: utf-8 -*-
"""time_series.ipynb

"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
# %matplotlib inline

from matplotlib import pyplot
series = pd.read_csv('airlinepassenger.csv', header=0, index_col=0)
series.plot()
pyplot.show()

from statsmodels.tsa.seasonal import seasonal_decompose
result = seasonal_decompose(series, model='multiplicative', period=1)
result.plot()
pyplot.show()



import pandas as pd
import numpy as np

product = {'month': [1,2,3,4,5,6,7,8,9,10,11,12], 'demand': [250,235,200,260,279,300,310,305,350,316,350,290]}

df = pd.DataFrame(product)

df.head()

df['pandas_SMA_3'] = df.iloc[:,1].rolling(window=3).mean()

df.head()

df['pandas_SMA_4'] = df.iloc[:,1].rolling(window=4).mean()

df.head()

import matplotlib.pyplot as plt
plt.figure(figsize=(15,10))
plt.grid(True)
plt.plot(df['demand'], label='demand')
plt.plot(df['pandas_SMA_3'], label='SMA 3 Months')
plt.plot(df['pandas_SMA_4'], label='SMA 4 Months')
plt.legend(loc=2)
plt.show()
