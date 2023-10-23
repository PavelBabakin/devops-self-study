# Task 5: Build the Docker image using docker build and run a container from it.

In the previous article, we crafted a basic **`Dockerfile`** for a simple web application. Now, let’s take the next step in our Docker journey by building the Docker image and running a container from it. This article will guide you through the process of building a Docker image using the **`docker build`** command and subsequently running a container from the built image.

---

### Building a Docker Image

### **Step 1: Navigate to Dockerfile Directory**

Ensure your terminal or command prompt is pointed to the directory containing your **`Dockerfile`**.

```
cd [path_to_your_Dockerfile]
```

### **Step 2: Build the Docker Image**

Use the **`docker build`** command to build your Docker image. Tag the image using **`-t`** followed by the name and optionally a tag in the ‘name:tag’ format.

```
docker build -t my-simple-web-app:latest .
```

### **Explanation:**

- **`docker build`**: The Docker command for building images from a Dockerfile.
- **`t my-simple-web-app:latest`**: Tags the image with the name **`my-simple-web-app`** and the tag **`latest`**.
- **`.`**: Specifies the build context as the current directory.

### **Step 3: Verify the Image Build**

Use the **`docker images`** command to list all available images and verify that your image has been built successfully.

```
docker images
```

---

### Running a Docker Container

### **Step 4: Run the Docker Container**

Use the **`docker run`** command to start a new container from your image.

```
docker run -p 3000:3000 my-simple-web-app:latest
```

### **Explanation:**

- **`docker run`**: The Docker command to run a container.
- **`p 3000:3000`**: Maps port 3000 of your machine to port 3000 on the container, allowing you to access the application.
- **`my-simple-web-app:latest`**: Specifies the image to use when creating the container.

### **Step 5: Access the Web Application**

Open a web browser and navigate to **`http://localhost:3000`** to access your simple web application running inside the Docker container.

### **Step 6: Stop the Docker Container**

When you wish to stop the Docker container, identify the container ID using the **`docker ps`** command.

```
docker ps
```

Then, stop the container using the **`docker stop`** command followed by the container ID.

```
docker stop [CONTAINER_ID]
```

---

### Conclusion

Congratulations! You have successfully built a Docker image and run a container from it, bringing your simple web application to life. This process of building images and running containers is fundamental to deploying applications with Docker, and mastering it will pave the way for managing more complex, multi-container applications in the future.

---

### Next Steps

- **Docker Compose**: Explore how to use Docker Compose to manage multi-container applications.
- **Docker Networking**: Understand how to enable communication between Docker containers.
- **Docker Volumes**: Learn how to manage data within and between Docker containers.

---

### Further Reading

- **[Docker Build Documentation](https://docs.docker.com/engine/reference/commandline/build/)**
- **[Docker Run Documentation](https://docs.docker.com/engine/reference/run/)**
- **[Docker Hub](https://hub.docker.com/)**