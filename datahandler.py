
import pandas as pd
# first API volumn is bs...
#How to store
#path = r"/User/mengdantian/Desktop/quantitative strategy/trend/"

import pandas.io.data as web
listOfCur =  ['JPY','CAD','EUR','GBP','CHF','SGD','INR','MXN','AUD','NZD']
#'EUR','GBP','CHF','SGD','INR','MXN','AUD','NZD'
historicalCur = {}
for cur in listOfCur:
    historicalCur[cur] = web.DataReader(cur+'=X','yahoo')
    #historicalCur[cur].iloc[::-1]
    historicalCur[cur].to_csv(cur+'.csv',sep=',')




