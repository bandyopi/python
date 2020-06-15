import pandas as pd
import matplotlib.pyplot as plt
import requests
from os import getcwd
from io import StringIO

num_days, top_n, country = 7, 20, 'Country/Region'

# Download file from GitHub using the "raw" url (note the "...COVID-19/blob/master/..." replace with "...COVID-19/master/...")
covid_mortality_csv = requests.get('https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
df = pd.read_csv(StringIO(covid_mortality_csv.text)) # don't use .content as it returns bytes
#df = pd.read_csv("csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_global.csv")
# df = df[df[country]=='India'] # Set the filter to get a specific Country
df = df.groupby(by=[country], as_index=False).sum()
dt_latest = df.columns[-1]
total_mortality = df[dt_latest].sum()

# Find the last n-day moving average mortality since 1st March, sort descending and take top_n
n_day_avg = str(num_days)+'DayAvg'
df[n_day_avg] = round((df[dt_latest] - df[df.columns[-1-num_days]])/num_days, 1)
df.sort_values(by=[n_day_avg], ascending=False, inplace=True)
df = df.head(top_n)
df_sma = pd.DataFrame()
df_sma[country] = df[country]
df_sma[dt_latest] = df[n_day_avg]
i = 2
dt = df.columns[-i]
while dt != '2/29/20':
    dt_prev = df.columns[-i-num_days]
    df_sma[dt] = round((df[dt] - df[dt_prev])/num_days, 1)
    i += 1
    dt = df.columns[-i]
#print(df_sma)

# Update the last n columns with mortality increase from previous date
cols = [country, n_day_avg]
for i in range(2,num_days+2):
    dt, dt_prev = df.columns[-i], df.columns[-i-1]
    df[dt] = df[dt].map(str) + ' [+' + (df[dt] - df[dt_prev]).map(str) + ']'
    cols.append(dt)
print('Displaying last', num_days, 'days stats for top', top_n, 'countries by mortality. Total', 
    f"{total_mortality:,d}", 'reported mortalities asOf', dt_latest)
print(df[cols])
#print(pd.concat([df[cols], df_sma], axis=1))

# Plot the SMA for top 5 countries
  # Need to set the dataframe index to 'country' 
  #  so the dataframe can be transposed with 'country' becoming column header instead of numeric indexes in df_sma
  # The transpose() 'T' is needed  because dataframe plots line series per column 
  # The iloc[::-1] is to reverse the row ordering (date shorting)
df_plt = df_sma.head(7).set_index(country).T.iloc[::-1]
dates = df_plt.index[0::7] # select every 7th day from the date list
#print(dates)
df_plt.plot(kind='line')
# Set plot Title and Axis labels
plt.title(str(num_days) + ' day moving average mortality for top 7 countries')
plt.xlabel('Date ->')
plt.ylabel('Mortality (' + str(num_days) + ' Days SMA) ->')
# Set Axis ticks
plt.xticks(ticks=range(0, len(df_plt.index)), labels=df_plt.index, rotation='vertical')
plt.yticks(ticks=range(0, int(df_plt.max(axis=1).max())+100, 100))
print('\n', df_plt.tail(14))
# Show every 7th x tick label - hiding the rest
[lbl.set_visible(False) for (i,lbl) in enumerate(plt.gca().xaxis.get_ticklabels()) if i % 7 != 0]
# Show grid lines
plt.grid(b=True, which='major', axis='y', color='lightgray', linewidth=1, linestyle='dotted')

plt.show()
