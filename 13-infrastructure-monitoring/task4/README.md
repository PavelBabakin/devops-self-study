# Task 4: Write basic queries in PromQL to visualize metrics.

Prometheus is a versatile monitoring tool that allows you to collect and analyze metrics from various services and applications. To make the most of Prometheus, you need to understand how to query and visualize your metrics effectively. In Task 4, we will explore writing basic queries in PromQL (Prometheus Query Language) to help you gain insights into your data and create visualizations.

### **Prerequisites:**

Before we begin, ensure you have:

1. A running Prometheus instance with target scraping set up (as described in Task 3).
2. Basic knowledge of the metrics you're monitoring and the labels associated with them.

### **Writing Basic Queries in PromQL:**

PromQL is a powerful query language designed for working with time series data. Here are some basic queries to help you get started:

1. **Selecting a Metric:**
    
    To select a metric, you can simply specify its name. For example, to select the "http_requests_total" metric, use the following query:
    
    ```
    http_requests_total
    ```
    
    This query will return the time series data for the "http_requests_total" metric.
    
2. **Filtering by Labels:**
    
    Prometheus metrics often come with labels to distinguish between various instances or services. You can filter metrics based on labels using curly braces. For instance, to select the "http_requests_total" metric for a specific HTTP method (e.g., "GET"), use the following query:http_requests_total{method="GET"}
    
    ```
    
    ```
    
    This query filters the metric to only include data where the "method" label is equal to "GET."
    
3. **Aggregating Data:**
    
    You can aggregate data to gain insights into its overall behavior. For example, to calculate the total number of HTTP requests for each endpoint, you can use the **`sum`** function:
    
    ```
    sum(http_requests_total) by (endpoint)
    ```
    
    This query sums the "http_requests_total" metric for each distinct "endpoint."
    
4. **Time-Based Queries:**
    
    To focus on a specific time range, you can use time-based queries. For instance, to select data from the last hour, you can use the **`rate`** function:
    
    ```
    rate(http_requests_total[1h])
    ```
    
    This query calculates the rate of HTTP requests over the last hour.
    
5. **Creating Graphs:**
    
    After you've written a query, you can visualize the data by clicking the "Graph" tab in the Prometheus web UI. This will display a time series graph based on your query, allowing you to analyze trends and anomalies.
    

Conclusion:

Writing basic queries in PromQL is a crucial skill for effectively utilizing Prometheus. In this article, we covered the fundamentals of selecting metrics, filtering by labels, aggregating data, using time-based queries, and visualizing data in graphs. With these skills, you can gain valuable insights into the performance and reliability of your infrastructure.

As you become more familiar with PromQL, you can create more complex queries to extract specific information from your metrics and set up alerts to proactively address issues. In the next task, we will delve into setting up alerting rules in Prometheus to enhance your monitoring capabilities. Stay tuned for more on your infrastructure monitoring journey with Prometheus.