import requests
from datetime import datetime

url = "https://api.open-meteo.com/v1/forecast"
default_parms = {
    "latitude" : 51.1657,
    "longitude" : 10.4515,
    "hourly" : "temperature_2m"
}

def weather_checker(api_url = url, parms = default_parms):
    try:
        response = requests.get(api_url, params=parms, timeout=5)
        response.raise_for_status()
        data = response.json()
        temperature_list = data.get("hourly", {}).get("temperature_2m", [])
        temperature = {}
        for i, temp in enumerate(temperature_list[:5]):
            temperature[i] = temp
        return temperature
    except requests.exceptions.RequestException as e:
        print (f"{datetime.now()} | Exception - {e}")
        return {}

if __name__ == "__main__":
    forecast = weather_checker()
    if forecast:
        for i, temp in forecast.items():
            print(f"Hour {i} - The temperature is {temp}")
    else:
        print("Unable to get the temperature")