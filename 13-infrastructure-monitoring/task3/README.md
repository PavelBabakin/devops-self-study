# Task 3: Set up target scraping in Prometheus to collect metrics from a sample application or service.

In our ongoing exploration of Prometheus, we have already installed the monitoring tool and become familiar with its web user interface. In Task 3, we will delve into the practical side of Prometheus by setting up target scraping. This essential step allows Prometheus to collect metrics from various services and applications, aiding in the effective monitoring and analysis of your infrastructure.

### **Prerequisites:**

Before we proceed, ensure that you have the following prerequisites in place:

1. A running Prometheus instance (installed as per the instructions in Task 1).
2. A sample application or service from which you want to collect metrics. For this article, we'll use a simple web application.

### **Setting up Target Scraping:**

Follow these steps to set up target scraping in Prometheus:

1. **Identify Your Target:**
    
    Begin by identifying the application or service from which you want to collect metrics. For our example, let's assume you have a web application running on a server at **`http://your-app-url:port`**.
    
2. **Edit the Prometheus Configuration:**
    
    Open your Prometheus configuration file (usually named **`prometheus.yml`**) in a text editor. This file is where you define your target scraping configurations.
    
    Add a new job under **`scrape_configs`** to specify the target. Here's an example:
    
    ```yaml
    scrape_configs:
      - job_name: 'prometheus'
        static_configs:
          - targets: ['localhost:9090']
        # Add your application's job configuration
      - job_name: 'sample-app'
        static_configs:
          - targets: ['your-app-url:port']
    ```
    
    In this configuration, we've added a new job named **`'sample-app'`**. Replace **`'your-app-url:port'`** with the actual URL and port of your application.
    
3. **Restart Prometheus:**
    
    After making changes to the configuration file, save it and restart the Prometheus service. The command to restart Prometheus may vary depending on your operating system and how it's managed. On Linux, you can typically use a command like:
    
    ```bash
    systemctl restart prometheus
    ```
    
4. **Verify Scraping:**
    
    Once Prometheus has restarted, navigate to the Prometheus web UI and go to the "Targets" page (under "Status"). You should see your new target listed, along with its health and last scrape time. Prometheus will now collect metrics from your sample application.
    
5. **Write PromQL Queries:**
    
    With metrics being collected, you can now write PromQL queries in the Expression Browser or Console of the Prometheus web UI to analyze and visualize the data. For example, you can query metrics related to your application's response time, error rates, or any other relevant performance indicators.
    

Conclusion:

Setting up target scraping in Prometheus is a fundamental step in infrastructure monitoring. In this article, we walked through the process of configuring Prometheus to collect metrics from a sample application or service. With metrics flowing into Prometheus, you can now analyze and gain insights into the performance and reliability of your infrastructure.

In the upcoming tasks, we'll explore more advanced features of Prometheus, including writing complex PromQL queries, setting up alerting rules, and integrating Prometheus with Alertmanager to effectively manage and route alerts. Stay tuned for our next article as we continue our journey into infrastructure monitoring with Prometheus.