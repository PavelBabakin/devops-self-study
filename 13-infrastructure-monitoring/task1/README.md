# Task 1: Install Prometheus on a server or local machine.

In the world of DevOps and infrastructure monitoring, Prometheus stands out as one of the most popular open-source solutions. It empowers organizations to collect and analyze metrics from various services and applications, aiding in maintaining system reliability and performance. In this article, we'll walk through the first task in our infrastructure monitoring journey - installing Prometheus on a server or a local machine.

Task 1: Install Prometheus

Prometheus is known for its flexibility and adaptability. You can install it on a dedicated server or even on your local machine for experimentation. Let's get started.

### **Prerequisites:**

Before we begin, make sure you have the following prerequisites in place:

1. A server or a local machine running a compatible operating system (Linux, Windows, macOS).
2. A user account with administrative privileges (if required).

### **Installation Steps:**

1. **Download Prometheus:**
    
    Start by visiting the Prometheus download page on the official website ([https://prometheus.io/download/](https://prometheus.io/download/)). Choose the appropriate version for your operating system. For this article, we'll install Prometheus on a Linux server.
    
    ```bash
    wget https://github.com/prometheus/prometheus/releases/download/v2.30.3/prometheus-2.30.3.linux-amd64.tar.gz
    ```
    
2. **Extract the Archive:**
    
    Use the **`tar`** command to extract the downloaded archive:
    
    ```bash
    tar -xvzf prometheus-2.30.3.linux-amd64.tar.gz
    ```
    
3. **Navigate to the Prometheus Directory:**
    
    Change your working directory to the Prometheus installation directory:
    
    ```bash
    cd prometheus-2.30.3.linux-amd64/
    ```
    
4. **Create a Configuration File:**
    
    Prometheus requires a configuration file to define the targets it will scrape for metrics. You can create a simple configuration file (prometheus.yml) in your preferred text editor. Here's an example:
    
    ```yaml
    global:
      scrape_interval: 15s
    
    scrape_configs:
      - job_name: 'prometheus'
        static_configs:
          - targets: ['localhost:9090']
      # Add additional job configurations as needed
    ```
    
    Save this file in the Prometheus directory.
    
5. **Start Prometheus:**
    
    To start Prometheus, use the following command:
    
    ```bash
    ./prometheus --config.file=prometheus.yml
    ```
    
    Prometheus will start and begin scraping metrics from the targets defined in the configuration file.
    
6. **Access the Prometheus Web UI:**
    
    Open your web browser and navigate to **`http://localhost:9090`** (or the address you specified in your configuration file). You should now see the Prometheus web user interface, which allows you to query and visualize metrics.
    

Conclusion:

Congratulations! You've successfully installed Prometheus on your server or local machine. In this article, we covered the initial installation steps, from downloading Prometheus to configuring it and starting the Prometheus server. In the upcoming articles, we will delve deeper into Prometheus by exploring its web UI, setting up target scraping, writing queries in PromQL, and much more.

Stay tuned for the next task in our infrastructure monitoring series, where we will dive into exploring the Prometheus web UI and understanding its basic components.