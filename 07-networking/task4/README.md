# Task 4: Set up a basic web server using Apache or Nginx and serve a static webpage over HTTP.

In the digital realm, web servers play a pivotal role in hosting websites and web applications, making them accessible to users across the globe. Nginx, renowned for its high performance and low resource consumption, is a popular web server choice among DevOps professionals. In this guide, we will explore the steps to set up a basic web server using Nginx and serve a static webpage over HTTP.

**Prerequisites**

- A Linux machine (physical or virtual)
- Root or sudo access to the machine
- Basic understanding of Linux terminal commands

**Step 1: Installing Nginx**

1. **Update Your System**: Ensure your system package repositories are up to date.
    
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```
    
2. **Install Nginx**: Utilize the package manager to install Nginx.
    
    ```bash
    sudo apt install nginx
    ```
    
3. **Start and Enable Nginx**: Ensure Nginx starts at boot and is running.
    
    ```bash
    sudo systemctl start nginx
    sudo systemctl enable nginx
    ```
    

**Step 2: Configuring Nginx to Serve a Static Webpage**

1. **Create a Webpage**: Develop a simple HTML webpage to be served.
    
    ```bash
    echo "<!DOCTYPE html><html><head><title>My Nginx Static Webpage</title></head><body><h1>Welcome to My Nginx Server!</h1></body></html>" | sudo tee /var/www/html/index.html
    ```
    
2. **Configure Nginx**: Ensure Nginx is set to serve your webpage.
    - Open the default Nginx configuration file:
        
        ```bash
        sudo nano /etc/nginx/sites-available/default
        ```
        
    - Ensure the **`location`** block points to your HTML file:
        
        ```
        location / {
            root /var/www/html;
            index index.html;
        }
        ```
        
    - Save and exit the text editor.
3. **Restart Nginx**: Apply the changes by restarting Nginx.
    
    ```bash
    sudo systemctl restart nginx
    ```
    

**Step 3: Accessing the Webpage**

- Open a web browser and navigate to **`http://[your-server-ip]`**. You should see the static webpage served by Nginx.

**Step 4: Basic Nginx Management**

- **Stop Nginx**:
    
    ```bash
    sudo systemctl stop nginx
    ```
    
- **Start Nginx**:
    
    ```bash
    sudo systemctl start nginx
    ```
    
- **Reload Nginx Configuration**:
    
    ```bash
    sudo systemctl reload nginx
    ```
    
- **Disable Nginx from Starting at Boot**:
    
    ```bash
    sudo systemctl disable nginx
    ```
    

**Conclusion**

Congratulations! You have successfully set up a basic web server using Nginx and served a static webpage over HTTP. Understanding web server setup and management is fundamental in DevOps, ensuring that web applications and sites are reliably accessible to users.

In the forthcoming articles, we will delve deeper into understanding the HTTP request/response cycle and securing web traffic with HTTPS. Stay tuned to continue building your DevOps skillset!