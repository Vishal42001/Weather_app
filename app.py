from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_weather_data(city_name):
    api_key = 'bc4d8169a8af9f06be559d89b2b7af4e'  # Replace with your own API key if needed
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if "weather" in data:
            D = data["weather"][0]['description']
            T = data["main"]['temp']
            H = data["main"]['humidity']
            icon = data["weather"][0]["icon"]  # Get the icon code
            return {"description": D, "temperature": T, "humidity": H, "icon": icon}
        else:
            return {"error": "City not found or invalid response"}
    else:
        return {"error": "Failed to retrieve data"}

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    city_name = None
    if request.method == 'POST':
        city_name = request.form.get('city_name')
        weather_data = get_weather_data(city_name)
    return render_template('index.html', weather_data=weather_data, city_name=city_name)

if __name__ == '__main__':
    app.run(debug=True)
