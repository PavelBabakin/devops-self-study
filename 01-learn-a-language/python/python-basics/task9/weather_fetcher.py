import requests

def fetch_weather(city_name):
    # Define the API endpoint and parameters
    API_ENDPOINT = "http://api.openweathermap.org/data/2.5/weather"
    API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # Use "imperial" for Fahrenheit
    }

    # Make the API call
    response = requests.get(API_ENDPOINT, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        weather_data = data['weather'][0]
        print(f"Weather in {city_name}:")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Weather: {weather_data['description']}")
    else:
        print(f"Failed to fetch weather data for {city_name}. Status code: {response.status_code}")

def main():
    city_name = input("Enter the name of the city: ")
    fetch_weather(city_name)

if __name__ == "__main__":
    main()