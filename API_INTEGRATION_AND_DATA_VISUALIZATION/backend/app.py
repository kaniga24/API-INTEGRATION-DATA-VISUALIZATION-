from flask import Flask, jsonify
import requests
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

app = Flask(__name__)

API_KEY = "a3926edb7093c40b6455ce1b366c62a7"
CITY = "Chennai"

@app.route("/")
def home():
    return "Flask server is running. Use /weather"

@app.route("/weather")
def weather_data():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    sns.set(style="whitegrid")
    plt.figure()
    plt.bar(["Temperature", "Humidity"], [temp, humidity])
    plt.title("Weather Data")
    plt.savefig("static/weather.png")
    plt.close()

    return jsonify({
        "city": CITY,
        "temperature": temp,
        "humidity": humidity
    })

if __name__ == "__main__":
    app.run(debug=True)