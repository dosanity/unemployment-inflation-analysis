import pandas_datareader as wb
import pandas as pd
from datetime import datetime
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import math
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as stats
from sklearn.linear_model import LogisticRegression

fromDate = "01/01/1948"
toDate = "12/31/2022"

Inflation = wb.DataReader('CPIAUCSL', 'fred', fromDate, toDate)
UnRate = wb.DataReader('UNRATE', 'fred', fromDate, toDate)

Inflation = Inflation.dropna()
UnRate = UnRate.dropna()

dataframe = Inflation.join(UnRate, how="inner")

dataframe = dataframe.dropna()

print(dataframe.head())

Y = dataframe['CPIAUCSL'].values
X = dataframe['UNRATE'].values

inputsTrain, inputsTest, resultTrain, resultTest = train_test_split(X, Y, test_size = 0.3, random_state = 1)

linRegr = linear_model.LinearRegression()
linRegr.fit(inputsTrain.reshape(-1, 1), resultTrain)
predict = linRegr.predict(inputsTest.reshape(-1, 1))

r2 = r2_score(resultTest, predict)

print("Our calculated coeffs m:{} and b:{} and our r2 is {}".format(linRegr.coef_,linRegr.intercept_,r2))

uni_mod = smf.ols(formula="CPIAUCSL ~ UNRATE", data = dataframe)
uni_result = uni_mod.fit()
print(uni_result.summary())
