# Task 10: Write a Go program that uses goroutines to parallelize the fetching of multiple URLs and measure the response time for each.

## **Parallel URL Fetching with Go**

In the realm of modern web development, efficiency is paramount. Whether you're building a web scraper, a monitoring tool, or a performance tester, the ability to fetch multiple URLs concurrently can significantly speed up your operations. Go, with its built-in concurrency model, is perfectly suited for such tasks. In this tutorial, we'll explore how to use Go's goroutines to fetch multiple URLs in parallel and measure the response time for each.

### **Why Go for Parallel Operations?**

Go's concurrency model is built around goroutines and channels. A goroutine is a lightweight thread managed by the Go runtime, allowing you to run multiple threads in parallel without the overhead of traditional threading models. This makes Go an excellent choice for tasks that require parallel processing, like fetching multiple URLs.

### **Building a Parallel URL Fetcher in Go**

1. **Structuring the Data**:
    
    We'll start by defining a list of URLs that we want to fetch. For this tutorial, we'll use a few popular search engines as our targets.
    
    ```go
    urls := []string{
        "https://www.google.com",
        "https://www.bing.com",
        "https://www.yahoo.com",
    }
    ```
    
2. **Fetching the URLs**:
    
    We'll define a function, **`fetchURL`**, that takes a URL and fetches it, printing the time it took to get a response.
    
    ```go
    func fetchURL(url string, wg *sync.WaitGroup) {
        defer wg.Done()
    
        start := time.Now()
        _, err := http.Get(url)
        if err != nil {
            fmt.Println("Error:", err)
            return
        }
    
        elapsed := time.Since(start)
        fmt.Printf("URL: %s took %s\n", url, elapsed)
    }
    ```
    
3. **Parallelizing the Fetch**:
    
    Using Go's goroutines, we can fetch all the URLs in our list concurrently. We'll use a **`sync.WaitGroup`** to ensure our program waits for all the fetches to complete before exiting.
    
    ```go
    var wg sync.WaitGroup
    for _, url := range urls {
        wg.Add(1)
        go fetchURL(url, &wg)
    }
    wg.Wait()
    ```
    
4. **Running the Utility**:
    
    After writing the utility, you can execute it using the **`go run`** command. This will display the response time for each URL in the list.
    
    ```bash
    go run url_fetcher.go
    ```
    

### **Conclusion**

With just a few lines of Go code, we've built a powerful utility that can fetch multiple URLs in parallel and measure their response times. This exercise showcases Go's strength in parallel processing and its potential as a tool for building efficient and scalable applications. Whether you're building a web scraper, a monitoring tool, or just curious about Go's capabilities, this tutorial provides a practical introduction to Go's concurrency model.