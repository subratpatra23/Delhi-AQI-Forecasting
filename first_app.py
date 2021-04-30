import pandas as pd 
import statsmodels.api as sm
import pickle

##Load the Dataset
cleaneddata = pd.read_csv("D:\\project new\\delhi_AQIclean.csv",index_col=0)
##Create & fit the model
model=sm.tsa.statespace.SARIMAX(cleaneddata,order=(2, 1, 2),seasonal_order=(2,0,2,24)).fit()
#Dump the model in pickel file    
pickle.dump(model, open('model.pkl', 'wb'))
