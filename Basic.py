from __future__ import division

#!/usr/bin/env python

"""This file contains the code for the Data Mining Class. It uses the Airline dataset <<add link>>"""

__author__ = ""
__copyright__ = ""
__credits__ = []
__license__ = ""
__version__ = ""
__maintainer__ = ""
__email__ = ""
__status__ = ""

# <codecell>

#  Importing various modules

# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from pylab import figure, show
from pandas import DataFrame, Series
import pandas as pd
import csv
import os
import statsmodels.formula.api as smf
import scipy.stats as stats
import statsmodels.api as sm

# <codecell>

#  Setting global constants. Please initialize this before running the code

TRAINING_LINE_NUMBER = 10 # Number of lines to be read from the huge file, set to total file length while running for entire file
INPUT_FILE_PATH="C:\\data\\airline\\" # Path of the folder where you have placed your files
SKIP_FIRST_LINE = True # To skip the first line, as its the header
YEARS = ['2008'] # Add more years in this list and add the files in the INPUT_FILE_PATH

# <codecell>

# Setting the dataframes for Airline, Plane and Carriers

try:
    path = "C:\\data\\airline\\plane-data.csv"
    dfPlane = pd.read_csv(path)
    path = 'C:\\data\\airline\\airports.csv'
    dfAirport = pd.read_csv(path)
    path = 'C:\\data\\airline\\carriers.csv'
    dfCarrier = pd.read_csv(path)
except Exception as e:
    print "Supplemental Data Import failed", e

# <codecell>

# Readng the main file in a Pandas dataframe

try:
    for year in YEARS:
        path = os.path.join(INPUT_FILE_PATH, '%d.csv' % int(year))
        dfMaster = pd.read_csv(path, nrows=TRAINING_LINE_NUMBER,skiprows=0)
except Exception as e:
    print "Supplemental Data Import failed", e
print dfMaster.head()

# <codecell>

dfMaster['ArrDelay'] = dfMaster['ArrDelay'].astype('int')
dfMaster['DepDelay'] = dfMaster['DepDelay'].astype('int')
print dfMaster.columns

# <codecell>

results = sm.OLS.from_formula('DepDelay ~ ArrDelay', dfMaster).fit()
print results.summary()

# <codecell>

intercept, slope = results.params
r2 = results.rsquared
print slope, intercept, r2

# <codecell>

plt.plot(dfMaster['ArrDelay'], dfMaster['DepDelay'], 'bo')
plt.hold(True)
x = np.array([0,200])
y = intercept + slope * x
plt.plot(x, y, 'r-')
plt.show()

# <codecell>

from statsmodels.stats.anova import anova_lm

print anova_lm(results)

