import pandas as pd

df = pd.read_csv("D:\\Data\\covid-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_global.csv")
num_days, top_n = 5, 2

# Find the latest date and short by the lates date desc
latest_date = df.columns[-1]
df.sort_values(by=[latest_date], ascending=False, inplace=True)

# Find the last n columns
last_col = df.columns.size
last_n_col = df.columns[1:2].append(df.columns[last_col-num_days:last_col])
print(last_n_col)

print("Top 10 countries by death asOf: " + latest_date )
print(df[last_n_col].head(15))

