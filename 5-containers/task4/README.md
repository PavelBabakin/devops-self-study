# Task 4: Write a basic Dockerfile to create a custom image for a simple web application.

Diving deeper into the Docker universe, we now explore the creation of custom Docker images using a **`Dockerfile`**. A Docker image serves as a blueprint for Docker containers and is created from a set of instructions written in a **`Dockerfile`**. In this article, we will guide you through crafting a basic **`Dockerfile`** to create a custom image for a simple web application.

---

### What is a Dockerfile?

A **`Dockerfile`** is a text document that contains all the commands a user could call on the command line to assemble an image. Using **`docker build`**, users can create an automated build that executes several command-line instructions in succession.

---

### Basic Components of a Dockerfile

- **FROM**: Specifies the base image to be used.
- **RUN**: Executes commands in a new layer on top of the current image.
- **COPY**: Copies files from the source on the host into the container’s own filesystem at the set destination.
- **CMD**: Provides defaults for an executing container.

---

### Step-by-Step: Creating a Dockerfile for a Simple Web Application

### **Step 1: Choose a Base Image**

We'll use a lightweight Node.js image as our base image to build a simple Node.js web application.

```
FROM node:14-alpine
```

### **Step 2: Set the Working Directory**

Define the working directory inside the Docker image. This directory will hold the application code.

```
WORKDIR /app
```

### **Step 3: Copy Application Code**

Copy the local code directory (**`.`**) into the image (**`/app`**).

```
COPY . .
```

### **Step 4: Install Dependencies**

Install the Node.js dependencies for the application using the **`npm install`** command.

```
RUN npm install
```

### **Step 5: Expose the Application Port**

Expose the port on which the application will run. For instance, if your app runs on port **`3000`**, you should expose it as follows:

```
EXPOSE 3000
```

### **Step 6: Define the Startup Command**

Specify the command to run the application using **`CMD`**.

```
CMD ["npm", "start"]
```

### **Final Dockerfile:**

Combining all the steps, your **`Dockerfile`** should look like this:

```
FROM node:14-alpine

WORKDIR /app

COPY . .

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]
```

---

### Building the Docker Image

Once the **`Dockerfile`** is ready, use the **`docker build`** command to create the Docker image.

```
docker build -t my-simple-web-app:latest .
```

Here, **`-t`** allows you to tag the image with a name, and **`.`** indicates that the build context is the current directory.

---

### Running the Docker Container

To run a container from your new image, use the **`docker run`** command.

```
docker run -p 3000:3000 my-simple-web-app:latest
```

Here, **`-p`** maps the host port to the container port.

---

### Conclusion

Congratulations! You've successfully crafted a basic **`Dockerfile`**, built a custom Docker image, and run a container for a simple web application. This foundational knowledge will pave the way for creating more complex, production-ready Docker images in the future.

---

### Next Steps

- **Optimizing Docker Images**: Learn strategies to minimize image size and enhance security.
- **Docker Compose**: Explore defining and running multi-container Docker applications.
- **Docker Networking**: Understand how to facilitate communication between Docker containers.