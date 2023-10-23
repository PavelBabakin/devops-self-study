# Task 16: Explore Azure Cosmos DB by creating a database and a container.

Azure Cosmos DB is a multi-model, globally distributed database service for large-scale applications with a wide-reaching geographic distribution. It provides turnkey global distribution, elastic scaling of throughput and storage, and low-latency data access. In this guide, we will explore how to create a database and a container in Azure Cosmos DB, providing a hands-on approach to working with NoSQL databases in Azure.

**Step 1: Creating an Azure Cosmos DB Account**

- **Navigate to Cosmos DB**: From the Azure Portal, click on “Create a resource”, and select “Azure Cosmos DB”.
- **Basics**: Configure the basic settings, including subscription, resource group, account name, and API (e.g., Core (SQL) for document databases).
- **Review + Create**: Review your configurations and click “Create” to deploy the Azure Cosmos DB account.

**Step 2: Creating a Database**

- **Navigate to the Cosmos DB Account**: Once created, go to the Cosmos DB account you just created.
- **Add Database**: Click on “Add Database” in the Overview section.
- **Configure**: Enter a unique database id and configure throughput settings.
- **Create**: Click “OK” to create the database.

**Step 3: Creating a Container**

- **Navigate to the Database**: Click on the database you created.
- **Add Container**: Click on “Add Container”.
- **Configure**: Enter a unique container id, partition key, and configure throughput settings.
- **Create**: Click “OK” to create the container.

**Step 4: Exploring Data**

- **Items**: Navigate to “Items” within your container to view and query data.
- **Upload Data**: Optionally, you can upload JSON items or manually add data using the “New Item” button.
- **Query Data**: Use the SQL API to run queries against your data in the “Items” section.

**Step 5: Integrating with Applications**

- **Connection String**: Retrieve the connection string from the “Keys” section under “Settings”.
- **SDK**: Use one of the Azure Cosmos DB SDKs (e.g., .NET, Java, Python) to integrate with your applications.
- **Query**: Use the SQL API or respective API for your database model to interact with the data in your application code.

**Conclusion**

Exploring Azure Cosmos DB by creating a database and a container provides a foundational understanding of working with NoSQL data in Azure. From creating the database to querying data, Azure Cosmos DB offers a robust and scalable platform for developing applications with a globally distributed, multi-model database. As we continue to explore Azure, our subsequent guides will delve into more advanced functionalities and development practices with Azure Cosmos DB. Stay tuned for more hands-on tasks and insights!