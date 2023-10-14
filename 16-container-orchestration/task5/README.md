# Task 5: Deploy your first application on Kubernetes using kubectl.

Now that you have a Kubernetes cluster set up, it's time to deploy your first application. In this task, we'll use the **`kubectl`** command-line tool to create and manage Kubernetes resources. We'll deploy a simple "Hello World" web application as an example.

## **1. Create a Kubernetes Deployment:**

To deploy your application, you'll start by creating a Kubernetes Deployment. Deployments ensure that a specified number of pod replicas are running and manage their updates. You can define the desired state of your application in a YAML configuration file. Create a file named **`hello-world-deployment.yaml`** and add the following content:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
      - name: hello-world
        image: nginx:latest
        ports:
        - containerPort: 80
```

This YAML file defines a Deployment with three replicas running an Nginx web server.

## **2. Apply the Deployment:**

Use the **`kubectl apply`** command to create the Deployment:

```bash
kubectl apply -f hello-world-deployment.yaml
```

Kubernetes will create the specified number of pods running Nginx.

## **3. Check the Deployment:**

You can check the status of the Deployment with the following command:

```bash
kubectl get deployments
```

You should see your "hello-world-deployment" with three replicas.

## **4. Expose the Deployment:**

Now that your application is running, you can expose it to the external world using a Service. Create a file named **`hello-world-service.yaml`** and add the following content:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-world-service
spec:
  selector:
    app: hello-world
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
  type: LoadBalancer
```

This YAML file defines a Service of type LoadBalancer to expose your application.

## **5. Apply the Service:**

Apply the Service YAML file with the following command:

```bash
kubectl apply -f hello-world-service.yaml
```

Kubernetes will create a LoadBalancer Service, which will provide an external IP address to access your "Hello World" application.

## **6. Access the Application:**

Use the following command to retrieve the external IP address of the Service:

```bash
kubectl get svc hello-world-service
```

You can access your "Hello World" application by entering the provided external IP address in a web browser.

Congratulations! You've successfully deployed your first application on Kubernetes. This simple example demonstrates the fundamental steps of creating Deployments and Services. As you continue your journey into Kubernetes, you can explore more complex applications, use Helm for package management, and implement various Kubernetes features to manage and scale your services effectively.