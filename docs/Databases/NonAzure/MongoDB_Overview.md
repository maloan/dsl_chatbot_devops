## MongoDB Overview

### **What is MongoDB?**

MongoDB is a widely used document-oriented NoSQL database that provides flexibility and [Scalability](../../Containerization_and_Deployment/Scalability.md) for modern applications. It allows developers to store data in JSON-like format (BSON) which is schema-free, enabling the storage of complex, hierarchical data structures with ease. It is well-suited for managing large amounts of unstructured data.

For more information, visit the [official MongoDB documentation](https://www.mongodb.com/docs/manual/#what-is-mongodb).

---

### **Deployment Environments**

MongoDB can be deployed in a variety of ways depending on your needs:

- **[MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server)**: A fully managed cloud database service, providing ease of use, scalability, and automated backups.
- **[MongoDB Enterprise](https://www.mongodb.com/docs/manual/administration/install-enterprise/#std-label-install-mdb-enterprise)**: A subscription-based service for enterprises requiring advanced features such as enhanced security and support.
- **[MongoDB Community Edition](https://www.mongodb.com/docs/manual/administration/install-community/#std-label-install-mdb-community-edition)**: A free, open-source version ideal for developers or small businesses that need the core MongoDB features.

---

### **Securing MongoDB Deployments**

Security is a top priority for MongoDB, with MongoDB Atlas providing several robust features to secure your deployments:

- **Authentication and Authorization**: MongoDB supports LDAP, OAuth, and other authentication methods to ensure that only authorized users have access to data. You can configure roles and permissions to control access.
    - Learn more about [Authentication and Authorization in MongoDB](https://www.mongodb.com/docs/atlas/security/config-db-auth/).
- **Encryption**: All data is encrypted by default both at rest and in transit to ensure data privacy. MongoDB Atlas also offers Key Management Service (KMS) integration.
    - Learn more about [Encryption at Rest](https://www.mongodb.com/docs/atlas/security-kms-encryption/).
- **IP Access List**: Restrict access to your database by IP address, ensuring that only authorized machines can access your data.
    - See the [IP Access List documentation](https://www.mongodb.com/docs/atlas/security/ip-access-list/).
- **Cloud Provider Support**: MongoDB Atlas works with major cloud providers like AWS, Azure, and Google Cloud, offering flexibility and additional layers of security.

---

### **SQL Support in MongoDB**

While MongoDB is a NoSQL database, it supports SQL queries through the [MongoDB Connector for BI](https://www.mongodb.com/products/bi-connector). This allows users to run SQL queries against MongoDB data and integrate it with Business Intelligence (BI) tools.

- The [MongoDB Application Modernization Guide](https://www.mongodb.com/modernize?tck=docs_server) provides a comprehensive approach to migrating from traditional SQL databases to MongoDB.

---

### **MongoDB Pricing**

MongoDB offers several pricing options to meet the needs of developers and businesses of all sizes:

- **Serverless Instances**: Ideal for low-traffic applications with usage-based pricing. Costs start from $0.10 per million reads.
- **Dedicated Clusters**: Starting at $57 per month for production applications that require more consistent performance and resources.
- **Shared Clusters**: Free tier available for educational use or small projects.
    - For more detailed pricing information, visit the [MongoDB Pricing page](https://www.mongodb.com/pricing#mdb-modal-dedicated).

---

### **MongoDB Enterprise Advanced**

MongoDB Enterprise Advanced is designed for enterprises that require robust features, high security, and support for hybrid cloud environments:

- **Robust Security**: Includes advanced encryption and compliance features to meet strict security requirements.
- **Ops Manager**: A management tool that simplifies monitoring, automation, and backups for MongoDB deployments.
- **BI Connector and [Kubernetes](docs/Containerization_and_Deployment/Docker_and_Kubernetes.md) Operator**: Helps integrate MongoDB with IT systems and orchestrates deployments in [Kubernetes](docs/Containerization_and_Deployment/Docker_and_Kubernetes.md) environments.

For more information, visit the [MongoDB Enterprise page](https://www.mongodb.com/try/download/enterprise).