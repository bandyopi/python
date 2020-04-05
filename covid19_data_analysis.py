import pandas as pd

df = pd.read_csv("csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_deaths_global.csv")
num_days, top_n = 5, 25

# Find the latest date and short by the lates date desc
latest_date = df.columns[-1]
previous_date = df.columns[-2]
df.sort_values(by=[latest_date], ascending=False, inplace=True)

# Find the last n columns
last_col = df.columns.size
last_n_col = df.columns[1:2].append(df.columns[last_col-num_days:last_col])
top_df=df[last_n_col].head(top_n)

print("Top", top_n, "countries by death asOf:", latest_date )
print(pd.concat([top_df, top_df[latest_date].sub(top_df[previous_date]).to_frame('increase')], axis=1))
