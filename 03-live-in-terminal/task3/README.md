# Task 3: Use top and htop to view running processes and system resources.

Hello, dear readers! As we continue our journey into the world of the terminal, today we'll be focusing on monitoring running processes and system resources. Specifically, we'll be discussing two powerful tools: **`top`** and **`htop`**. These utilities provide real-time insights into your system's performance, helping you keep tabs on what's happening under the hood. Let's dive in!

### 1. **`top` (Table of Processes)**

The **`top`** command provides a dynamic, real-time view of the processes running on your system. It displays information about the system's performance, including CPU usage, memory consumption, and much more.

**Usage**:

```bash
top
```

**Key Features**:

- **Processes List**: **`top`** displays a list of currently executing processes, sorted by default by the percentage of CPU usage.
- **System Summary**: At the top, you'll see a summary of system statistics, including uptime, number of tasks, CPU status, and memory usage.
- **Interactive Commands**: While **`top`** is running, you can use various keyboard shortcuts to interact with processes, change display settings, and more.

**Common Interactive Commands**:

- **`q`**: Quit **`top`**.
- **`k`**: Kill a process. You'll be prompted to enter the process ID.
- **`u`**: Display processes for a specific user.
- **`r`**: Renice (change priority of) a process.

### 2. **`htop` (Enhanced Table of Processes)**

While **`top`** is incredibly useful, **`htop`** takes process monitoring to the next level with a more user-friendly interface, color-coded metrics, and easier navigation.

**Usage**:

```bash
htop
```

**Key Features**:

- **Color-Coded Metrics**: **`htop`** uses colors to provide a clearer view of resource usage, making it easier to interpret at a glance.
- **Easier Navigation**: Navigate through the list of processes using arrow keys, and easily sort processes by different criteria.
- **Process Tree View**: Display processes in a tree format, showing parent-child relationships.
- **Customizable**: You can customize the display, choose which columns to show, and more.

**Common Interactive Commands**:

- **`F9`**: Open the "Kill" menu to terminate a process.
- **`kicker`**: Open the search bar to find a process.
- **`F3`**: Search for the next instance of a previously searched term.
- **`F2`**: Access the setup menu for customization.

**Installation** (if not pre-installed):
Depending on your system, you might need to install **`htop`** using your package manager:

- For Debian/Ubuntu: **`sudo apt install htop`**
- For CentOS/RedHat: **`sudo yum install htop`**
- For macOS: **`brew install htop`**

### **Conclusion**

Both **`top`** and **`htop`** are invaluable tools for anyone looking to monitor and manage system processes. While **`top`** offers a straightforward and efficient way to view system metrics, **`htop`** provides a more enhanced and interactive experience. By familiarizing yourself with these tools, you'll be well-equipped to keep your system running smoothly. In our upcoming articles, we'll explore more advanced terminal utilities. Stay tuned!