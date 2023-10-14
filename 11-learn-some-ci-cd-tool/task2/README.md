# Task 2: Set up a basic freestyle project in Jenkins to pull from a Git repository and run a build.

Jenkins is a powerful automation server that can help you set up Continuous Integration (CI) for your projects. In this task, we will create a basic freestyle project in Jenkins to pull code from a Git repository and run a build whenever changes are detected.

### **Prerequisites**

Before you start, ensure you have Jenkins installed and running on your server or local machine, as we discussed in Task 1. You should also have a Git repository with a project you want to build.

### **Creating a Freestyle Project**

Follow these steps to create a basic freestyle project in Jenkins:

### Step 1: Log In to Jenkins

1. Open your web browser and navigate to the URL where Jenkins is running (e.g., **`http://localhost:8080/`**).
2. Log in using your administrator credentials.

### Step 2: Create a New Item

1. Click on "New Item" on the Jenkins dashboard.
2. Enter a name for your project, e.g., "My Freestyle Project."
3. Choose the "Freestyle project" option and click "OK."

### Step 3: Configure the Project

You'll be taken to the project configuration page. Here are some key configurations you can set:

- **General**: You can specify a project description and configure build triggers.
- **Source Code Management**: Choose Git and provide the URL of your Git repository. You can also specify the branch to build.
- **Build Triggers**: You can configure when to build your project. For example, you can set it to build whenever there are changes in the Git repository.
- **Build Environment**: You can define environment variables or other build-related settings.
- **Build**: This is where you specify the build steps. You can use shell commands or scripts to build your project.

### Step 4: Set Up the Build Step

In the "Build" section, you'll define the steps to build your project. For example, if you're building a Node.js application, you might use the following shell commands:

```bash
npm install         # Install project dependencies
npm run build       # Build the project
npm test            # Run tests
```

### Step 5: Save and Build

After configuring your project, click the "Save" button.

Now, you can manually trigger a build by clicking "Build Now" on the project page. Or, if you configured build triggers, Jenkins will automatically start a build whenever there are changes in the Git repository.

### **Viewing Build Results**

You can view the build results on the project page. Jenkins will display whether the build was successful or not. You can also check the console output to see the details of the build process.

### **Conclusion**

In this task, you've successfully set up a basic freestyle project in Jenkins to pull code from a Git repository and run a build. This is the fundamental step in implementing Continuous Integration (CI) for your projects. Jenkins makes it easy to automate your build process, ensuring that your code is continuously tested and built as changes are made.