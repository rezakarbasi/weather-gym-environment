import pandas as pd

df = pd.read_csv('wa_weather_1944_till_2016.csv')

rain = df.groupby('Year')['rainfall_mm'].sum().to_frame()
min_temp = df.groupby('Year')['min_temp_C'].min().to_frame()
max_temp = df.groupby('Year')['max_temp_C'].max().to_frame()
ave_temp = df.groupby('Year')['daily_avg'].mean().to_frame()

result = pd.concat([rain,min_temp,max_temp,ave_temp], axis=1)
result.to_csv('weather-yearly.csv')