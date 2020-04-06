import pandas as pd

num_days, top_n = 5, 25
df = pd.read_csv("csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_global.csv")
df = df.groupby(by=['Country/Region'], as_index=False).sum()
#df = df[df['Country/Region']=='Australia'] # Set the filter to get a specific Country

# Find the last n-day average mortality, sort descending and take top_n
n_day_avg = str(num_days)+'DayAvg'
df[n_day_avg] = (df[df.columns[-1]] - df[df.columns[-1-num_days]])/num_days
df.sort_values(by=[n_day_avg], ascending=False, inplace=True)
df = df.head(top_n)

# Update the last n columns with mortality increase from previous date
cols = ['Country/Region', n_day_avg]
for i in range(2,num_days+2):
    dt, prev_dt = df.columns[-i], df.columns[-i-1]
    df[dt] = df[dt].map(str) + ' (' + (df[dt] - df[prev_dt]).map(str) + ')'
    cols.append(dt)
print(df[cols])
