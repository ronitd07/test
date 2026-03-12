import requests
import json
import datetime

def get_weather(city):
    api_key = "aed9ccb74c74b0ac39685fac78bb1c48"  # Replace with your OpenWeather API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For Celsius
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        with open(f"{city}_weather.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Weather in {city}:\n")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"☁ Condition: {data['weather'][0]['description'].capitalize()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        print(f"🌡 Pressure: {data['main']['pressure']/1e3} bar")
        sunrise_timestamp = data["sys"]["sunrise"]   # e.g., 1756165642
        sunset_timestamp = data["sys"]["sunset"]
        timezone_offset = data["timezone"]
        # Create timezone object from offset
        tz = datetime.timezone(datetime.timedelta(seconds=timezone_offset))

        # Convert timestamps using fromtimestamp with tz
        sunrise_time = datetime.datetime.fromtimestamp(sunrise_timestamp, tz=tz)
        sunset_time = datetime.datetime.fromtimestamp(sunset_timestamp, tz=tz)
        

        print("🌅 Sunrise:", sunrise_time.strftime("%H:%M:%S"))
        print("🌇 Sunset:", sunset_time.strftime("%H:%M:%S"))
    else:
        print("City not found or error fetching data.")
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)