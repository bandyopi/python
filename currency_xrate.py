import requests, json

response = requests.get("https://api.exchangeratesapi.io/latest?symbols=USD")
j = json.loads(response.text)
print(j["date"]) 

response = requests.get("https://raw.github.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")
print(response.text)