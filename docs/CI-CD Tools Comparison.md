---
created: 2024-10-01 15:45
updated: 2024-10-15 10:21
---

### **GitHub Actions**
**Why Use**: It's easier to set up, integrates smoothly with GitHub repositories, and works well for small-to-medium projects.
[[Example GitHub Actions Pipeline]]

### **Azure Pipelines**
**Why Use**: Ideal for more complex workflows, especially if the chatbot is hosted in Azure. Offers advanced integration with other Azure services.
[[Example Azure Pipelines YAML]]


### **Tradeoffs**:
- **GitHub Actions**: Simpler setup, easier to configure for smaller teams or projects.
- **Azure Pipelines**: Ideal if already using Azure services, providing more advanced CI/CD workflows for larger or more complex apps.

---

## **Testing Tools**

### **Unit Testing**:
- **Pytest**: Simple, widely used for Python projects, makes it easy to write test cases.
- **unittest**: Built-in Python framework for unit tests.
[[Example Pytest Unit Test]]


### **End-to-End Testing**:
- **Botium**: Designed specifically for testing chatbot conversation flows and integrations.
- **Selenium/Cypress**: Great for UI testing of web-based chatbots.
[[Botium Example]]


### **Performance Testing**:
- **Locust**: Simulates user load to assess scalability and performance.
[[Locust Test Example]]


### **Tradeoffs**:
- **Quick & Easy**: `pytest` or `unittest` offer rapid integration for unit testing core chatbot functions.
- **Important**: `Botium` provides extensive conversation flow testing, vital for validating chatbot logic.
- **Nice-to-Have**: Performance tests with `Locust` to ensure the chatbot can handle increasing user loads.
