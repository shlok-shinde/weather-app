import requests

def get_weather(city):
  url = f"https://wttr.in/{city}?format=j1"
  response = requests.get(url)

  if response.status_code == 200:
    data = response.json()
    current = data["current_condition"][0]
    temp = current["temp_C"]
    weather = current["weatherDesc"][0]["value"]
    feels_like = current["FeelsLikeC"]
    humidity = current["humidity"]
    print(f"\nWeather in {city.capitalize()}:")
    print(f"Weather: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
  else:
    print("Error fetching weather data.")

if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)