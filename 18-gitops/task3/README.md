# Task 3: Install ArgoCD on a Kubernetes cluster.

ArgoCD is a powerful tool that plays a central role in implementing GitOps practices. It allows you to deploy and manage applications on a Kubernetes cluster by syncing with Git repositories. In this article, we will walk you through the process of installing ArgoCD on a Kubernetes cluster, a crucial step in your GitOps journey.

### **Prerequisites**

Before we begin, ensure you have the following prerequisites in place:

1. **Kubernetes Cluster**: You should have a running Kubernetes cluster. If you don't have one already, you can set up a local cluster using Minikube or use a cloud-based solution like Google Kubernetes Engine (GKE), Amazon EKS, or Microsoft Azure AKS.
2. **kubectl**: You need the **`kubectl`** command-line tool installed and configured to interact with your Kubernetes cluster.
3. **Helm**: Helm is a package manager for Kubernetes, and you'll need it to install ArgoCD. Make sure you have Helm installed and configured on your local machine.

### **Installing ArgoCD**

Here are the steps to install ArgoCD:

**Step 1: Add ArgoCD Helm Repository**

ArgoCD can be installed using Helm charts. To get started, add the ArgoCD Helm repository to your Helm installation:

```bash
helm repo add argo https://argoproj.github.io/argo-helm
```

**Step 2: Create Namespace**

It's a good practice to create a dedicated namespace for ArgoCD:

```bash
kubectl create namespace argocd
```

**Step 3: Install ArgoCD using Helm**

Now, install ArgoCD into the **`argocd`** namespace:

```bash
helm install argocd argo/argo-cd --namespace argocd
```

**Step 4: Monitor Installation Progress**

Check the installation progress by running:

```bash
kubectl get pods -n argocd
```

Wait until all the pods are in the "Running" state. This might take a few moments.

**Step 5: Expose the ArgoCD Web UI**

ArgoCD has a web-based user interface that you can access. To expose it, create a port-forward to the ArgoCD server:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

You can now access the ArgoCD UI at [http://localhost:8080](http://localhost:8080/). The default username is **`admin`** and the password is the name of the server pod, which you can retrieve using:

```bash
kubectl get pods -n argocd -l "app.kubernetes.io/name=argocd-server" -o name | cut -d'/' -f 2
```

**Step 6: Login to ArgoCD UI**

Log in to the ArgoCD UI with the provided credentials (username: admin, password: retrieved from the previous step). You are now ready to start using ArgoCD to deploy applications using GitOps!

### **Conclusion**

Installing ArgoCD on a Kubernetes cluster is a fundamental step in your GitOps journey. It enables you to manage your applications using declarative Git repositories, providing you with greater control, consistency, and reproducibility in your deployments. In the next articles, we will explore how to deploy applications using ArgoCD and dive deeper into GitOps best practices. Stay tuned for more hands-on guidance on your path to becoming a DevOps engineer!