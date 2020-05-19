import pandas as pd
import numpy as np
def get_countrywise_data(country_code=None):
    url="https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    raw_data= pd.read_csv(url,error_bad_lines=False)
    country_data = None
    if country_code is not None:
        country_data=raw_data[raw_data['iso_code']==country_code].copy()
        country_data.reset_index(drop=True,inplace=True)
        country_data['date']=pd.to_datetime(country_data['date'])
        shifted_date=country_data['date'].shift(periods = 1,fill_value=country_data['date'].iloc[0])
        shifted_date.drop(shifted_date.tail(1).index,inplace=True)
        country_data['days']=country_data['date'].diff(1)
        country_data['days'].iloc[0]=np.timedelta64(0,'D')
        country_data['days']=country_data['days'].cumsum()
    else:
        country_data = raw_data
    return country_data
