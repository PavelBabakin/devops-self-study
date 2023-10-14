# Task 13: Set up a project in CircleCI and write a .circleci/config.yml file for a basic build and test pipeline.

In this task, we'll set up a project in CircleCI and write a **`.circleci/config.yml`** file to define a basic build and test pipeline for your project.

### **Prerequisites**

Before you begin, make sure you have signed up for CircleCI and have access to a project in your version control account. You should also have a basic understanding of the build and test process for your project.

### **Setting Up a Project in CircleCI**

Follow these steps to set up a project in CircleCI:

### Step 1: Access the CircleCI Dashboard

1. Log in to your CircleCI account.
2. After logging in, you'll be directed to the CircleCI dashboard.

### Step 2: Add a Project

1. Click on the "Add Projects" button to add your project to CircleCI.
2. Select your project from the list of repositories associated with your version control account.
3. Follow the instructions to configure your project settings, including the source code location and the build environment.

### Step 3: Write a **`.circleci/config.yml`** File

The **`.circleci/config.yml`** file defines the build and test pipeline for your project. You can create this file in your project's repository and configure the steps to build, test, and deploy your code.

Here's an example of a basic **`.circleci/config.yml`** file for a Node.js project:

```yaml
version: 2.1
executors:
  node-executor:
    docker:
      - image: circleci/node:14

jobs:
  build:
    executor: node-executor
    steps:
      - checkout

      - run:
          name: Install Dependencies
          command: npm install

      - run:
          name: Build
          command: npm run build

      - run:
          name: Test
          command: npm test

workflows:
  version: 2
  build-deploy:
    jobs:
      - build
```

In this example:

- We define a Node.js executor that uses a Node.js 14 Docker image.
- We define a job named "build" that checks out the code, installs dependencies, builds the project, and runs tests.
- We use a workflow that includes the "build" job.

### Step 4: Commit and Push

After writing the **`.circleci/config.yml`** file, commit and push it to your project's repository. This will trigger CircleCI to use the defined pipeline to build and test your code.

### Step 5: Monitor Your Pipeline

You can monitor the progress and results of your pipeline on the CircleCI dashboard. If there are any issues or failures, CircleCI will provide detailed logs to help with troubleshooting.

### **Conclusion**

Setting up a project in CircleCI and writing a **`.circleci/config.yml`** file is the key to automating your build and test pipeline. With CircleCI, you can ensure that your code is consistently built, tested, and deployed as defined in your configuration.