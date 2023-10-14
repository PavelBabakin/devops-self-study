# Task 11: Deploy a sample application in the Istio service mesh.

In Task 11 of the DevOps Engineer's Service Mesh learning program, we'll explore the practical side of Istio by deploying a sample application into the Istio service mesh. Istio is a powerful service mesh tool that enhances the communication, security, and observability of microservices. Deploying a sample application will allow you to see Istio in action and understand its impact on your microservices architecture.

**Prerequisites**

Before we proceed, ensure you have successfully installed Istio on your Kubernetes cluster as outlined in the previous task. Additionally, make sure you have a basic understanding of Kubernetes and have **`kubectl`** configured to interact with your cluster.

**Step 1: Deploy a Sample Application**

For this guide, we'll deploy a basic "Hello, World!" application called "httpbin." This application will act as a sample service within the Istio service mesh.

1. Create a Kubernetes namespace for your application (if you haven't already):

```bash
kubectl create namespace sample-app
```

1. Deploy the httpbin sample application:

```bash
kubectl apply -n sample-app -f https://raw.githubusercontent.com/istio/istio/release-1.11/samples/httpbin/httpbin.yaml
```

This YAML file defines the httpbin application and deploys it into your Kubernetes cluster.

1. Verify that the application pods are running:

```bash
kubectl get pods -n sample-app
```

You should see the httpbin pods in the "Running" state.

**Step 2: Expose the Sample Application**

By default, the httpbin application is not exposed to external traffic. To access it, you can create a Kubernetes service and Istio VirtualService to define routing rules:

1. Create a Kubernetes service to expose the httpbin application:

```
kubectl apply -n sample-app -f https://raw.githubusercontent.com/istio/istio/release-1.11/samples/httpbin/httpbin-service.yaml
```

1. Create an Istio VirtualService to define routing rules for the application:

```bash
kubectl apply -n sample-app -f https://raw.githubusercontent.com/istio/istio/release-1.11/samples/httpbin/httpbin-gateway.yaml
```

This VirtualService configures Istio to route external traffic to the httpbin service.

**Step 3: Access the Sample Application**

The httpbin application can now be accessed using Istio's Ingress Gateway. The exact address depends on your Kubernetes cluster configuration.

1. Determine the external IP and port of your Istio Ingress Gateway. The command may vary depending on your Kubernetes environment. For example, in a Minikube environment, you can use:

```bash
minikube ip
```

1. Use the Ingress Gateway IP and port to access the httpbin application. For example:

```bash
curl http://<gateway-ip>:<gateway-port>/status/418
```

You should receive a "418 I'm a teapot" response, confirming that the application is accessible via Istio.

**Conclusion**

By deploying the httpbin sample application into the Istio service mesh, you have taken the first steps in experiencing Istio's capabilities in action. You can now see how Istio handles traffic and applies features like routing, security, and observability to your microservices. In the upcoming tasks, we'll explore more advanced topics and features of Istio to further enhance your service mesh management skills. Stay tuned for more practical guides on your DevOps journey.