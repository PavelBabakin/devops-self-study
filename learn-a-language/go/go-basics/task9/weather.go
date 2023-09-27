package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

type WeatherResponse struct {
	Main struct {
		Temp float64 `json:"temp"`
	} `json:"main"`
	Name string `json:"name"`
}

func fetchWeather(city string) {
	apiKey := "YOUR_API_KEY" // Replace with your OpenWeatherMap API key
	apiUrl := fmt.Sprintf("http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric", city, apiKey)

	resp, err := http.Get(apiUrl)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer resp.Body.Close()

	body, _ := ioutil.ReadAll(resp.Body)

	var weather WeatherResponse
	json.Unmarshal(body, &weather)

	fmt.Printf("The current temperature in %s is %f°C\n", weather.Name, weather.Main.Temp)
}

func main() {
	city := "London" // Replace with your desired city
	fetchWeather(city)
}
