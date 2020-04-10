import pandas as pd, matplotlib.pyplot as plt

num_days, top_n, country = 5, 20, 'Country/Region'

df = pd.read_csv("csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_global.csv")
#df = df[df[country]=='Australia'] # Set the filter to get a specific Country
df = df.groupby(by=[country], as_index=False).sum()
dt_latest = df.columns[-1]
total_mortality = df[dt_latest].sum()

# Find the last n-day moving average mortality for the last n days, sort descending and take top_n
n_day_avg = str(num_days)+'DayAvg'
df[n_day_avg] = (df[dt_latest] - df[df.columns[-1-num_days]])/num_days
df.sort_values(by=[n_day_avg], ascending=False, inplace=True)
df = df.head(top_n)
df_sma = pd.DataFrame()
df_sma[country] = df[country]
df_sma[dt_latest] = df[n_day_avg]
for i in range(2, 16): #num_days+2):
    dt, dt_prev = df.columns[-i], df.columns[-i-num_days]
    df_sma[dt] = (df[dt] - df[dt_prev])/num_days
#print(df_sma)

# Update the last n columns with mortality increase from previous date
cols = [country, n_day_avg]
for i in range(2,num_days+2):
    dt, dt_prev = df.columns[-i], df.columns[-i-1]
    df[dt] = df[dt].map(str) + ' [+' + (df[dt] - df[dt_prev]).map(str) + ']'
    cols.append(dt)
print('Displaying last', num_days, 'days stats for top', top_n, 'countries by mortality. Total', 
    total_mortality, 'reported mortalities asOf', dt_latest)
print(df[cols])
#print(pd.concat([df[cols], df_sma], axis=1))

# Plot the SMA for top 5 countries
  # Need to set the dataframe index to 'country' 
  #  so the dataframe can be transposed with 'country' becoming column header instead of numeric indexes in df_sma
  # The transpose() 'T' is needed  because dataframe plots line series per column 
  # The iloc[::-1] is to reverse the row ordering (date shorting)
df_plt = df_sma.head(5).set_index(country).T.iloc[::-1]
#print(df_plt)
df_plt.plot(kind='line')
ax = plt.gca()
#ax.set_xlabels(df_plt.index)
#for i in range(1, len(df.index)+1):
 #   df_plt.plot(kind='line', y=df_plt.columns[-i], x=country, ax=ax)
#plt.xscale(df_plt.index)
plt.title('5 day moving agerage mortality by top 5 countroes')
plt.xlabel('Date ->')
plt.ylabel('Mortality (5 Days SMA) ->')
plt.show()