---
created: 2024-10-22 15:30
updated: 2024-10-23 13:08
---
### **What is MongoDB?**

MongoDB is a document-oriented database known for its ease of development and scalability. It features a flexible schema, making it suitable for large volumes of diverse data. For more details, refer to the [official MongoDB documentation](https://www.mongodb.com/docs/manual/#what-is-mongodb).

### **Deployment Environments**
MongoDB can be deployed in several ways:
- **[MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server)**: A fully managed cloud service.
- **[MongoDB Enterprise](https://www.mongodb.com/docs/manual/administration/install-enterprise/#std-label-install-mdb-enterprise)**: A subscription-based platform for enterprises requiring advanced features.
- **[MongoDB Community Edition](https://www.mongodb.com/docs/manual/administration/install-community/#std-label-install-mdb-community-edition)**: An open-source version for developers and small businesses.

### **Securing MongoDB Deployments**
MongoDB Atlas incorporates essential security features:
- **Authentication and Authorization**: Control user access rights with methods like LDAP and OIDC; see [MongoDB’s security page](https://www.mongodb.com/docs/atlas/security/config-db-auth/).
- **Encryption**: Data is encrypted by default, both at rest and in transit. Learn more about [Encryption at Rest](https://www.mongodb.com/docs/atlas/security-kms-encryption/).
- **IP Access List**: Restrict access to specified IPs; see [IP Access List documentation](https://www.mongodb.com/docs/atlas/security/ip-access-list/).
- **Cloud Provider Support**: Works with AWS, Azure, and Google Cloud for enhanced security.

### **SQL Support in MongoDB**
MongoDB uses its own query language but allows SQL through the [MongoDB Connector for BI](https://www.mongodb.com/products/bi-connector). The [MongoDB Application Modernization Guide](https://www.mongodb.com/modernize?tck=docs_server) aids in transitioning from SQL databases.

### **MongoDB Pricing**
Pricing options include:
- **Serverless Instances**: From $0.10 per million reads for casual applications.
- **Dedicated Clusters**: Starting at $57 per month for production use.
- **Shared Clusters**: A free tier for educational use
  [Pricing and configurations](https://www.mongodb.com/pricing#mdb-modal-dedicated)

### **MongoDB Enterprise Advanced**
For on-premises or hybrid needs, it offers:
- **Robust Security**: Advanced encryption and compliance.
- **Ops Manager**: Simplifies database management.
- **BI Connector and Kubernetes Operator**: Enhances IT integration.
Visit [MongoDB Enterprise](https://www.mongodb.com/try/download/enterprise) for more information.
