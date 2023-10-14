# Task 5: Integrate Jenkins with a version control system (e.g., GitHub) to trigger builds on commits.

Integrating Jenkins with a version control system (VCS) like GitHub is a key part of a Continuous Integration (CI) setup. This integration allows Jenkins to automatically trigger builds and tests whenever code changes are pushed to the VCS repository. In this task, we'll set up the integration between Jenkins and GitHub.

### **Prerequisites**

Before you begin, make sure you have Jenkins installed and configured, as discussed in the previous tasks. You should also have a GitHub repository with the project you want to build and test.

### **Integrating Jenkins with GitHub**

Here's how to integrate Jenkins with GitHub:

### Step 1: Install GitHub Plugin

1. Log in to your Jenkins web interface.
2. Click on "Manage Jenkins" in the left-hand menu.
3. Select "Manage Plugins."
4. In the "Available" tab, search for "GitHub Integration" or "GitHub." Check the checkbox next to the plugin and click "Install without restart."

### Step 2: Configure GitHub Webhook

To allow GitHub to notify Jenkins of changes, you need to set up a webhook:

1. In your GitHub repository, go to "Settings."
2. Click on "Webhooks."
3. Click "Add webhook."
4. In the "Payload URL" field, enter your Jenkins URL followed by **`/github-webhook/`**. For example, **`http://your-jenkins-server/github-webhook/`**.
5. Choose "application/json" as the content type.
6. In "Which events would you like to trigger this webhook?" select "Just the push event."
7. Click "Add webhook" to save.

### Step 3: Configure Jenkins for GitHub

1. In your Jenkins web interface, click on "Manage Jenkins" and select "Configure System."
2. Scroll down to the "GitHub" section and click "Add GitHub Server."
3. Provide a name for your GitHub server.
4. Under "Credentials," click "Add" to add your GitHub credentials. This can be a username and password or a token with the necessary permissions.
5. In the "API URL" field, enter the GitHub API URL, which is typically **`https://api.github.com`**.
6. Click "Test Connection" to ensure that Jenkins can connect to your GitHub server.
7. Save your configuration.

### Step 4: Create or Update Jenkins Projects

Now, in your Jenkins projects, update the Source Code Management section to use the GitHub integration. If you haven't created a project yet, follow the steps in Task 4 to create a Jenkinsfile and configure your freestyle project.

1. In your Jenkins project, go to the configuration page.
2. Under "Source Code Management," select "Git."
3. In the "Repository URL," enter your GitHub repository URL.
4. Under "Credentials," select the GitHub credentials you added in the previous step.
5. Save your configuration.

### Step 5: Test the Integration

Now, whenever changes are pushed to your GitHub repository, Jenkins will automatically detect them and trigger a build based on your Jenkinsfile.

### **Conclusion**

Integrating Jenkins with a version control system like GitHub is a vital part of setting up a CI/CD pipeline. This integration ensures that your code is built and tested automatically whenever changes are pushed, helping to catch and resolve issues early in the development process.