# Task 6: Deploy the application using ArgoCD by connecting it to the Git repository.

ArgoCD simplifies the deployment of applications on Kubernetes clusters through GitOps practices. In this article, we'll guide you through deploying an application using ArgoCD by connecting it to a Git repository. This process allows you to maintain infrastructure and application configurations in a version-controlled, declarative way.

### **Prerequisites**

Before starting, ensure you have the following prerequisites in place:

1. **ArgoCD Installed**: Make sure ArgoCD is correctly installed on your Kubernetes cluster as explained in a previous article.
2. **Git Repository**: You should have a Git repository with Kubernetes manifests for your application. If you haven't created one, refer to the previous article for guidance.

### **Deploying an Application with ArgoCD**

Follow these steps to deploy your application using ArgoCD:

**Step 1: Access the ArgoCD Dashboard**

1. Open a web browser and navigate to the URL where you exposed the ArgoCD web UI. By default, it should be **`http://localhost:8080`** if you followed the installation steps.
2. Log in to the ArgoCD dashboard with your credentials.

**Step 2: Add a New Application**

1. In the ArgoCD dashboard, click on the "Applications" tab.
2. Click the "New App" button to create a new application.
3. Fill in the application details:
    - **Application Name**: Choose a name for your application.
    - **Project**: You can select an existing project or create a new one.
    - **Sync Policy**: Set the sync policy for your application, such as manual or automatic synchronization.
    - **Source**: In the "Repository URL" field, enter the URL of your Git repository containing the application manifests.
    - **Path**: If your manifests are in a subdirectory of the repository, specify the path to that directory.
    - **Destination**: Define the target Kubernetes namespace for your application.
    - **Cluster**: Select the target cluster where you want to deploy the application.
4. Click the "Create" button to add the application.

**Step 3: Sync the Application**

1. After adding the application, you will be redirected to the application details page.
2. To deploy the application, click the "Sync" button.
3. ArgoCD will initiate a synchronization process, deploying the application based on the manifests in the linked Git repository.

**Step 4: Monitor Synchronization**

1. You can monitor the synchronization progress by going to the "Applications" tab and selecting your application. Here, you can see details on the synchronization status.
2. Once the synchronization is complete, your application is deployed on the Kubernetes cluster.

**Step 5: Verification**

To ensure your application is successfully deployed:

1. Use **`kubectl`** to check the status of your application resources. For example:

```bash
kubectl get pods -n <namespace>
```

1. Verify that your application is running correctly by accessing it through its defined services or endpoints.

### **Conclusion**

Deploying an application using ArgoCD in a GitOps workflow allows you to maintain a declarative, version-controlled approach to managing your Kubernetes applications. By connecting ArgoCD to your Git repository, you can effortlessly deploy and synchronize your applications while enjoying the benefits of consistency and traceability.

In the next articles, we will explore more advanced deployment strategies and configurations with ArgoCD. Stay tuned for further insights into the world of GitOps and DevOps.