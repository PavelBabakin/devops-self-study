# Task 11: Write a script to monitor CPU and memory usage, alerting (printing a message) when usage exceeds 80%.

## **Monitoring System Resources with Python: A DevOps Perspective**

In the dynamic world of DevOps, staying ahead of potential system bottlenecks is crucial. Whether it's an application consuming excessive CPU or a memory leak slowly crippling a server, early detection can be the difference between smooth operations and a full-blown crisis. In this article, we'll explore how to use Python to monitor CPU and memory usage on macOS, providing real-time alerts when usage exceeds a certain threshold.

### **The Importance of Monitoring**

System monitoring serves as the eyes and ears of a DevOps professional. It provides:

- **Early Detection**: Identify potential issues before they escalate.
- **Performance Insights**: Understand how applications and services impact system resources.
- **Optimization Opportunities**: Make informed decisions on resource allocation, scaling, and system upgrades.

### **Python: A DevOps Ally**

Python, with its extensive libraries and ease of use, is a valuable tool in the DevOps arsenal. For our monitoring task, we'll leverage the **`psutil`** library, which offers an interface to retrieve system utilization details.

### **Crafting the Resource Monitor**

Our Python script, **`resource_monitor.py`**, is designed to:

1. **Fetch CPU Usage**: Determine the percentage of CPU being used.
2. **Fetch Memory Usage**: Understand how much of the system's RAM is in use.
3. **Alert on High Usage**: Print a warning message if either CPU or memory usage exceeds 80%.

Executing the script provides real-time insights into system resource consumption, allowing for timely interventions.

### **Applications in DevOps**

While our script offers a snapshot of CPU and memory usage, its real power lies in potential integrations:

- **Logging and Dashboards**: Store resource usage data over time and visualize trends.
- **Notification Systems**: Integrate with messaging platforms or alerting systems to notify teams of high resource usage.
- **Automated Interventions**: Trigger scripts or tools to address high resource usage, such as restarting services or scaling resources.

### **Conclusion**

Monitoring is a cornerstone of effective DevOps practices. By keeping a close eye on system resources, professionals can ensure optimal performance, timely interventions, and proactive management. Python, with its versatility and extensive library support, offers a robust solution for crafting custom monitoring tools tailored to specific needs. As you continue your DevOps journey, consider the myriad ways in which monitoring can enhance your operations and the role Python can play in it.

Stay vigilant and keep coding!