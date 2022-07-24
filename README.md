# Extent of Unemployment on Inflation

Our current economic climate is unique with the rise of the coronavirus. In the economy, we are seeing unique factors such as a high inflation rate paired with a low uneomployment rate. Historically, stagflation or recession-inflation occurs which is a situation where the inflation rate is high and unemployment remains high as well. We are particularly interested to see how these changes in the unemployment rate are potentially impacting the increase in inflation rate.

## Data

Our data is from the Federal Reserve Bank of St. Louis. The Federal Bank is central to the nation's economy and provides economic resources and data for US economic statistical analysis. 

For our X variable, we chose to look at the monthly unemployment rate (`UNRATE`). The unemployment rate represents the number of unemployed as a percentage of the labor force. Labor force data are restricted to people 16 years of age and older, who currently reside in 1 of the 50 states or the District of Columbia, who do not reside in institutions (e.g., penal and mental facilities, homes for the aged), and who are not on active duty in the Armed Forces. 

![fredgraph](https://user-images.githubusercontent.com/29410712/180629012-d348804f-6ace-4876-9450-54ed2b60e127.png)

For our Y variable, we chose to look at the Consumer Price Index. The Consumer Price Index for All Urban Consumers: All Items (`CPIAUCSL`) is a price index of a basket of goods and services paid by urban consumers. Percent changes in the price index measure the inflation rate between any two time periods. The most common inflation metric is the percent change from one year ago. It can also represent the buying habits of urban consumers. This particular index includes roughly 88 percent of the total population, accounting for wage earners, clerical workers, technical workers, self-employed, short-term workers, unemployed, retirees, and those not in the labor force.

The CPIs are based on prices for food, clothing, shelter, and fuels; transportation fares; service fees (e.g., water and sewer service); and sales taxes. Prices are collected monthly from about 4,000 housing units and approximately 26,000 retail establishments across 87 urban areas. To calculate the index, price changes are averaged with weights representing their importance in the spending of the particular group. The index measures price changes (as a percent change) from a predetermined reference date. In addition to the original unadjusted index distributed, the Bureau of Labor Statistics also releases a seasonally adjusted index. The unadjusted series reflects all factors that may influence a change in prices. However, it can be very useful to look at the seasonally adjusted CPI, which removes the effects of seasonal changes, such as weather, school year, production cycles, and holidays.

![fredgraph (1)](https://user-images.githubusercontent.com/29410712/180629045-84721112-77dc-443d-ac4e-2360b9ed0a48.png)

## Process

Given the large time frame of data, we parsed the unemployment and inflation into four time periods of relatively equal lengths. 

| Time Periods | Years            |
| ------------ | ---------------- |
| Period 1     | 1948 - 1966      |
| Period 2     | 1967 - 1984      |
| Period 3     | 1985 - 2002      |
| Period 4     | 2003 - 2022      |
| Overall      | 1948 - 2022      |

### Code

In creating the code, we had to go through a few steps:

1. Download the data from FRED database and import the relevant statistical modules.

```
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
```

2. Define the variables and appropriate timeframes.

```
fromDate = "01/01/1948"
toDate = "07/23/2022"

Inflation = wb.DataReader('CPIAUCSL', 'fred', fromDate, toDate)
UnRate = wb.DataReader('UNRATE', 'fred', fromDate, toDate)
```

3. Clean the data and combine it.

```
Inflation = Inflation.dropna()
UnRate = UnRate.dropna()

dataframe = Inflation.join(UnRate, how="inner")

dataframe = dataframe.dropna()

print(dataframe.head())
```

4. Run an Ordinary Least Squares regression to determine the statistical significance and trends.

```
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
```

## Results

#### Period 1 (1948 - 1966) regression results.
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               CPIAUCSL   R-squared:                       0.040
Model:                            OLS   Adj. R-squared:                  0.036
Method:                 Least Squares   F-statistic:                     9.388
Date:                Sat, 23 Jul 2022   Prob (F-statistic):            0.00245
Time:                        20:28:20   Log-Likelihood:                -531.19
No. Observations:                 228   AIC:                             1066.
Df Residuals:                     226   BIC:                             1073.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     26.0712      0.678     38.452      0.000      24.735      27.407
UNRATE         0.4169      0.136      3.064      0.002       0.149       0.685
==============================================================================
Omnibus:                        1.903   Durbin-Watson:                   0.004
Prob(Omnibus):                  0.386   Jarque-Bera (JB):                1.892
Skew:                          -0.160   Prob(JB):                        0.388
Kurtosis:                       2.690   Cond. No.                         21.2
==============================================================================
```
In Period 1, the intercept of the regression is 26.0712 and the R-squared is 0.040. The R-squared is the proportion of the variation in the dependent variable that is predictable from the independent variable. In this case, unemployment does have and impact on inflation, but due to the R-squared being small, it is not the total determinant of inflation. This means that 4% of the variability observed in the target variable is explained by this regression model. Additionally, unemployment is statistically significant and as unemployment increases by 1%, inflation increases by 0.4169 percentage points. 

#### Period 2 (1967 - 1984) regression results.
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               CPIAUCSL   R-squared:                       0.619
Model:                            OLS   Adj. R-squared:                  0.617
Method:                 Least Squares   F-statistic:                     348.0
Date:                Sat, 23 Jul 2022   Prob (F-statistic):           9.30e-47
Time:                        20:29:42   Log-Likelihood:                -884.05
No. Observations:                 216   AIC:                             1772.
Df Residuals:                     214   BIC:                             1779.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -1.7768      3.520     -0.505      0.614      -8.715       5.162
UNRATE         9.8912      0.530     18.656      0.000       8.846      10.936
==============================================================================
Omnibus:                        1.392   Durbin-Watson:                   0.020
Prob(Omnibus):                  0.499   Jarque-Bera (JB):                1.476
Skew:                           0.183   Prob(JB):                        0.478
Kurtosis:                       2.825   Cond. No.                         24.1
==============================================================================
```
In Period 2, the intercept of the regression is -1.7768 and the R-squared is 0.619. The R-squared is the proportion of the variation in the dependent variable that is predictable from the independent variable. This means that 61.9% of the variability observed in the target variable is explained by this regression model. Additionally, unemployment is statistically significant and as unemployment increases by 1%, inflation increases by 9.8912 percentage points. 

#### Period 3 (1985 - 2002) regression results.
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               CPIAUCSL   R-squared:                       0.377
Model:                            OLS   Adj. R-squared:                  0.374
Method:                 Least Squares   F-statistic:                     129.3
Date:                Sat, 23 Jul 2022   Prob (F-statistic):           9.45e-24
Time:                        20:30:56   Log-Likelihood:                -930.60
No. Observations:                 216   AIC:                             1865.
Df Residuals:                     214   BIC:                             1872.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    221.1728      6.851     32.285      0.000     207.669     234.676
UNRATE       -13.3648      1.175    -11.373      0.000     -15.681     -11.049
==============================================================================
Omnibus:                       10.248   Durbin-Watson:                   0.012
Prob(Omnibus):                  0.006   Jarque-Bera (JB):                4.755
Skew:                          -0.072   Prob(JB):                       0.0928
Kurtosis:                       2.288   Cond. No.                         33.4
==============================================================================
```
In Period 3, the intercept of the regression is 221.1728 and the R-squared is 0.377. The R-squared is the proportion of the variation in the dependent variable that is predictable from the independent variable. This means that 37.7% of the variability observed in the target variable is explained by this regression model. Additionally, unemployment is statistically significant and as unemployment increases by 1%, inflation decreases by 13.3648 percentage points. 

#### Period 4 (2003 - 2022) regression results.
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               CPIAUCSL   R-squared:                       0.027
Model:                            OLS   Adj. R-squared:                  0.023
Method:                 Least Squares   F-statistic:                     6.368
Date:                Sat, 23 Jul 2022   Prob (F-statistic):             0.0123
Time:                        20:32:14   Log-Likelihood:                -1087.2
No. Observations:                 234   AIC:                             2178.
Df Residuals:                     232   BIC:                             2185.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept    240.8726      5.248     45.894      0.000     230.532     251.213
UNRATE        -2.0694      0.820     -2.523      0.012      -3.685      -0.454
==============================================================================
Omnibus:                        4.851   Durbin-Watson:                   0.004
Prob(Omnibus):                  0.088   Jarque-Bera (JB):                3.032
Skew:                          -0.058   Prob(JB):                        0.220
Kurtosis:                       2.455   Cond. No.                         20.7
==============================================================================
```
In Period 4, the intercept of the regression is 240.8726 and the R-squared is 0.027. The R-squared is the proportion of the variation in the dependent variable that is predictable from the independent variable. In this case, unemployment does have and impact on inflation, but due to the R-squared being small, it is not the total determinant of inflation. This means that 2.7% of the variability observed in the target variable is explained by this regression model. Additionally, unemployment is statistically significant and as unemployment increases by 1%, inflation decreases by 2.0694 percentage points. 

#### Overall (1948 - 2022) regression results.
                            OLS Regression Results                            
==============================================================================
Dep. Variable:               CPIAUCSL   R-squared:                       0.031
Model:                            OLS   Adj. R-squared:                  0.030
Method:                 Least Squares   F-statistic:                     28.99
Date:                Sat, 23 Jul 2022   Prob (F-statistic):           9.31e-08
Time:                        20:46:46   Log-Likelihood:                -5187.2
No. Observations:                 894   AIC:                         1.038e+04
Df Residuals:                     892   BIC:                         1.039e+04
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     67.7891      9.460      7.166      0.000      49.222      86.356
UNRATE         8.4992      1.579      5.384      0.000       5.401      11.597
==============================================================================
Omnibus:                      397.130   Durbin-Watson:                   0.002
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               82.872
Skew:                           0.494   Prob(JB):                     1.01e-18
Kurtosis:                       1.883   Cond. No.                         21.7
==============================================================================

Overall, the intercept of the regression is 67.7891 and the R-squared is 0.031. The R-squared is the proportion of the variation in the dependent variable that is predictable from the independent variable. In this case, unemployment does have and impact on inflation, but due to the R-squared being small, it is not the total determinant of inflation. This means that 3.1% of the variability observed in the target variable is explained by this regression model. Additionally, unemployment is statistically significant and as unemployment increases by 1%, inflation increases by 8.4992 percentage points.

## Possible Explanations

Why are we seeing low unemployment with high inflation?

+ Job Availability
  + Anyone who wants a job can get one, as there is a large group of people that simply dod not want to work.
+ Global Pandemic
  + Despite an intitial shart increase in job loss, many companies have now transitioned to a work-from-home model, limiting job cuts.
  
## Conclusion

Further research can be done to see what other factors influence the inflation rate. Some possible areas for futher investigation is that we can identify impacts of the central bank policy, such as asset purchases and interest rates (Fed funds rate), on unemployment and inflation. We could also look at how the S&P 500 and treasure rates could impact inflation. Additionally, we could utilize different variables to indicate the presence of a recession. 
