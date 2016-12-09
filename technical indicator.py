import pandas as pd
import numpy as np
import csv
import os

# fUNCTIONS OBJECTIVE: calculate sma based on different windows and write csv, update new sma for new data coming and
#update corresponding csv, kept only the most recently csv for indicator

def sma(pn_data, index, window):
    return np.mean(pn_data[index- window: index]['Adj Close'])

def historicalTechnical(listofdays, techIndName,underlying):
    underlyingData = pd.read_csv(underlying+'.csv')
    technicalpd = pd.DataFrame(index = underlyingData['Date'])
    obs = len(underlyingData)
    lastDate = technicalpd.index[-1]
    for day in listofdays:
        technicalpd.loc[day:,techIndName+str(day)+'d']= list(sma(underlyingData, index, day) for index in xrange(day, obs))
    #write into csv
    technicalpd.to_csv(techIndName + underlying + lastDate + '.csv')

historicalTechnical([5,10,15,20,30,45], 'sma','JPY') # get the historical up to date sma
#update function and csv file
def updateTechnical(listofdays, techIndName, underlying, currentDate,lastDate):
    underlyingData = pd.read_csv(underlying + '.csv')
    try:
        underlyingData.index[-1] == currentDate #check if the lastline of original data is the currentdate
        smanew =  [sma(underlyingData,len(underlyingData), day) for day in listofdays] #new sma for the current rate only
        newrow = [currentDate]
        newrow.extend(smanew) #write it to a list of string for the appending row for csc
        try:
            if os.path.exists(techIndName + underlying + currentDate + '.csv'):
                print "check if technical indicator it is alrady up to date"
        except:
            if not os.path.exists(techIndName + underlying + lastDate + '.csv'): # check if the lastdate.csv exists
                file(techIndName + underlying + lastDate + '.csv', 'w').close()
                print "pls check if the lastdate technicalindicator csv is here"
            else:#update a new row with current date indicators
                with open(techIndName + underlying + lastDate + '.csv', 'a') as f:
                    writer =  csv.writer(f)
                    writer.writerow(newrow)
                os.rename(techIndName + underlying + lastDate + '.csv', techIndName + underlying + currentDate + '.csv')#update csv name
    except:
        print "pls check the new original data is up to date"

updateTechnical([5,10,15,20,30,45], 'sma','JPY',"2016-12-05","2016-12-02")
