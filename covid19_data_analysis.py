import pandas as pd

df = pd.read_csv("C:\\data\\covid-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_global.csv")
latest_date = df.columns[-1]
df.sort_values(by=[latest_date], ascending=False, inplace=True)
print("Top 10 countries by death asOf: " + latest_date )
print(list("Country/Region").append(df.columns[df.columns.size-5:df.columns.size]))
print(df[["Country/Region", df.columns[-5], df.columns[-4], df.columns[-3], df.columns[-2], latest_date]].head(15))

