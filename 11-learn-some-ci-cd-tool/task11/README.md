# Task 11: Use matrix builds to run tests on multiple versions of a language or platform.

Matrix builds in GitHub Actions allow you to run tests on multiple versions of a language or platform simultaneously. This can be especially useful for ensuring your project is compatible with different runtime environments. In this task, we'll explore how to use matrix builds in a GitHub Actions workflow.

### **Prerequisites**

Before you begin, make sure you have a GitHub repository for your project and a basic understanding of the different versions or environments you want to test against.

### **Creating a Matrix Build**

Follow these steps to create a matrix build in your GitHub Actions workflow:

### Step 1: Access the "Actions" Tab

1. Open your web browser and navigate to your GitHub repository.
2. Click on the "Actions" tab, which is located near the top of the repository page.

### Step 2: Edit Your Workflow

In the "Actions" tab, locate the workflow you want to modify and click on its name to edit it.

### Step 3: Define the Matrix

In your workflow's YAML file, you can define a matrix of versions or platforms you want to test. Here's an example:

```yaml
name: Matrix Build

on:
  push:
    branches:
      - main

jobs:
  test:
    strategy:
      matrix:
        node: [12, 14, 16]
        os: [ubuntu-latest, windows-latest, macos-latest]

    runs-on: ${{ matrix.os }}

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Node.js
      uses: actions/setup-node@v2
      with:
        node-version: ${{ matrix.node }}

    - name: Install dependencies
      run: npm install

    - name: Test
      run: npm test
```

In this example:

- The workflow is triggered on pushes to the "main" branch.
- The **`strategy`** section defines a matrix with different versions of Node.js (**`node`**) and operating systems (**`os`**).
- The workflow runs on the specified operating system from the matrix.
- The steps are similar to the basic workflow, but they take the Node.js version from the matrix.

### Step 4: Save and Commit

After defining your matrix build, click on the "Start commit" button to save your workflow file. You'll need to commit this file to your repository.

### Step 5: Monitor Your Workflow

Once you've committed the workflow file, GitHub Actions will automatically detect and execute it whenever there are pushes to the "main" branch. The workflow will run tests for all combinations of Node.js versions and operating systems specified in the matrix.

### **Conclusion**

Using matrix builds in GitHub Actions is a powerful way to ensure your project is compatible with multiple versions of a language or platform. By defining a matrix in your workflow, you can simultaneously test your project under different runtime environments, making it more robust and reliable.