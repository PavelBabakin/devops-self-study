# Task 3: Familiarize yourself with basic Docker commands like docker ps, docker images, and docker logs.

Embarking further into our journey with Docker, it's crucial to acquaint ourselves with its command-line interface (CLI). Docker CLI allows us to interact with Docker, manage containers, images, networks, and volumes. In this article, we'll explore some fundamental Docker commands that will enhance your understanding and management of containers: **`docker ps`**, **`docker images`**, and **`docker logs`**.

---

### Docker CLI: A Brief Overview

Docker CLI is a command-line interface that allows users to interact with Docker daemon, enabling them to build, run, and manage Docker containers. The Docker CLI sends commands to the Docker API, which in turn communicates with the Docker daemon to execute the requested tasks.

---

### Command 1: **`docker ps`**

The **`docker ps`** command is used to list all the running Docker containers.

### **Usage:**

```
docker ps [OPTIONS]
```

### **Example:**

```
docker ps
```

### **Explanation:**

- **CONTAINER ID**: A unique identifier for each container.
- **IMAGE**: The image used to create the container.
- **COMMAND**: The command that is being run inside the container.
- **CREATED**: The duration since the container has been created.
- **STATUS**: The current status of the container.
- **PORTS**: The port(s) that are mapped to the container.
- **NAMES**: The name assigned to the container.

### **Options:**

- **`a, --all`**: Show all containers (default shows just running).
- **`q, --quiet`**: Display only the numeric IDs.
- **`s, --size`**: Show the total file sizes.

---

### Command 2: **`docker images`**

The **`docker images`** command lists all the Docker images available locally on your machine.

### **Usage:**

```
docker images [OPTIONS] [REPOSITORY[:TAG]]
```

### **Example:**

```
docker images
```

### **Explanation:**

- **REPOSITORY**: The repository to which the image belongs.
- **TAG**: The tag assigned to the image.
- **IMAGE ID**: A unique identifier for the image.
- **CREATED**: The duration since the image has been created.
- **SIZE**: The size of the image.

### **Options:**

- **`a, --all`**: Show all images (default hides intermediate images).
- **`q, --quiet`**: Only show numeric IDs.

---

### Command 3: **`docker logs`**

The **`docker logs`** command fetches the logs of a container, allowing you to view the output and errors from the processes running inside the container.

### **Usage:**

```
docker logs [OPTIONS] CONTAINER
```

### **Example:**

```
docker logs [CONTAINER_ID or CONTAINER_NAME]
```

### **Explanation:**

This command will display the log output of the specified container, which is particularly useful for debugging purposes.

### **Options:**

- **`-details`**: Show extra details provided to logs.
- **`f, --follow`**: Follow log output.
- **`-since`**: Show logs since timestamp (e.g., 2013-01-02T13:23:37) or relative (e.g., 42m for 42 minutes).
- **`-tail`**: Number of lines to show from the end of the logs.

---

### Conclusion

Understanding and utilizing Docker commands is fundamental to efficiently managing containers and images. The commands **`docker ps`**, **`docker images`**, and **`docker logs`** provide insights into the running containers, available images, and container log outputs, respectively. As you continue to explore Docker, these commands will prove to be invaluable in your container management and debugging efforts.

---

### Next Steps

- **Working with Docker Images**: Dive deeper into creating and managing Docker images.
- **Docker Compose**: Learn how to define and manage multi-container Docker applications.
- **Docker Networking**: Explore how to facilitate communication between Docker containers.

---

### Further Reading

- **[Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)**
- **[Docker Documentation](https://docs.docker.com/)**
- **[Docker Hub](https://hub.docker.com/)**