from fredapi import Fred
import pandas as pd

API_KEY = "3df2eebc0e5c86669deee55302bd4d12"

fred = Fred(api_key=API_KEY)

sp500 = fred.get_series('SP500')  

# To DataFrame
df = sp500.reset_index()
df.columns = ['date', 'close']

# save to data folder 
df.to_csv('data/sp500_raw.csv', index=False)

print("Saved SP500 data to data/sp500_raw.csv")
