import re
import json
import requests
import csv
import pandas as pd
import datetime
import time

## Set Up Query Headers and url
headers = {'Content-type': 'application/json', 'Accept': 'application/json',
        'Authorization': 'API-Key y3ztpada92a72ykqgb2spnuy7y8upapl#hjw19efv327liz2nxpwpt5wehpdafsc2dnrv8l0zb01cjp10sjlgke2z9oeai8gt'}
url = 'https://business-playlive.railsbank.com/v1/railsbank/biz-team/query-database'

## Import Datomic Query ##
with open("/Users/john/Documents/Code/Scripting/Notifications2.json",'r') as file:
    data = file.read()


#initilise overall dataframe
overall_df = pd.DataFrame()

## Set initial parameter
from_date = datetime.datetime(2017,1,1,00,00,000)
to_date = from_date + datetime.timedelta(weeks=8)

print(from_date)
print(to_date)

for i in range (24):
#Fill parameter list

    from_date = from_date + datetime.timedelta(weeks=8)
    to_date = to_date + datetime.timedelta(weeks=8)

    print("iteration",i)

    ## input parameter to query
    query = data.replace(("{{from_date}}"),str(from_date.isoformat()))
    query = query.replace(("{{to_date}}"),str(to_date.isoformat()))

    print (from_date)
    print(to_date)
    
    ## Wait to reduce load on biz server

    
    print(query)
    ## POST Request ##
    response = requests.post(url, data=query, headers=headers)
    
    print (response.json())
    df = pd.DataFrame(response.json())
    overall_df = overall_df.append(df)

    
    
    
overall_df.to_csv('/Users/john/Documents/Code2/Scripting/Dalton_sum_balances.csv')
