import pandas as pd
import numpy as np
JPY = pd.read_csv('JPY.csv')
def sma(pn_data, index, window):
    return np.mean(pn_data[index- window: index]['Adj Close'])

#write a pandas ...
listofdays = [5,10,15,20,30,45]
technicalJPY = pd.DataFrame(index = JPY['Date'][:50])

for day in listofdays:
    technicalJPY.loc[day:,'sma'+str(day)+'d']= list(sma(JPY, index, day) for index in xrange(day, 50))
    print technicalJPY[40:]
#update function
current = "2010-03-12"
technicalJPY.loc[current] =[sma(JPY, 51, day) for day in listofdays]
print technicalJPY[40:]
    #print technicalJPY[40:]
