from flask import Flask, jsonify, render_template_string
import psutil

app = Flask(__name__)

@app.route('/')
def system_info():
    # Fetch system information
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    
    # HTML template to display the information
    template = """
    <h1>System Information</h1>
    <ul>
        <li><strong>CPU Usage:</strong> {{ cpu_usage }}%</li>
        <li><strong>Memory Usage:</strong> {{ memory_info.percent }}% ({{ memory_info.used }} / {{ memory_info.total }})</li>
        <li><strong>Disk Usage:</strong> {{ disk_info.percent }}% ({{ disk_info.used }} / {{ disk_info.total }})</li>
    </ul>
    """

    return render_template_string(template, cpu_usage=cpu_usage, memory_info=memory_info, disk_info=disk_info)

@app.route('/api/system_info')
def api_system_info():
    # Fetch system information
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    
    # Create a dictionary with the system information
    data = {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_info.percent,
        "memory_used": memory_info.used,
        "memory_total": memory_info.total,
        "disk_usage": disk_info.percent,
        "disk_used": disk_info.used,
        "disk_total": disk_info.total
    }
    
    # Return the data as JSON
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)