# Task 6: Push your custom image to Docker Hub or another container registry.

After successfully building a Docker image, the next logical step in the Docker journey is to share your image with others or deploy it to a remote server. Docker Hub, a cloud-based registry service, provides a platform for sharing Docker images. In this article, we will guide you through the process of pushing your custom Docker image to Docker Hub.

---

### What is Docker Hub?

Docker Hub is a service provided by Docker for finding and sharing container images with your team and the Docker community. It allows you to push your images for either public or private use.

---

### Prerequisites

- **Docker ID**: Ensure you have a Docker ID and are signed in to Docker Hub. If not, create an account on **[Docker Hub](https://hub.docker.com/)**.
- **Docker Desktop**: Ensure Docker Desktop is running on your machine.

---

### Step-by-Step: Pushing Your Docker Image to Docker Hub

### **Step 1: Login to Docker Hub**

In your terminal or command prompt, log in to Docker Hub using the **`docker login`** command and enter your Docker ID and password when prompted.

```
docker login
```

### **Step 2: Tag Your Docker Image**

Before pushing the image to Docker Hub, tag it using the **`docker tag`** command. The tag should follow the format **`username/repository:tag`**.

```
docker tag my-simple-web-app:latest [YourDockerID]/my-simple-web-app:latest
```

### **Explanation:**

- **`my-simple-web-app:latest`**: The name and tag of your local image.
- **`[YourDockerID]/my-simple-web-app:latest`**: The name and tag you want to give to your image on Docker Hub.

### **Step 3: Push the Docker Image**

Use the **`docker push`** command to push your image to Docker Hub.

```
docker push [YourDockerID]/my-simple-web-app:latest
```

### **Step 4: Verify the Push to Docker Hub**

Navigate to your Docker Hub account on the web and verify that the image has been pushed successfully. You should see **`my-simple-web-app`** listed in your repositories.

---

### Sharing and Pulling the Docker Image

- **Sharing**: If your repository is public, anyone can pull and use your Docker image. If it's private, only you and your collaborators can pull and use it.
- **Pulling**: To pull the image from Docker Hub, use the **`docker pull`** command:
    
    ```
    docker pull [YourDockerID]/my-simple-web-app:latest
    ```
    

---

### Conclusion

Congratulations! You have successfully pushed your custom Docker image to Docker Hub, making it accessible for sharing and deployment. This practice is fundamental for distributing your applications and collaborating with others in the Docker ecosystem.

---

### Next Steps

- **Docker Compose**: Explore defining and running multi-container Docker applications.
- **Docker Networking**: Dive deeper into Docker networking capabilities.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Learn how to integrate Docker with CI/CD pipelines.

---

### Further Reading

- **[Docker Hub Documentation](https://docs.docker.com/docker-hub/)**
- **[Docker Push Documentation](https://docs.docker.com/engine/reference/commandline/push/)**
- **[Docker Tag Documentation](https://docs.docker.com/engine/reference/commandline/tag/)**