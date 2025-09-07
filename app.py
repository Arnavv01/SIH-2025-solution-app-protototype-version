from flask import Flask, render_template, request
import requests

app = Flask(__name__)

locations = {
    # UP districts
    "Noida": {"coords": (28.5355, 77.3910), "hindi": "नोएडा"},
    "Ghaziabad": {"coords": (28.6692, 77.4538), "hindi": "ग़ाज़ियाबाद"},
    # Punjab Districts
    "Amritsar": {"coords": (31.6340, 74.8723), "hindi": "अमृतसर"},
    "Barnala": {"coords": (30.3741, 75.5489), "hindi": "बरनाला"},
    "Bathinda": {"coords": (30.2109, 74.9455), "hindi": "बठिंडा"},
    "Faridkot": {"coords": (30.6769, 74.7584), "hindi": "फ़रीदकोट"},
    "Fatehgarh Sahib": {"coords": (30.6425, 76.4016), "hindi": "फतेहगढ़ साहिब"},
    "Fazilka": {"coords": (30.4036, 74.0284), "hindi": "फाजिल्का"},
    "Firozpur": {"coords": (30.9251, 74.6131), "hindi": "फ़िरोज़पुर"},
    "Gurdaspur": {"coords": (32.0419, 75.4050), "hindi": "गुरदासपुर"},
    "Hoshiarpur": {"coords": (31.5326, 75.9115), "hindi": "होशियारपुर"},
    "Jalandhar": {"coords": (31.3260, 75.5762), "hindi": "जालंधर"},
    "Kapurthala": {"coords": (31.3796, 75.3810), "hindi": "कपूरथला"},
    "Ludhiana": {"coords": (30.9010, 75.8573), "hindi": "लुधियाना"},
    "Malerkotla": {"coords": (30.5309, 75.8715), "hindi": "मलेरकोटला"},
    "Mansa": {"coords": (29.9995, 75.3937), "hindi": "मंसा"},
    "Moga": {"coords": (30.8130, 75.1688), "hindi": "मोगा"},
    "Sri Muktsar Sahib": {"coords": (30.4762, 74.5111), "hindi": "श्री मुक्तसर साहिब"},
    "Pathankot": {"coords": (32.2643, 75.6421), "hindi": "पठानकोट"},
    "Patiala": {"coords": (30.3398, 76.3869), "hindi": "पटियाला"},
    "Rupnagar": {"coords": (30.9685, 76.5274), "hindi": "रूपनगर"},
    "Mohali": {"coords": (30.7046, 76.7179), "hindi": "मोहाली"},
    "Sangrur": {"coords": (30.2458, 75.8420), "hindi": "संगरूर"},
    "Nawanshahr": {"coords": (31.1256, 76.1189), "hindi": "नवांशहर"},
    "Tarn Taran": {"coords": (31.4517, 74.9274), "hindi": "तरण तारण"}
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/crops")
def crops():
    return render_template("crops.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

@app.route("/market")
def market():
    return render_template("market.html")

@app.route("/weather", methods=["GET", "POST"])
def weather():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        if city in locations:
            lat, lon = locations[city]["coords"]
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=relative_humidity_2m,precipitation"
            response = requests.get(url).json()

            if "current_weather" in response:
                current = response["current_weather"]
                times = response["hourly"]["time"]
                humidities = response["hourly"]["relative_humidity_2m"]
                precipitations = response["hourly"]["precipitation"]

                if current["time"] in times:
                    idx = times.index(current["time"])
                    humidity = humidities[idx]
                    rainfall = precipitations[idx]
                else:
                    humidity = None
                    rainfall = None

                weather_data = {
                    "city": city,
                    "temperature": current["temperature"],
                    "humidity": humidity,
                    "rainfall": rainfall,
                    "time": current["time"]
                }
            else:
                error = "Weather data unavailable"
        else:
            error = "City not found"

    return render_template("weather.html", weather=weather_data, error=error, locations=locations)

if __name__ == "__main__":
    app.run(debug=True)
