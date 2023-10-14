# Task 8: Make changes to the application's manifests in the Git repository and observe how ArgoCD automatically synchronizes the changes.

In the GitOps workflow, one of the key advantages is the ability to make changes to your application's configuration in a controlled and declarative manner. In this article, we will guide you through the process of making changes to your application's manifests in the Git repository and observing how ArgoCD automatically synchronizes those changes to ensure the cluster's state matches the updated desired state.

### **Prerequisites**

Before we proceed, ensure you have the following prerequisites in place:

1. **ArgoCD Installed**: You should have ArgoCD correctly installed on your Kubernetes cluster.
2. **Git Repository**: You should have a Git repository containing the Kubernetes manifests for your application. If you haven't created one, refer to the previous articles for guidance.
3. **Access to Git Repository**: Make sure you have write access to the Git repository, as you will be making changes to it.

### **Making Changes to Application Manifests**

Follow these steps to make changes to your application's manifests in the Git repository:

**Step 1: Clone the Git Repository**

1. Open your terminal or command prompt.
2. Clone the Git repository containing your application's manifests to your local machine. Replace **`<repository-url>`** with the actual URL of your Git repository.

```bash
git clone <repository-url>
```

1. Navigate to the directory where your application manifests are located.

**Step 2: Make Changes**

1. Use a code editor to open and edit one or more of your application's manifest files. You can make various changes, such as updating image versions, modifying configuration settings, or changing resource definitions.
2. Save your changes.

**Step 3: Commit and Push Changes**

1. In your terminal, commit the changes you made to your Git repository:

```bash
git add .
git commit -m "Updated application configuration"
```

1. Push the changes to your remote repository:

```bash
git push origin main
```

Replace **`main`** with the branch name in your repository if it's different.

**Step 4: Observe Automatic Synchronization with ArgoCD**

Now that you've pushed changes to your Git repository, let's observe how ArgoCD automatically synchronizes those changes:

1. Open the ArgoCD dashboard in your web browser.
2. In the "Applications" tab, find your application and click on it to view its details.
3. In the application details page, you'll see information about the application's synchronization status.
4. ArgoCD will detect the changes you pushed to the Git repository and automatically initiate the synchronization process.
5. You can monitor the synchronization progress by refreshing the page. ArgoCD will apply the changes to your application, ensuring that the cluster's state matches the updated desired state.

**Step 5: Verification**

1. After synchronization is complete, use **`kubectl`** to verify that your application has been updated on the Kubernetes cluster. Check the status of the application's resources, pods, or services as needed.
2. Access your application to ensure it is running as expected and that your changes have been applied successfully.

### **Conclusion**

In a GitOps workflow with ArgoCD, making changes to your application's manifests and observing automatic synchronization is a seamless process. This approach ensures that the cluster's state remains aligned with the desired state defined in your Git repository, even when changes are introduced.

In the upcoming articles, we will explore more advanced GitOps features and best practices for managing your applications effectively. Stay tuned for further insights into the world of DevOps and GitOps.