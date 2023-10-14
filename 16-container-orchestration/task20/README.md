# Task 20: Dive into custom resource definitions (CRDs) and create custom controllers.

Custom Resource Definitions (CRDs) and custom controllers in Kubernetes provide a powerful mechanism for extending and customizing the platform to meet your specific application and business requirements. In this task, we'll dive into CRDs and learn how to create custom controllers to manage these custom resources.

## **What are Custom Resource Definitions (CRDs)?**

Custom Resource Definitions (CRDs) allow you to extend the Kubernetes API by defining your custom resources. These resources can represent application-specific objects, settings, or configurations. They are defined using CustomResourceDefinitions and stored in etcd, the Kubernetes datastore, just like native resources.

## **Creating and Managing Custom Resources:**

Here's how to create and manage custom resources using CRDs:

1. **Define a CRD:**
    
    Create a YAML file that defines your custom resource and its schema. The CRD specifies the resource's name, fields, validation rules, and other metadata.
    
    Example CRD YAML (**`my-crd.yaml`**):
    
    ```yaml
    apiVersion: apiextensions.k8s.io/v1
    kind: CustomResourceDefinition
    metadata:
      name: myresources.example.com
    spec:
      group: example.com
      names:
        kind: MyResource
        plural: myresources
        singular: myresource
      scope: Namespaced
      versions:
        - name: v1
          served: true
          storage: true
      subresources:
        status: {}
    ```
    
2. **Apply the CRD:**
    
    Apply the CRD configuration to your Kubernetes cluster using **`kubectl apply`**.
    
    ```bash
    kubectl apply -f my-crd.yaml
    ```
    
3. **Create Custom Resources:**
    
    With the CRD in place, you can create custom resources based on the defined schema.
    
    Example Custom Resource (**`myresource-instance.yaml`**):
    
    ```yaml
    apiVersion: example.com/v1
    kind: MyResource
    metadata:
      name: myresource-instance
    spec:
      key: value
    ```
    
    Apply the custom resource to the cluster:
    
    ```bash
    kubectl apply -f myresource-instance.yaml
    ```
    
4. **Create a Custom Controller:**
    
    To manage your custom resources, you need to create a custom controller. A controller watches for changes to your custom resources and takes action accordingly.
    
    Example custom controller code (simplified):
    
    ```go
    package main
    
    import (
        "k8s.io/client-go/kubernetes"
        "k8s.io/client-go/tools/cache"
        "k8s.io/client-go/util/wait"
        "k8s.io/apimachinery/pkg/util/runtime"
    )
    
    func main() {
        // Create a clientset to interact with the Kubernetes API.
    
        // Create a SharedInformer to watch for custom resource changes.
    
        // Define handlers for added, modified, and deleted custom resources.
    
        // Start the informer and controller loop.
    }
    ```
    
    This code is a simplified example. In practice, custom controllers can be more complex and can react to various events, manage resources, and perform reconciliations.
    
5. **Deploy the Custom Controller:**
    
    Package your custom controller as a container and deploy it in your Kubernetes cluster.
    
6. **Custom Resource Management:**
    
    Your custom controller watches for changes to custom resources and takes actions based on your application's specific logic. For example, it can create other resources, perform updates, or initiate other workflows.
    

## **Benefits of Custom Resource Definitions (CRDs) and Custom Controllers:**

- **Customization:** CRDs allow you to create resources that align with your application's unique requirements and configurations.
- **Scalability:** Custom controllers can manage resources at scale, automating tasks and reducing operational overhead.
- **Extensibility:** Kubernetes can be extended to manage more than just built-in resources, making it a versatile platform for various use cases.
- **Consistency:** Custom resources can be defined and managed in a way that is consistent with native Kubernetes resources.

Custom Resource Definitions (CRDs) and custom controllers empower you to tailor Kubernetes to your specific application and operational needs. They are essential for managing custom resources efficiently, automating tasks, and enabling unique capabilities within your Kubernetes cluster.