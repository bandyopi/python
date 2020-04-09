import pandas as pd, matplotlib.pyplot as plot

num_days, top_n = 5, 20
df = pd.read_csv("csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_global.csv")
#df = df[df['Country/Region']=='Australia'] # Set the filter to get a specific Country
df = df.groupby(by=['Country/Region'], as_index=False).sum()
total_mortality = df[df.columns[-1]].sum()

# Find the last n-day average mortality, sort descending and take top_n
n_day_avg = str(num_days)+'DayAvg'
df[n_day_avg] = (df[df.columns[-1]] - df[df.columns[-1-num_days]])/num_days
df.sort_values(by=[n_day_avg], ascending=False, inplace=True)
df = df.head(top_n)

# Update the last n columns with mortality increase from previous date
cols = ['Country/Region', n_day_avg]
for i in range(2,num_days+2):
    dt, prev_dt = df.columns[-i], df.columns[-i-1]
    df[dt] = df[dt].map(str) + ' [+' + (df[dt] - df[prev_dt]).map(str) + ']'
    cols.append(dt)
print('Displaying', num_days, 'days stats for top', top_n, 'countries by mortality. Total', 
    total_mortality, 'reported mortalities asOf', df.columns[-2])
print(df[cols])
#ax=df.plot.bar(x='Country/Region', y=n_day_avg, rot=0)
#plot.show()