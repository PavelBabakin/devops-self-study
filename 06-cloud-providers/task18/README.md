# Task 18: Deploy a Docker container using Azure Kubernetes Service (AKS).

Azure Kubernetes Service (AKS) simplifies deploying, managing, and scaling containerized applications using Kubernetes. With AKS, you can leverage the power of Kubernetes without having to manage the underlying infrastructure. In this guide, we will explore how to deploy a Docker container using AKS, providing a hands-on approach to container orchestration in Azure.

**Step 1: Creating an AKS Cluster**

- **Navigate to AKS**: From the Azure Portal, click on “Create a resource”, and select “Kubernetes Service”.
- **Basics**: Configure the basic settings, including subscription, resource group, region, and Kubernetes version.
- **Scale**: Define the node size and node count.
- **Authentication**: Configure the service principal and role-based access control.
- **Review + Create**: Review your configurations and click “Create” to deploy the AKS cluster.

**Step 2: Configuring kubectl**

- **Install kubectl**: Ensure that **`kubectl`**, the Kubernetes command-line tool, is installed on your local machine.
- **Connect kubectl to AKS**: Use the “Connect” button in the AKS overview in the Azure Portal to get the command to configure **`kubectl`** to use the AKS cluster.

**Step 3: Deploying a Docker Container**

- **Docker Image**: Ensure your Docker image is available in a container registry (e.g., Docker Hub, Azure Container Registry).
- **Create a Deployment YAML**: Define a Kubernetes deployment YAML file that specifies the Docker image, desired replicas, and other configurations.
    
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: myapp-deployment
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: myapp
      template:
        metadata:
          labels:
            app: myapp
        spec:
          containers:
          - name: myapp-container
            image: [Your Docker Image]
    ```
    
- **Deploy**: Use **`kubectl`** to deploy the Docker container.
    
    ```bash
    kubectl apply -f [Your Deployment YAML File]
    ```
    

**Step 4: Exposing the Application**

- **Create a Service YAML**: Define a Kubernetes service YAML file to expose the deployment.
    
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: myapp-service
    spec:
      selector:
        app: myapp
      ports:
        - protocol: TCP
          port: 80
          targetPort: [Your Application Port]
      type: LoadBalancer
    ```
    
- **Expose**: Use **`kubectl`** to expose the deployment.
    
    ```bash
    kubectl apply -f [Your Service YAML File]
    ```
    
- **Access**: Obtain the external IP of the service and access the application.
    
    ```bash
    kubectl get service myapp-service
    ```
    

**Conclusion**

Deploying a Docker container using Azure Kubernetes Service (AKS) provides a scalable and manageable approach to run containerized applications in the cloud. From creating the AKS cluster to exposing your application, AKS handles the underlying Kubernetes complexity, allowing you to focus on your applications. As we continue to explore Azure, our subsequent guides will delve into more advanced container orchestration practices and scenarios with AKS. Stay tuned for more hands-on tasks and insights!