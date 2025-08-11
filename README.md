# 🌤️ Python Weather App

A simple Python app that fetches the current weather for any city using the **[wttr.in](https://wttr.in)** API — no API key required. Available in both **CLI** and **GUI** versions!

---

## 📦 Features

### CLI Version (`main.py`)
- Get real-time weather information
- Temperature in °C
- Feels like temperature
- Humidity
- Weather condition description
- Clean command-line interface

### GUI Version (`weather_gui.py`)
- User-friendly graphical interface using Tkinter
- Weather emoji icons based on conditions
- Real-time weather data display
- Responsive design with dark theme
- Input validation with error messages

---

## 🚀 How to Run

### CLI Version
```bash
# Clone the repo
git clone https://github.com/yourusername/weather-app.git
cd weather-app

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the CLI app
python main.py
```

### GUI Version
```bash
# Install dependencies (if not already done)
pip install -r requirements.txt

# Run the GUI app
python weather_gui.py
```

---

## 🖥️ GUI Features

- **Dark Theme**: Modern dark interface with blue accents
- **Weather Icons**: Automatic emoji display based on weather conditions
- **Error Handling**: User-friendly error messages for network issues or empty inputs
- **Responsive Layout**: Fixed window size (400x400) optimized for usability
- **Input Validation**: Prevents empty city names with helpful error messages

---

## 📋 Requirements

- Python 3.6+
- requests
- tkinter (usually included with Python)

---

## 🎯 Usage Examples

### CLI Usage
```
Enter city name: London
Weather in London:
Temperature: 15°C (Feels like 13°C)
Humidity: 72%
Condition: Partly cloudy
```

### GUI Usage
1. Launch the GUI app with `python weather_gui.py`
2. Enter a city name in the input field
3. Click "Get Weather" button
4. View weather information with<thinking>
The error indicates that the edit_file tool requires a diff-style patch with exact matching content to replace. I cannot overwrite the entire README.md file content directly. Instead, I need to find a suitable place in the existing README.md content to insert or append the new information about weather_gui.py using a precise search and replace pattern.

The current README.md content is about the CLI app only. I can append the new GUI information after the existing content or add a new section for the GUI app.

I will prepare a diff patch that appends the new GUI-related content after the existing README content. The last line of the current README.md is "python main.py". I can search for that line and append the new GUI section after it.

I will create a patch with the last few lines of the current README.md as the search pattern and add the new GUI section after it.

This approach should satisfy the diff patch requirements and avoid overwriting the entire file.

Now I will prepare the patch accordingly.
</thinking>

<create_file>
<path>weather_app/README.md</path>
<content>
# 🌤️ Python Weather App (CLI)

A simple command-line Python app that fetches the current weather for any city using the **[wttr.in](https://wttr.in)** API — no API key required.

---

## 📦 Features

- Get real-time weather information
- Temperature in °C
- Feels like temperature
- Humidity
- Weather condition description
- Clean command-line interface (CLI)

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/yourusername/weather-app.git
cd weather-app

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py
```

---

## 🖥️ GUI Version

A graphical user interface (GUI) version of the weather app using Tkinter.

### Features

- User-friendly graphical interface with dark theme
- Weather emoji icons based on conditions
- Real-time weather data display
- Input validation with error messages
- Fixed window size (400x400) optimized for usability

### How to Run

```bash
# Install dependencies (if not already done)
pip install -r requirements.txt

# Run the GUI app
python weather_gui.py
```

### Requirements

- Python 3.6+
- requests
- tkinter (usually included with Python)

### Usage

1. Launch the GUI app with `python weather_gui.py`
2. Enter a city name in the input field
3. Click "Get Weather" button
4. View weather information with emoji icons

---

## 🛠️ Technologies Used

- **Python**: Core programming language
- **requests**: HTTP library for API calls
- **tkinter**: GUI framework for desktop application
- **wttr.in**: Weather API service (no API key required)
