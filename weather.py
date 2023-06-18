import requests

api_key = '86469fb40636fb08b5b59eb9cce4bb69'
base_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{base_url}?appid={api_key}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("An error occured.")