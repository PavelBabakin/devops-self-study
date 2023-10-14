# Task 5: Create a Git repository with Kubernetes manifests for a sample application.

In the GitOps workflow, having a version-controlled Git repository containing your Kubernetes manifests is a foundational practice. This repository serves as the source of truth for your application configurations. In this article, we will guide you through creating a Git repository with Kubernetes manifests for a sample application, a crucial step in your GitOps journey.

### **Prerequisites**

Before you start, make sure you have the following prerequisites in place:

1. **Git**: You need Git installed on your local machine. You can download and install Git from the official website ([https://git-scm.com/](https://git-scm.com/)).
2. **A Code Editor**: You will need a code editor to create and edit Kubernetes manifest files. You can choose any code editor you prefer, such as Visual Studio Code, Sublime Text, or Atom.
3. **A Git Repository**: You can use a popular Git repository hosting service like GitHub, GitLab, or Bitbucket. In this article, we'll use GitHub for demonstration purposes.

### **Creating a Git Repository**

Follow these steps to create a Git repository for your sample application:

**Step 1: Sign In to GitHub**

1. Open a web browser and navigate to GitHub ([https://github.com/](https://github.com/)).
2. Sign in to your GitHub account. If you don't have an account, you can create one for free.

**Step 2: Create a New Repository**

1. Click the "+" sign in the upper right corner of the GitHub homepage and select "New repository."
2. Fill in the repository name, description, and other optional settings. Choose whether the repository should be public or private. In this example, let's name the repository "sample-app-k8s" and make it public.
3. Click the "Create repository" button.

**Step 3: Clone the Repository**

After creating the repository, you'll see instructions for initializing it with a README or pushing an existing repository. You will use the "push an existing repository from the command line" instructions. Follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to store your Kubernetes manifest files for the sample application.
3. Initialize a new Git repository in this directory:

```bash
git init
```

1. Create a sample Kubernetes manifest for your application using a code editor. You can start with a simple example like a Deployment or a ConfigMap. Save it with an appropriate file extension, e.g., **`.yaml`** or **`.json`**.
2. Add the manifest file to the Git repository and commit your changes:

```bash
git add .
git commit -m "Initial commit"
```

1. Now, copy the "push an existing repository from the command line" instructions from GitHub and paste them into your terminal. It will look something like this:

```bash
git remote add origin <repository-url>
git branch -M main
git push -u origin main
```

1. Replace **`<repository-url>`** with the actual URL of your GitHub repository.

**Step 4: Verify the Repository**

Refresh the GitHub repository page, and you should see the Kubernetes manifest file you pushed. Your Git repository is now set up with the initial Kubernetes manifest for your sample application.

### **Conclusion**

Creating a Git repository with Kubernetes manifests is a pivotal step in the GitOps workflow. This repository will be the source of truth for your application configurations, enabling you to manage your applications declaratively and version-controlled.

In the upcoming articles, we will explore how to deploy your sample application using ArgoCD in a GitOps manner. Stay tuned for hands-on experiences and best practices for your journey to becoming a DevOps engineer.