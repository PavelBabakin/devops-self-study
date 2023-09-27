# Task 9: Use the net/http package to make an API call to a free weather service and fetch the current weather for a given city.

## **Fetching Weather Data with Go**

In today's interconnected world, APIs play a pivotal role in data exchange and integration across platforms. Whether you're building a weather application, a stock market tracker, or a news aggregator, APIs are the backbone that powers these applications. In this tutorial, we'll explore how to use Go (or Golang) to fetch weather data from an API.

### **Why Go for API Interactions?**

Go's standard library offers robust support for HTTP clients and servers. Its simplicity, combined with its efficient concurrency model, makes it an excellent choice for building applications that interact with APIs.

### **Building a Weather Fetcher in Go**

1. **Setting Up the API**:
    
    We'll be using the OpenWeatherMap API for this tutorial. You'll need to sign up and get an API key to authenticate your requests.
    
2. **Structuring the Data**:
    
    Go's static typing requires us to define a structure that matches the JSON response from the API. For this tutorial, we're only interested in the city's name and its current temperature.
    
    ```go
    type WeatherResponse struct {
        Main struct {
            Temp float64 `json:"temp"`
        } `json:"main"`
        Name string `json:"name"`
    }
    ```
    
3. **Making the API Call**:
    
    Go's **`net/http`** package provides the **`Get`** function, which we can use to make a GET request to the API.
    
    ```go
    apiUrl := fmt.Sprintf("http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric", city, apiKey)
    resp, err := http.Get(apiUrl)
    ```
    
4. **Parsing the Response**:
    
    Once we get the response, we read the body and unmarshal the JSON data into our **`WeatherResponse`** struct.
    
    ```go
    body, _ := ioutil.ReadAll(resp.Body)
    var weather WeatherResponse
    json.Unmarshal(body, &weather)
    ```
    
5. **Displaying the Data**:
    
    Finally, we print out the city's name and its current temperature.
    
    ```go
    fmt.Printf("The current temperature in %s is %f°C\n", weather.Name, weather.Main.Temp)
    ```
    
6. **Running the Utility**:
    
    After writing the utility, you can execute it using the **`go run`** command. This will display the current temperature for the specified city.
    
    ```bash
    go run weather.go
    ```
    

### **Conclusion**

With Go's comprehensive standard library, fetching data from an API becomes a straightforward task. This exercise not only showcases Go's capabilities in making HTTP requests and parsing JSON data but also demonstrates its potential as a go-to language for building diverse applications. As you continue your journey with Go, you'll discover its vast potential in various domains, from API interactions to web applications and beyond.