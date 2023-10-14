# Task 11: Understand persistent storage in Kubernetes and set up Persistent Volumes (PV) and Persistent Volume Claims (PVC).

In Kubernetes, applications often require persistent storage to maintain data across pod restarts or reschedules. To address this need, Kubernetes provides the concepts of Persistent Volumes (PV) and Persistent Volume Claims (PVC). In this task, we'll explore persistent storage in Kubernetes and the steps to set up PVs and PVCs.

## **Understanding Persistent Storage in Kubernetes:**

- **Containers and Storage:** In a containerized environment, data stored within a container is ephemeral, meaning it's lost when the pod is destroyed. For stateful applications, you need persistent storage to maintain data integrity.
- **Persistent Volumes (PV):** PVs are volumes that exist within a cluster and provide an abstraction for the underlying storage. PVs can be pre-provisioned or dynamically created by a storage class.
- **Persistent Volume Claims (PVC):** PVCs are requests made by pods for a specific amount and access mode of storage. They act as a claim to a PV.

## **Setting Up Persistent Volumes (PV) and Persistent Volume Claims (PVC):**

**1. Define a Persistent Volume (PV):**

To create a PV, you typically need to define a YAML file, e.g., **`my-pv.yaml`**, and specify the storage capacity, access modes, and the actual storage details. Here's an example:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  hostPath:
    path: /data/my-pv
```

- **Capacity:** Specify the storage capacity for the PV.
- **Access Modes:** Define the access mode for the PV. Common modes are **`ReadWriteOnce`**, **`ReadOnlyMany`**, and **`ReadWriteMany`**.
- **Storage Details:** The **`hostPath`** in this example uses a directory on the host for storage. In production, you would use cloud storage solutions or networked storage systems.
1. Apply the PV configuration:

```bash
kubectl apply -f my-pv.yaml
```

**2. Create a Persistent Volume Claim (PVC):**

PVCs are used by pods to request storage. You can create a PVC YAML file, e.g., **`my-pvc.yaml`**, and specify the storage capacity and access mode:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
```

1. Apply the PVC configuration:

```bash
kubectl apply -f my-pvc.yaml
```

**3. Mount the PVC in a Pod:**

To use the PVC in a pod, you can define a volume and mount it in the pod's spec. Here's an example:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-container
    image: nginx
    volumeMounts:
    - name: my-storage
      mountPath: /data
  volumes:
  - name: my-storage
    persistentVolumeClaim:
      claimName: my-pvc
```

This pod uses the PVC **`my-pvc`** and mounts it to the **`/data`** path.

1. Deploy the pod:

```bash
kubectl apply -f my-pod.yaml
```

With this setup, the pod can access and use the persistent storage provided by the PVC.

**Benefits of Using PVs and PVCs:**

- **Data Persistence:** PVs and PVCs ensure data persistence for stateful applications, databases, and other storage-dependent workloads.
- **Abstraction:** PVs abstract the underlying storage infrastructure, making it easier to manage and maintain storage.
- **Dynamic Provisioning:** Storage classes can be used to dynamically provision PVs, simplifying the setup process.

As you continue working with Kubernetes, understanding and using PVs and PVCs will be essential for running stateful applications and managing persistent storage efficiently.