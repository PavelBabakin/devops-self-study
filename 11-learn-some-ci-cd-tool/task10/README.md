# Task 10: Create a basic GitHub Actions workflow to build and test a project on push or pull request.

GitHub Actions allows you to automate various tasks, including building and testing your projects. In this task, we'll create a basic GitHub Actions workflow to build and test a project automatically whenever code is pushed or a pull request is opened.

### **Prerequisites**

Before you start, ensure you have a GitHub repository for your project and some familiarity with the build and test process for your project.

### **Creating a GitHub Actions Workflow**

To create a basic GitHub Actions workflow, follow these steps:

### Step 1: Access the "Actions" Tab

1. Open your web browser and navigate to your GitHub repository.
2. Click on the "Actions" tab, which is located near the top of the repository page.

### Step 2: Create a New Workflow

In the "Actions" tab, you can create a new workflow:

1. Click on the "New workflow" button. This will open a code editor where you can define your workflow.

### Step 3: Define Your Workflow

In the code editor, you'll define your GitHub Actions workflow using YAML syntax. Here's an example of a basic workflow that builds and tests your project:

```yaml
name: Build and Test

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: '14'

    - name: Install dependencies
      run: npm install

    - name: Build
      run: npm run build

    - name: Test
      run: npm test
```

In this example:

- The workflow is triggered on pushes and pull requests to the "main" branch.
- It runs on the latest version of Ubuntu.
- The steps include checking out the code, setting up Node.js, installing project dependencies, building the project, and running tests.

### Step 4: Save and Commit

After defining your workflow, click on the "Start commit" button to save your workflow file. You'll need to commit this file to your repository.

### Step 5: Monitor Your Workflow

Once you've committed the workflow file, GitHub Actions will automatically detect and execute it whenever there are pushes or pull requests to the "main" branch. You can monitor the workflow's progress and results in the "Actions" tab of your repository.

### **Conclusion**

Creating a basic GitHub Actions workflow is a powerful way to automate your project's build and test processes. With the defined workflow, your project will automatically be built and tested on every push or pull request, helping you catch issues early in the development process.