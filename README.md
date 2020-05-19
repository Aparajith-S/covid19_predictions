# Project description
To Analyze and predict the outcome of new cases by country and find the trend of the number of cases in each of these countries.

## Code
- `fetchData.py` implements helpers to fetch covid19 data from OWID repo
    - `get_countrywise_data(country_code=None)` gets data from the country of interest
        `country_code = None` will return the data with all countries
         `country_code = 'IND' ` will get all data corresponding to the ISO code IND - India and will use the date column to add number of                                  days elapsed since start of data collection (datetime delta) to be further used for exploratory data  
                                 analysis
        
## Data
The data will be directly used from the master branch of OWID/Covid-19-data so that the daily updates 
will help build a unsupervised learning model to predict future outcomes.

https://github.com/owid/covid-19-data
