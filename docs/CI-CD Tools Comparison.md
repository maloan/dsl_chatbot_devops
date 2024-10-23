---
created: 2024-10-22 13:03
updated: 2024-10-23 12:23
---

## Continuous Integration and Continuous Delivery (CI/CD) Tools
- GitHub Actions 
- Azure Pipelines

---

### 1. **GitHub Actions**

#### Overview
GitHub Actions, integrated into GitHub, automates workflows based on repository events like pull requests and commits. It’s best suited for small-to-medium projects.

#### Use Cases
- **Simple Workflows**: Ideal for running tests, building Docker containers, and deploying web apps.
- **GitHub Integration**: Perfect for teams using GitHub for version control.
- **Event-Driven**: Automates actions based on GitHub events.
- **Open Source Projects**: Cost-effective for open-source due to its free usage for public repositories.

#### Advantages
- **Easy Setup**: Quick configuration with predefined actions or YAML files.
- **Native Integration**: Seamless experience without external tools.
- **Reusable Actions Marketplace**: Access to pre-configured actions for common tasks.
- **Cost Efficiency**: Generous free-tier for small and open-source projects.
- **Customizable Workflows**: Tailored workflows based on repository events.

#### Disadvantages 
- **Complex Workflows**: Limited support for very complex multi-stage deployments.
- **Scaling Issues**: Can become cumbersome as project complexity grows.
- **Platform-Limited**: More effort required for integration with non-GitHub services.

#### Cost
- **Free for Public Repositories**: Unlimited usage.
- **Private Repositories**: 2,000 free minutes/month; $0.008 per additional minute and $0.25 per GB/month for storage.

[[Example GitHub Actions Pipeline]]

#### Links
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)

---

### 2. **Azure Pipelines**
#### Overview
Azure Pipelines is a comprehensive CI/CD service from Microsoft, part of Azure DevOps. It is suitable for complex workflows, especially for Azure-based deployments, and supports any language and platform.

#### Use Cases
- **Complex Workflows**: Ideal for intricate, multi-stage CI/CD flows integrating with services like Kubernetes and VMs.
- **Azure Integration**: Perfect for teams using Azure, enabling smooth deployments to services like AKS and Azure App Services.
- **Multi-Cloud & Hybrid Deployments**: Supports deployments across multiple clouds and on-premise environments.
- **Advanced CI/CD Pipelines**: Features like gated check-ins and release management make it suitable for enterprises.

#### Advantages
- **Deep Azure Integration**: Simplifies Azure service deployments.
- **Advanced Workflow Features**: Offers detailed control over pipeline stages and conditions.
- **Language Agnostic**: Supports many programming languages and platforms.
- **Extensive Customization**: Uses YAML-based pipelines for complex workflows.
- **Built-in Test Management**: Automates testing with detailed reporting.

#### Disadvantages
- **Steeper Learning Curve**: Requires a solid grasp of CI/CD concepts.
- **Cost at Scale**: Potentially expensive for large teams or extensive compute needs.

#### Cost
- **Free Tier**: 1,800 minutes/month for public projects and 1 free parallel job.
- **Paid Plans**: $40/month for additional parallel jobs; self-hosted agents are free but incur Azure resource costs.

[[Example Azure Pipelines YAML]]


#### Links
- [Azure Pipelines Documentation](https://learn.microsoft.com/en-us/azure/devops/pipelines/)
- [Example Azure Pipeline for Bot Framework](https://learn.microsoft.com/en-us/composer/how-to-cicd)

---

### Comparison of GitHub Actions vs. Azure Pipelines

| Feature              | **GitHub Actions**                                         | **Azure Pipelines**                                              |
| -------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------- |
| **Ease of Setup**    | Easy to set up, integrates natively with GitHub            | More complex setup, but supports powerful features               |
| **Ideal Use Case**   | Simple-to-medium projects, GitHub-centric workflows        | Large, complex workflows, enterprise applications                |
| **Platform Support** | Best for GitHub-hosted repositories                        | Supports any platform, integrates with GitHub, Azure, and others |
| **Customization**    | High, with pre-configured actions and custom workflows     | Extremely high, with full YAML configuration support             |
| **Integration**      | GitHub Marketplace for third-party tools                   | Deep integration with Azure, supports multiple cloud platforms   |
| **Cost**             | Free for public repos, $0.008 per minute for private repos | Free for 1,800 minutes/month, $40 per additional parallel job    |
| **Best For**         | Small-to-medium projects, open-source workflows            | Enterprise-level projects, Azure-hosted apps                     |

---

### Additional CI/CD Tools
- **Jenkins**: Highly customizable, supports complex workflows, open-source. [Documentation](https://www.jenkins.io/doc/)
- **Spinnaker & ArgoCD**: For blue-green deployments and smooth updates, open-source. [Documentation](https://www.spinnaker.io/)

---

### Further reading
- [Set up CI/CD for Composer Bot](https://learn.microsoft.com/en-us/composer/how-to-cicd)
- [[Containerization and Deployment]]