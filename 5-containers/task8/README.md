# Task 8: Write a docker-compose.yml file to set up a web application and its database.

In the previous article, we explored Docker Compose and its significance in orchestrating multi-container applications. Now, let's delve into practical application by crafting a **`docker-compose.yml`** file to set up a simple web application and its database, ensuring they interact seamlessly.

---

### Understanding **`docker-compose.yml`**

A **`docker-compose.yml`** file is a YAML file that defines how Docker containers should behave in a production environment. It allows you to define:

- **Services**: The applications or microservices, each running in its own container.
- **Networks**: Networks to facilitate communication between containers.
- **Volumes**: Volumes or file paths for persistent data storage.

---

### Example: Setting Up a Web Application and Database

Let’s create a **`docker-compose.yml`** file to set up a simple Node.js web application and a MongoDB database.

### **Step 1: Define the Version**

Specify the Docker Compose file format version.

```yaml
version: '3'
```

### **Step 2: Define Services**

Define the services (containers) that should be created.

```yaml
services:
```

### Web Service

Define the web service, specify the Docker image to use, and map the ports.

```yaml
 	 web:
    image: node:14-alpine
    ports:
      - "3000:3000"
    depends_on:
      - db
```

### Database Service

Define the database service and specify the Docker image to use.

```yaml
  db:
    image: mongo:4.4-bionic
```

### **Step 3: Define Networks (if needed)**

Define the networks to be used by the services.

```yaml
networks:
  app-network:
    driver: bridge
```

### **Step 4: Define Volumes (if needed)**

Define the volumes for persistent data storage.

```yaml
volumes:
  db-data:
```

### **Step 5: Configure Services**

Configure the services to use the defined networks and volumes.

```yaml
services:
  web:
    ...
    networks:
      - app-network
  db:
    ...
    volumes:
      - db-data:/data/db
    networks:
      - app-network
```

### **Final `docker-compose.yml`**

Combining all steps, your **`docker-compose.yml`** should look like this:

```yaml
version: '3'

services:
  web:
    image: node:14-alpine
    ports:
      - "3000:3000"
    depends_on:
      - db
    networks:
      - app-network

  db:
    image: mongo:4.4-bionic
    volumes:
      - db-data:/data/db
    networks:
      - app-network

networks:
  app-network:
    driver: bridge

volumes:
  db-data:

```

---

### Running Docker Compose

To run Docker Compose and bring up your services:

```
docker-compose up
```

To stop your services:

```
docker-compose down
```

---

### Conclusion

With the crafted **`docker-compose.yml`**, you've orchestrated a simple setup involving a web application and a database. Docker Compose simplifies the management and deployment of multi-container applications, ensuring they interact seamlessly and are easy to scale and maintain.

---

### Next Steps

- **Docker Compose Commands**: Explore various Docker Compose commands for managing your application.
- **Environment Variables**: Learn how to use environment variables in Docker Compose.
- **Service Scaling**: Explore how to scale services using Docker Compose.

---

### Further Reading

- **[Docker Compose File Reference](https://docs.docker.com/compose/compose-file/)**
- **[Docker Compose CLI Reference](https://docs.docker.com/compose/reference/overview/)**
- **[Docker Documentation](https://docs.docker.com/)**