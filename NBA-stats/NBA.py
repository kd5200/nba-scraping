import pandas as pd
import requests
import time
import numpy as np 
pd.set_option('display.max_columns', None) # so we can see all columns in a wide DataFrame


test_URL="https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2011-12&SeasonType=Regular%20Season&StatCategory=PTS"

r = requests.get(url=test_URL).json()

table_headers = r['resultSet']['headers']

pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)

df = pd.DataFrame(columns = table_headers)

print(df)