# Task 8: Use GitLab Runners to execute your pipeline jobs.

GitLab Runners are agents that execute the jobs defined in your **`.gitlab-ci.yml`** file. In this task, we'll set up and use GitLab Runners to execute the pipeline jobs for your project.

### **Prerequisites**

Before you begin, ensure you have a project set up on GitLab, as discussed in the previous tasks. You should also have a basic **`.gitlab-ci.yml`** file defining your CI/CD pipeline.

### **Setting Up GitLab Runners**

GitLab provides various types of runners, including shared runners hosted by GitLab and your own custom runners. Here's how to set up runners for your project:

### Step 1: Access Your Project Settings

1. Log in to your GitLab account.
2. Navigate to your project.

### Step 2: Navigate to CI/CD Settings

1. In your project, click on "Settings" in the left-hand menu.
2. Scroll down and find the "CI/CD" section.

### Step 3: Register a Runner

In the "Runners" section, you can register a runner to execute your project's CI/CD jobs.

1. Click on the "Expand" button to view runner registration details.
2. You will see a registration token. This token is required to register a runner for your project. Keep it confidential.

### Step 4: Install and Register GitLab Runner

The steps for installing and registering a GitLab Runner depend on your operating system. Here are the general steps for a Linux-based runner:

1. Install GitLab Runner on your server using the package manager relevant to your Linux distribution. For example, on Ubuntu, you can use the following commands:
    
    ```bash
    sudo apt-get update
    sudo apt-get install gitlab-runner
    ```
    
2. Register the runner using the registration token from GitLab. Replace **`YOUR_REGISTRATION_TOKEN`** with the actual token from your project's settings:
    
    ```bash
    sudo gitlab-runner register
    ```
    
    - Enter the GitLab Runner URL, typically **`https://gitlab.com/`** for GitLab.com or your instance's URL.
    - Provide the token you received from your project settings.
    - Choose a runner description (e.g., "My Runner").
    - Choose tags if necessary.
    - Choose the executor type (e.g., **`shell`**, **`docker`**, or **`docker+machine`**).
    - Configure any executor-specific options if applicable.
3. Once registered, the runner will be available to execute jobs for your project.

### Step 5: Use GitLab Runner in Your Pipeline

In your **`.gitlab-ci.yml`** file, you can specify the runner to use by defining tags for your jobs. For example, to use a runner with the tag "my-runner," you can modify your job definitions as follows:

```yaml
build:
  stage: build
  tags:
    - my-runner
  script:
    - echo "Building the project..."
```

### **Monitoring and Troubleshooting**

You can monitor the status and details of your pipeline runs, including the runner used, in the "Pipelines" section of your GitLab project. If any issues arise, you can check the runner's logs for troubleshooting.

### **Conclusion**

Setting up and using GitLab Runners is a crucial step in enabling GitLab CI/CD for your project. These runners are responsible for executing the jobs defined in your **`.gitlab-ci.yml`** file, ensuring your CI/CD pipeline is carried out efficiently and reliably.