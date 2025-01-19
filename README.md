# 🌦️ Weather App

A simple **Flask-based web application** to fetch and display the current weather conditions for any city using the **OpenWeatherMap API**.

---

## 🚀 Features
- 🌍 **Search Weather by City**: Enter the name of any city to get real-time weather updates.
- 📋 **Displays**:
  - Current weather description.
  - Temperature in Celsius (°C).
  - Humidity levels (%).
  - Weather icon for better visualization.
- 🚦 **Error Handling**:
  - Handles invalid city names gracefully.
  - Displays error messages for failed API calls.

---

## 🛠️ Technologies Used
- **Python** 🐍
- **Flask** (Web Framework)
- **HTML** for front-end design.
- **OpenWeatherMap API** for fetching weather data.

---

## ✅ Prerequisites
Make sure you have the following installed before running the app:
- **Python** 3.7 or above.
- Flask: Install using `pip install flask`
- Requests library: Install using `pip install requests`

---

## 📖 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Vishal42001/Weather_app.git
cd weather-app

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Replace API Key
Open the file app.py.
Replace the api_key value with your OpenWeatherMap API key:
api_key = 'your-api-key-here'
Don't have an API key? Sign up for free at OpenWeatherMap.

4️⃣ Run the Application
python app.py

Open your browser and navigate to:
http://127.0.0.1:5000

🌈 Usage
Enter the city name in the search box.
Click on "Get Weather".
View the current weather details, including:
Description.
Temperature.
Humidity.
Weather icon.
📸 Screenshots
https://github.com/Vishal42001/Weather_app/blob/main/weather_ss.png

🏠 Home Page

🐞 Troubleshooting
App doesn't run?

Ensure Flask and Requests are properly installed.
Run pip install -r requirements.txt to reinstall dependencies.
Weather data not displayed?

Double-check your API key and replace it if necessary.
Verify your network connectivity.
