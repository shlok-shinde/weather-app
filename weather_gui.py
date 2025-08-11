import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
  city = city_entry.get().strip()
  if not city:
    messagebox.showerror("Error", "Please enter a city name.")
    return
  url = f"https://wttr.in/{city}?format=j1"

  try:
      response = requests.get(url)
      response.raise_for_status()
      data = response.json()

      current = data["current_condition"][0]
      temp_c = current["temp_C"]
      feels_like_c = current["FeelsLikeC"]
      humidity = current["humidity"]
      wind_speed = current["windspeedKmph"]
      weather_desc = current["weatherDesc"][0]["value"]

      weather_details = (
          f"Weather: {weather_desc}\n"
          f"Temperature: {temp_c}°C (Feels like {feels_like_c}°C)\n"
          f"Humidity: {humidity}%\n"
          f"Wind Speed: {wind_speed} km/h"
      )

      weather_result.set(weather_details)
      weather_icon.set(get_weather_emoji(weather_desc))

  except requests.exceptions.RequestException:
      messagebox.showerror("Error", "Failed to fetch weather data.")

def get_weather_emoji(condition):
  condition = condition.lower()
  if "sun" in condition:
    return "☀️"
  elif "cloud" in condition:
    return "☁️"
  elif "rain" in condition:
    return "🌧️"
  elif "snow" in condition:
    return "❄️"
  elif "thunder" in condition:
    return "⛈️"
  else:
    return "🌏"
  
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="#2C3E50")
root.resizable(False, False)

title_label = tk.Label(root, text="🌤 Weather App", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white")
title_label.pack(pady=10)

city_label = tk.Label(root, text="Enter City:", font=("Arial", 12), bg="#2C3E50", fg="white")
city_label.pack(pady=5)

city_entry = tk.Entry(root, bg="#34495E", fg="white", font=("Arial", 14), justify="center")
city_entry.pack(pady=5)

get_btn = tk.Button(root, text="Get Weather", font=("Arial", 12, "bold"), bg="#1ABC9C", fg="white", command=get_weather)
get_btn.pack(pady=5)

weather_icon = tk.StringVar()
weather_icon_label = tk.Label(root, textvariable=weather_icon, bg="#2C3E50", fg="white", font=("Arial", 24))
weather_icon_label.pack(pady=5)

weather_result = tk.StringVar()
weather_result_label = tk.Label(root, textvariable=weather_result, bg="#2C3E50", fg="white", font=("Arial", 14))
weather_result_label.pack(pady=5)

root.mainloop()