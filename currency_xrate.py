import requests, json

response = requests.get("https://api.exchangeratesapi.io/latest?symbols=USD")
j = json.loads(response.text)
print(j["date"]) 