# Inflation Analysis

Our current economic climate is unique with the rise of the coronavirus. In the economy, we are seeing unique factors such as a high inflation rate paired with a low unemployment rate. Historically, stagflation or recession-inflation occurs which is a situation where the inflation rate is high and unemployment remains high as well. We are particularly interested to see how these changes in the unemployment rate are potentially impacting the increase in inflation rate. By using Python, we will analyze the impact of unemployment on inflation, but also other factors that could potentially impact inflation.

For more information on the research on inflation, I have written a paper on the current state and impacts on inflation for the year 2022: [Inflation & Monetary Policy](https://github.com/dosanity/unemployment-inflation-analysis/files/9175033/Inflation-and-Monetary-Policy.pdf)

## Data

Our data is from the Federal Reserve Bank of St. Louis. The Federal Bank is central to the nation's economy and provides economic resources and data for US economic statistical analysis. We also used Yahoo Finance which is data source to access stock market data.

For our X variables, we chose to look at the monthly unemployment rate (`UNRATE`), Federal Funds Effective Rate (`DFF`), and the S&P 500 Index (`SPY`). 

The unemployment rate represents the number of unemployed as a percentage of the labor force. Labor force data are restricted to people 16 years of age and older, who currently reside in 1 of the 50 states or the District of Columbia, who do not reside in institutions (e.g., penal and mental facilities, homes for the aged), and who are not on active duty in the Armed Forces. 

![fredgraph](https://user-images.githubusercontent.com/29410712/180629012-d348804f-6ace-4876-9450-54ed2b60e127.png)

The federal funds rate is the interest rate at which depository institutions trade federal funds (balances held at Federal Reserve Banks) with each other overnight. When a depository institution has surplus balances in its reserve account, it lends to other banks in need of larger balances. In simpler terms, a bank with excess cash, which is often referred to as liquidity, will lend to another bank that needs to quickly raise liquidity.

![fredgraph (1)](https://user-images.githubusercontent.com/29410712/196342930-e46e7545-8a26-403f-b104-bc098834424f.png)

The Standard and Poor's 500, or simply the S&P 500, is a stock market index tracking the stock performance of 500 large companies listed on stock exchanges in the United States. It is one of the most commonly followed equity indices.

For our Y variable, we chose to look at the Inflation Rate (`INFRATE`). We can calculate the inflation rate using the Consumer Price Index. The Consumer Price Index for All Urban Consumers: All Items (`CPIAUCSL`) is a price index of a basket of goods and services paid by urban consumers. Percent changes in the price index measure the inflation rate between any two time periods. The most common inflation metric is the percent change from one year ago. It can also represent the buying habits of urban consumers. This particular index includes roughly 88 percent of the total population, accounting for wage earners, clerical workers, technical workers, self-employed, short-term workers, unemployed, retirees, and those not in the labor force.

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

We then calculated the Inflation Rate by subtracting the past date CPI from the current date CPI and divide the answer by the past date CPI. From there, we multiplied the results by 100.

$$
Inflation\ Rate = (CPI_{x+1} - CPI_x) / CPI_x * 100
$$

#### Ordinary Least Squares Assumptions:

1. Standard Errors assume that the covariance matrix of the errors is correctly specified.
2. The condition number is large, 1.22e+03. This might indicate that there are strong multicollinearity or other numerical problems.
3. The linear regression model is "linear in parameters."
4. There is a random sampling of observations.
5. There is homoscedasticity and no autocorrelation.

## Unemployment Analysis

#### Period 1 (1948 - 1966) results.

<img src="https://user-images.githubusercontent.com/29410712/196335047-1dfbc943-9a49-4ef1-bebf-1f8e476ec41a.png"  width=50% height=50%>

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                INFRATE   R-squared:                       0.017
Model:                            OLS   Adj. R-squared:                  0.011
Method:                 Least Squares   F-statistic:                     2.582
Date:                Mon, 17 Oct 2022   Prob (F-statistic):              0.110
Time:                        22:20:53   Log-Likelihood:                -225.96
No. Observations:                 150   AIC:                             455.9
Df Residuals:                     148   BIC:                             461.9
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      2.2862      0.483      4.729      0.000       1.331       3.241
UNRATE        -0.1472      0.092     -1.607      0.110      -0.328       0.034
==============================================================================
Omnibus:                        0.263   Durbin-Watson:                   0.067
Prob(Omnibus):                  0.877   Jarque-Bera (JB):                0.376
Skew:                           0.091   Prob(JB):                        0.829
Kurtosis:                       2.835   Cond. No.                         29.4
==============================================================================
```
In Period 1, the intercept of the regression is 2.2862 and the R-squared is 0.017. The R-squared is the proportion of the variation in the dependent variable that is predictable from the independent variable. Due to the R-squared being small, it is not the total determinant of inflation. This means that around 1.7% of the variability observed in the target variable is explained by this regression model. Additionally, unemployment is not statistically significant and as unemployment increases by 1%, inflation rate decreases by 0.1472 percentage points. 

#### Period 2 (1967 - 1984) results.

<img src="https://user-images.githubusercontent.com/29410712/196335940-bd5a3c95-b27c-434a-ace4-20855a61594d.png"  width=50% height=50%>

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                INFRATE   R-squared:                       0.025
Model:                            OLS   Adj. R-squared:                  0.020
Method:                 Least Squares   F-statistic:                     5.374
Date:                Mon, 17 Oct 2022   Prob (F-statistic):             0.0214
Time:                        22:28:00   Log-Likelihood:                -549.38
No. Observations:                 215   AIC:                             1103.
Df Residuals:                     213   BIC:                             1109.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      5.0465      0.761      6.634      0.000       3.547       6.546
UNRATE         0.2652      0.114      2.318      0.021       0.040       0.491
==============================================================================
Omnibus:                       17.328   Durbin-Watson:                   0.018
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               18.012
Skew:                           0.666   Prob(JB):                     0.000123
Kurtosis:                       2.515   Cond. No.                         24.2
==============================================================================
```
In Period 2, the intercept of the regression is 5.0465 and the R-squared is 0.025. The R-squared is the proportion of the variation in the dependent variable that is predictable from the independent variable. This means that 2.5% of the variability observed in the target variable is explained by this regression model. Additionally, unemployment is statistically significant and as unemployment increases by 1%, inflation increases by 0.2652 percentage points. 

#### Period 3 (1985 - 2002) results.

<img src="https://user-images.githubusercontent.com/29410712/196336460-fd761db6-3e6c-4dc8-af94-33d2d7d6ce45.png"  width=50% height=50%>

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                INFRATE   R-squared:                       0.010
Model:                            OLS   Adj. R-squared:                  0.005
Method:                 Least Squares   F-statistic:                     2.062
Date:                Mon, 17 Oct 2022   Prob (F-statistic):              0.152
Time:                        22:32:49   Log-Likelihood:                -331.00
No. Observations:                 215   AIC:                             666.0
Df Residuals:                     213   BIC:                             672.7
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      2.4887      0.431      5.768      0.000       1.638       3.339
UNRATE         0.1064      0.074      1.436      0.152      -0.040       0.253
==============================================================================
Omnibus:                        9.557   Durbin-Watson:                   0.059
Prob(Omnibus):                  0.008   Jarque-Bera (JB):               10.056
Skew:                           0.529   Prob(JB):                      0.00655
Kurtosis:                       2.942   Cond. No.                         33.4
==============================================================================
```
In Period 3, the intercept of the regression is 2.4887 and the R-squared is 0.010. The R-squared is the proportion of the variation in the dependent variable that is predictable from the independent variable. Due to the R-squared being small, it is not the total determinant of inflation. This means that around 1% of the variability observed in the target variable is explained by this regression model. Additionally, unemployment is not statistically significant and as unemployment increases by 1%, inflation rate increase by 0.1064 percentage points.  

#### Period 4 (2003 - 2022) results.

<img src="https://user-images.githubusercontent.com/29410712/196337079-2b0bf44f-3fe4-418a-9329-91e1bdf036d8.png"  width=50% height=50%>

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                INFRATE   R-squared:                       0.147
Model:                            OLS   Adj. R-squared:                  0.144
Method:                 Least Squares   F-statistic:                     40.45
Date:                Mon, 17 Oct 2022   Prob (F-statistic):           1.05e-09
Time:                        22:40:33   Log-Likelihood:                -458.12
No. Observations:                 236   AIC:                             920.2
Df Residuals:                     234   BIC:                             927.2
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      4.5071      0.346     13.018      0.000       3.825       5.189
UNRATE        -0.3454      0.054     -6.360      0.000      -0.452      -0.238
==============================================================================
Omnibus:                       41.668   Durbin-Watson:                   0.084
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               61.971
Skew:                           1.038   Prob(JB):                     3.49e-14
Kurtosis:                       4.412   Cond. No.                         20.5
==============================================================================
```
In Period 4, the intercept of the regression is 4.5071 and the R-squared is 0.147. The R-squared is the proportion of the variation in the dependent variable that is predictable from the independent variable. This means that 14.7% of the variability observed in the target variable is explained by this regression model. Additionally, unemployment is statistically significant and as unemployment increases by 1%, inflation decreases by 0.3454 percentage points.  

#### Overall (1948 - 2022) results.

<img src="https://user-images.githubusercontent.com/29410712/196337627-b6f3fccc-51ce-477a-9ac6-cb302b8afd37.png"  width=50% height=50%>

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                INFRATE   R-squared:                       0.011
Model:                            OLS   Adj. R-squared:                  0.009
Method:                 Least Squares   F-statistic:                     8.767
Date:                Mon, 17 Oct 2022   Prob (F-statistic):            0.00316
Time:                        22:44:03   Log-Likelihood:                -2008.1
No. Observations:                 819   AIC:                             4020.
Df Residuals:                     817   BIC:                             4030.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      2.5340      0.363      6.971      0.000       1.821       3.248
UNRATE         0.1759      0.059      2.961      0.003       0.059       0.293
==============================================================================
Omnibus:                      214.844   Durbin-Watson:                   0.020
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              469.262
Skew:                           1.439   Prob(JB):                    1.26e-102
Kurtosis:                       5.340   Cond. No.                         23.2
==============================================================================
```

Overall, the intercept of the regression is 2.5340 and the R-squared is 0.011. The R-squared is the proportion of the variation in the dependent variable that is predictable from the independent variable. In this case, unemployment does have and impact on inflation, but due to the R-squared being small, it is not the total determinant of inflation. This means that 1.1% of the variability observed in the target variable is explained by this regression model. Additionally, unemployment is statistically significant and as unemployment increases by 1%, inflation increases by 0.1759 percentage points.

### Other Variables

In our next analysis, we will only look at the years 1993 - 2022 since the data available for `SPY` is between this time period.

```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                INFRATE   R-squared:                       0.234
Model:                            OLS   Adj. R-squared:                  0.228
Method:                 Least Squares   F-statistic:                     35.86
Date:                Mon, 17 Oct 2022   Prob (F-statistic):           3.03e-20
Time:                        23:10:04   Log-Likelihood:                -610.30
No. Observations:                 356   AIC:                             1229.
Df Residuals:                     352   BIC:                             1244.
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      1.2686      0.517      2.456      0.015       0.253       2.285
UNRATE        -0.0650      0.056     -1.151      0.250      -0.176       0.046
DFF            0.2578      0.050      5.178      0.000       0.160       0.356
SPY            0.0070      0.001      7.090      0.000       0.005       0.009
==============================================================================
Omnibus:                       36.171   Durbin-Watson:                   0.091
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               50.053
Skew:                           0.710   Prob(JB):                     1.35e-11
Kurtosis:                       4.165   Cond. No.                     1.22e+03
==============================================================================
```

From this analysis, we can see that the intercept of the regression is 1.2686 and the R-squared is 0.234. This means that 23.4% of the variability observed in the target variable is explained by this regression model. From our independent variables, we can see that the unemployment rate is not statistically significant while the federal funds rate and S&P 500 are statistically significant. Thus, as the federal funds rate increases by 1%, inflation increases by 0.2578 percentage points. This makes sense because the Federal Reserve increases the rate to combat inflation. High fed funds rate is correlated to high inflation etc. Additionally, as the the price of the S&P 500 Index increase by 1 percentage point, inflation increases by 0.007 percentage points. It shows that there is some impact from the S&P 500, but it isn't large.


### Possible Explanations

Why are we seeing low unemployment with high inflation?

+ Job Availability
  + Anyone who wants a job can get one, as there is a large group of people that simply do not want to work.
+ Global Pandemic
  + Despite an intitial short increase in job loss, many companies have now transitioned to a work-from-home model, limiting job cuts. 
