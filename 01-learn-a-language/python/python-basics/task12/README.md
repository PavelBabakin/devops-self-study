# Task 12: Create a Flask web application with a single route that displays system information.

## **Building a System Monitoring Web Application with Flask**

In the age of cloud computing and microservices, having a clear view of your system's health and performance is paramount. While there are many tools and platforms available for system monitoring, sometimes a custom solution is needed to cater to specific requirements. In this article, we'll explore how to use Flask, a lightweight web framework for Python, to create a simple web application that displays key system metrics.

### **Why Flask?**

Flask is a micro web framework for Python. Its simplicity and flexibility make it an excellent choice for building web applications quickly. Whether you're prototyping a new idea or building a production-ready application, Flask provides the tools you need without the bloat.

### **Crafting the System Monitoring Application**

Our Flask application will display three key metrics:

1. **CPU Usage**: The percentage of CPU being used.
2. **Memory Usage**: The percentage of RAM in use and the total RAM available.
3. **Disk Usage**: The percentage of disk space in use and the total disk space available.

To fetch these metrics, we'll use the **`psutil`** library, a cross-platform library for accessing system details.

### **Building the Application**

The core of our application is the **`system_info`** route. This route fetches the system metrics using **`psutil`** and then displays them using a simple HTML template. The use of **`render_template_string`** allows us to embed the HTML directly in our Python script for simplicity.

### **Running the Application**

Once the application is ready, running it is as simple as executing the Python script. The application will be accessible at **`http://127.0.0.1:5000/`**, displaying the system metrics in a user-friendly format.

### **Expanding the Application**

While our application provides basic system metrics, there's a lot of potential for expansion:

- **Additional Metrics**: Incorporate more system metrics like network usage, active processes, or system uptime.
- **Styling and Interactivity**: Use CSS frameworks like Bootstrap to enhance the look and feel. Add JavaScript for real-time updates or interactive charts.
- **Database Integration**: Store metrics over time and create historical charts or trend analyses.
- **Alerting**: Integrate with messaging platforms or email to send alerts based on certain conditions.

### **Conclusion**

System monitoring is a crucial aspect of DevOps and system administration. By building custom monitoring tools, professionals can tailor solutions to their specific needs, ensuring that they have the insights they need to maintain optimal system performance. Flask, with its simplicity and flexibility, provides an excellent platform for building these tools, allowing for rapid development and iteration.

Stay informed and keep building!