# Task 3: Install and set up JFrog Artifactory on a local machine or server.

In Task 3 of your DevOps journey, we'll take the practical leap into the world of binary repository management by installing and setting up JFrog Artifactory. Artifactory is a powerful and widely-used binary repository manager that plays a pivotal role in effective artifact management. By the end of this guide, you'll have Artifactory up and running on your local machine or server, ready to facilitate efficient storage, versioning, and management of binary artifacts.

**Prerequisites**

Before we dive into the installation, ensure that you have the following prerequisites in place:

1. **Operating System**: JFrog Artifactory is compatible with various operating systems, including Linux, Windows, and macOS. Choose the one that best fits your environment.
2. **Java**: Artifactory requires Java to run. Ensure that you have Java Development Kit (JDK) installed on your machine. You can download it from the official Oracle or OpenJDK websites.
3. **System Resources**: Check the system requirements for your chosen Artifactory version. Ensure that your machine or server has the necessary CPU, RAM, and disk space to support Artifactory.

Installation Steps

Let's get started with the installation and setup of JFrog Artifactory:

**Step 1: Download Artifactory**

Visit the [JFrog Artifactory download page](https://jfrog.com/open-source/#artifactory) to access the open-source version. Select your preferred package format (e.g., ZIP, Tar, or installer for your OS).

**Step 2: Extract or Install**

Depending on your chosen package format, you will either extract the files or run the installer. For Linux, use the terminal and extract the files with the following command:

```bash
tar -xvf artifactory-<version>.tar.gz
```

For Windows, run the installer executable.

**Step 3: Configuration**

Navigate to the Artifactory installation directory and locate the **`artifactory.system.properties`** file. You can configure various settings in this file, such as the port Artifactory runs on, database connections, and security options. Make any necessary adjustments based on your requirements.

**Step 4: Start Artifactory**

In your terminal or command prompt, navigate to the Artifactory installation directory and run the following command to start Artifactory:

For Linux:

```bash
./bin/artifactory.sh
```

For Windows:

```bash
bin\artifactory.bat
```

Artifactory will start, and you can access it through your web browser by entering **`http://localhost:8081/artifactory`**. If you configured a different port in Step 3, replace **`8081`** with the port you specified.

**Step 5: Initial Configuration**

Upon accessing Artifactory for the first time, you'll be prompted to complete the initial setup. This includes setting up your admin credentials and choosing a license (if applicable). Follow the on-screen instructions to complete this process.

**Step 6: Accessing Artifactory**

You can now log in with your admin credentials and begin using JFrog Artifactory to manage binary artifacts.

Conclusion

Congratulations! You've successfully installed and set up JFrog Artifactory on your local machine or server. You're now equipped with a powerful binary repository manager that will be integral in your DevOps journey. In the upcoming tasks, we'll explore how to create and manage repositories, deploy and retrieve artifacts, integrate Artifactory with build tools, and delve into advanced features. With Artifactory in your DevOps toolkit, you'll be well-prepared to efficiently manage your software artifacts and streamline your development and deployment processes. Stay tuned for more hands-on exercises and insights on your road to becoming a DevOps engineer.