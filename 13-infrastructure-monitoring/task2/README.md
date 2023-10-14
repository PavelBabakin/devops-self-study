# Task 2: Explore the Prometheus web UI and understand its basic components.

Prometheus is a powerful open-source monitoring tool used to collect and query metrics from various services and applications. In the previous article, we installed Prometheus, and now it's time to get acquainted with its web user interface. This article will guide you through Task 2, where we explore the Prometheus web UI and understand its basic components.

### **Accessing the Prometheus Web UI**

Before we dive into the components of the Prometheus web UI, make sure your Prometheus server is up and running. You can access the web UI by opening a web browser and navigating to **`http://localhost:9090`** (or the address you specified in your configuration file).

### **Basic Components of the Prometheus Web UI**

1. **Expression Browser:**
    
    The Expression Browser is where you can write PromQL (Prometheus Query Language) expressions to query and visualize metrics. It allows you to select specific metrics, apply functions, and create graphs for visualization.
    
    - To test a basic query, type **`up`** in the "Expression" field and click "Execute." This query fetches the "up" metric, which indicates whether a target is up or not.
2. **Graph:**
    
    The Graph tab allows you to create graphs to visualize metric data. After executing a query, you can click on the "Graph" tab to view a time series graph. You can adjust the time range for the graph using the time range selector in the top right corner.
    
3. **Console:**
    
    The Console tab is where you can execute PromQL queries and view the results in tabular form. This is useful for more complex queries or for exploring metric data in detail.
    
4. **Status and Configuration:**
    
    Clicking on the "Status" menu at the top right of the UI provides information about the Prometheus server's status, including its version, configuration, and various targets it's scraping. This can be useful for monitoring the health of your Prometheus server.
    
5. **Targets:**
    
    Under the "Status" menu, you can navigate to "Targets" to see the list of targets configured in your Prometheus instance. This section displays information about each target, including its health and last scrape time.
    
6. **Alerts:**
    
    Prometheus allows you to set up alerting rules to monitor specific conditions and generate alerts. The "Alerts" tab displays a list of active alerts and their current status.
    
7. **Configurations:**
    
    The "Configurations" tab provides an overview of your Prometheus configuration file. This is helpful for troubleshooting and verifying that your scraping configurations are correctly set up.
    

Conclusion:

Exploring the Prometheus web UI is the first step in harnessing the power of Prometheus for infrastructure monitoring. In this article, we covered the essential components of the Prometheus web UI, including the Expression Browser, Graph, Console, Status, Targets, Alerts, and Configurations. Understanding these components is crucial for effectively querying and visualizing metrics, setting up alerts, and ensuring the reliability and performance of your systems.

In the upcoming articles, we will continue our journey with Prometheus, delving into more advanced features and tasks. Stay tuned for Task 3, where we will set up target scraping in Prometheus to collect metrics from a sample application or service.