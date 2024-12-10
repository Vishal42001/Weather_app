import json
import requests

#API to Fetch Temp. Of A City
city_name=input("Enter the city name:")
api_key='bc4d8169a8af9f06be559d89b2b7af4e'

#To build the API URL:
api_URL=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
get_server_info=requests.get(api_URL)
data=get_server_info.json()
print(data)

pretty_data=json.dumps(data,indent=4)
print(pretty_data)

#To Fetch Specific Data From JSON:
D=data["weather"][0]['description']
T=data["main"]['temp']
H=data["main"]['humidity']
print(f'The Current Weather is:{D} & Temperature is:{T} & Humidity is:{H}')
