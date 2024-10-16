---
created: 2024-10-14 09:38
updated: 2024-10-16 09:39
---
# Bot Framework security guidelines
- use of HTTPS
- self-destructing messages
- [[data storage]]
	- database firewall 
	- database hardening 
		- updated, all security controls enabled and uninstall/delete all features that aren't needed
	- no valuable information stored in the DB
- user authentication
- https://learn.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-authentication?view=azure-bot-service-4.0&tabs=multitenant


### data storage -> [Key vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)
- store and control access to tokens, passwords, certificates, API keys
- create and control the encryption keys used
- provision, manage, and deploy public and private TLS/SSL certificates

### [Testing bots (DRAFT)](https://github.com/microsoft/botframework-sdk/blob/main/specs/testing/testing.md)
#### Test types
- **Unit Tests**

    Are written by developers and normally executed as part of the Continuous Integration build pipeline.
    Their main purpose is to ensure that the coded logic for a bot executes as expected.
    
- **Natural Language Understanding Tests**
    
    Can be written by developers, NLU engineers or Product owners and can be executed as part of the CI pipeline or when the language model for the bot changes.
    Their main purpose is to ensure that the bot understands what the user is asking and that there are no regressions in the language models when they are extended or modified.
    These tests typically target LUIS and QnAMaker.
    
- **Language Generation tests**
    
    They are written by NLU engineers or Product owners and are executed as part of the CI pipeline of the underlying Language Generation files (.lg files) for the bot change.
    Their main goal is to ensure the bot constructs meaningful, variable and grammatically correct responses to the user.
    
    See [this page](https://github.com/Microsoft/botbuilder-dotnet/tree/ComposableDialog/doc/LanguageGeneration) for an overview of LG files.
    
- **Functional tests**
    
    Also called End to End tests, these tests target the entire bot and its dependent services.
    Non-technical audiences should be able to write and execute these type of tests.
    
- **UI Testing**
    
    Coded UI tests are used for UI-driven functional automation of bots deployed to different channels.
    These tests use open source frameworks like [Selenium](https://docs.seleniumhq.org/) or [Appium](http://appium.io/) to automate UI execution of the client app and playback pre-created scripts.
    These tests are written by developers in conjuntion with product owners.
    
- **Load Tests**
    
    These tests validate that the solution will work under the expected user load. They are typically written by testers and developers and cover end to end scenarios under a variable set of load conditions.
    
    
- **Health checks**
    
    Helth checks are executed on deployed bots and ensure that all the bot and its related services are working as expected in production.
    These tests can be integrated with operation dashboard and trigger alerts if something in the bot is broken.


### Bot Framework Web Chat

[](https://github.com/microsoft/botframework-sdk/tree/main#bot-framework-web-chat)

The Bot Framework [Web Chat](https://github.com/Microsoft/BotFramework-WebChat#readme) is a highly customizable web-based client chat control for Azure Bot Service that provides the ability for users to interact with your bot directly in a web page. [[Stable release](https://www.npmjs.com/package/botframework-webchat) | [Docs](https://github.com/Microsoft/BotFramework-WebChat/tree/main/docs) | [Samples](https://github.com/Microsoft/BotFramework-WebChat/tree/main/samples)]

### Bot Framework CLI

[](https://github.com/microsoft/botframework-sdk/tree/main#bot-framework-cli)

The Bot Framework CLI Tools hosts the [open source](https://github.com/microsoft/botframework-cli) cross-platform Bot Framework CLI tool, designed to support building robust end-to-end development workflows. The Bot Framework CLI tool replaced the [legacy standalone tools](https://github.com/Microsoft/BotBuilder-Tools) used to manage bots and related services. BF CLI aggregates the collection of cross-platform tools into one cohesive and consistent interface.

### Bot Framework Composer

[](https://github.com/microsoft/botframework-sdk/tree/main#bot-framework-composer)

[Bot Framework Composer](https://github.com/microsoft/BotFramework-Composer/blob/main/README.md) is an integrated development tool for developers and multi-disciplinary teams to build bots and conversational experiences with the Microsoft Bot Framework. Within this tool, you'll find everything you need to build a sophisticated conversational experience.

### [[Botkit]]

[](https://github.com/microsoft/botframework-sdk/tree/main#botkit)

[Botkit](https://github.com/howdyai/botkit#readme) is a developer tool and SDK for building chat bots, apps and custom integrations for major messaging platforms. Botkit bots `hear()` triggers, `ask()` questions and `say()` replies. Developers can use this syntax to build dialogs - now cross compatible with the latest version of Bot Framework SDK.

In addition, Botkit brings with it 6 platform adapters allowing Javascript bot applications to communicate directly with messaging platforms: [Slack](https://github.com/howdyai/botkit/tree/main/packages/botbuilder-adapter-slack#readme), [Webex Teams](https://github.com/howdyai/botkit/tree/main/packages/botbuilder-adapter-webex#readme), [Google Hangouts](https://github.com/howdyai/botkit/tree/main/packages/botbuilder-adapter-hangouts#readme), [Facebook Messenger](https://github.com/howdyai/botkit/tree/main/packages/botbuilder-adapter-facebook#readme), [Twilio](https://github.com/howdyai/botkit/tree/main/packages/botbuilder-adapter-twilio-sms#readme), and [Web chat](https://github.com/howdyai/botkit/tree/main/packages/botbuilder-adapter-web#readme).

Botkit is part of Microsoft Bot Framework and is released under the [MIT Open Source license](https://github.com/howdyai/botkit/blob/main/LICENSE.md)


# Bot Framework Emulator

[](https://github.com/microsoft/botframework-emulator#bot-framework-emulator)

The Bot Framework Emulator is a desktop application that allows bot developers to test and debug bots built using the [Bot Framework SDK](https://github.com/microsoft/botbuilder). You can use the Bot Framework Emulator to test bots running either locally on your machine or connect to bots running remotely through a tunnel.

This repo is part the [Microsoft Bot Framework](https://github.com/microsoft/botframework-sdk) - a comprehensive framework for building enterprise-grade conversational AI experiences.


# [Implement custom storage for your bot](https://learn.microsoft.com/en-us/azure/bot-service/bot-builder-custom-storage?view=azure-bot-service-4.0)


# [Azure Monitor data sources and data collection methods](https://learn.microsoft.com/en-us/azure/azure-monitor/data-sources)
![[overview-blowout-20230707-opt.svg]]

|     |     |     |
| --- | --- | --- |
| Activity log | The Activity log provides insight into subscription-level events for Azure services including service health records and configuration changes. | Collected automatically. View in the Azure portal or create a diagnostic setting to send it to other destinations. Can be collected in Log Analytics workspace at no charge. See [Azure Monitor activity log](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/activity-log). | 
| Platform metrics | Platform metrics are numerical values that are automatically collected at regular intervals for different aspects of a resource. The specific metrics vary for each type of resource. | Collected automatically and stored in [Azure Monitor Metrics](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-platform-metrics). View in metrics explorer or create a diagnostic setting to send it to other destinations. See [Azure Monitor Metrics overview](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/data-platform-metrics) and [Supported metrics with Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/supported-metrics/metrics-index) for a list of metrics for different services. | 
| Resource logs |  Provide insight into operations that were performed within an Azure resource. The content of resource logs varies by the Azure service and resource type. | You must create a diagnostic setting to collect resources logs. See [Azure resource logs](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/resource-logs) and [Supported services, schemas, and categories for Azure resource logs](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/resource-logs-schema) for details on each service. | 
|     |     |     |

# [Application Insights overview](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview)
## Experiences

Application Insights provides many experiences to enhance the performance, reliability, and quality of your applications.

[](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview#investigate)

### Investigate

- [Application dashboard](https://learn.microsoft.com/en-us/azure/azure-monitor/app/overview-dashboard): An at-a-glance assessment of your application's health and performance.
- [Application map](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-map): A visual overview of application architecture and components' interactions.
- [Live metrics](https://learn.microsoft.com/en-us/azure/azure-monitor/app/live-stream): A real-time analytics dashboard for insight into application activity and performance.
- [Transaction search](https://learn.microsoft.com/en-us/azure/azure-monitor/app/transaction-search-and-diagnostics?tabs=transaction-search): Trace and diagnose transactions to identify issues and optimize performance.
- [Availability view](https://learn.microsoft.com/en-us/azure/azure-monitor/app/availability-overview): Proactively monitor and test the availability and responsiveness of application endpoints.
- [Failures view](https://learn.microsoft.com/en-us/azure/azure-monitor/app/failures-and-performance-views?tabs=failures-view): Identify and analyze failures in your application to minimize downtime.
- [Performance view](https://learn.microsoft.com/en-us/azure/azure-monitor/app/failures-and-performance-views?tabs=performance-view): Review application performance metrics and potential bottlenecks.

[](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview#monitoring)

### Monitoring

- [Alerts](https://learn.microsoft.com/en-us/azure/azure-monitor/alerts/alerts-overview): Monitor a wide range of aspects of your application and trigger various actions.
- [Metrics](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/metrics-getting-started): Dive deep into metrics data to understand usage patterns and trends.
- [Diagnostic settings](https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/diagnostic-settings): Configure streaming export of platform logs and metrics to the destination of your choice.
- [Logs](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview): Retrieve, consolidate, and analyze all data collected into Azure Monitoring Logs.
- [Workbooks](https://learn.microsoft.com/en-us/azure/azure-monitor/visualize/workbooks-overview): Create interactive reports and dashboards that visualize application monitoring data.

[](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview#usage)

### Usage

- [Users, sessions, and events](https://learn.microsoft.com/en-us/azure/azure-monitor/app/usage#users-sessions-and-events---analyze-telemetry-from-three-perspectives): Determine when, where, and how users interact with your web app.
- [Funnels](https://learn.microsoft.com/en-us/azure/azure-monitor/app/usage#funnels---discover-how-customers-use-your-application): Analyze conversion rates to identify where users progress or drop off in the funnel.
- [Flows](https://learn.microsoft.com/en-us/azure/azure-monitor/app/usage#user-flows---analyze-user-navigation-patterns): Visualize user paths on your site to identify high engagement areas and exit points.
- [Cohorts](https://learn.microsoft.com/en-us/azure/azure-monitor/app/usage#cohorts---analyze-a-specific-set-of-users-sessions-events-or-operations): Group users by shared characteristics to simplify trend identification, segmentation, and performance troubleshooting.

[](https://learn.microsoft.com/en-us/azure/azure-monitor/app/app-insights-overview#code-analysis)

### Code analysis

- [Profiler](https://learn.microsoft.com/en-us/azure/azure-monitor/profiler/profiler-overview): Capture, identify, and view performance traces for your application.
- [Code optimizations](https://learn.microsoft.com/en-us/azure/azure-monitor/insights/code-optimizations): Harness AI to create better and more efficient applications.
- [Snapshot debugger](https://learn.microsoft.com/en-us/azure/azure-monitor/snapshot-debugger/snapshot-debugger): Automatically collect debug snapshots when exceptions occur in .NET application
- 
### Unsupported Software Development Kits (SDKs)

Many community-supported Application Insights SDKs exist, but Microsoft only provides support for instrumentation options listed in this article.

### What telemetry does Application Insights collect?

From server web apps:

- HTTP requests.
- [Dependencies](https://learn.microsoft.com/en-us/azure/azure-monitor/app/asp-net-dependencies). Calls to SQL databases, HTTP calls to external services, Azure Cosmos DB, Azure Table Storage, Azure Blob Storage, and Azure Queue Storage.
- [Exceptions](https://learn.microsoft.com/en-us/azure/azure-monitor/app/asp-net-exceptions) and stack traces.
- [Performance counters](https://learn.microsoft.com/en-us/azure/azure-monitor/app/performance-counters): Performance counters are available when using:
    - [Azure Monitor Application Insights agent](https://learn.microsoft.com/en-us/azure/azure-monitor/app/application-insights-asp-net-agent)
    - [Azure monitoring for VMs or virtual machine scale sets](https://learn.microsoft.com/en-us/azure/azure-monitor/app/azure-vm-vmss-apps)
    - [Application Insights `collectd` writer](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/app/deprecated-java-2x#collectd-linux-performance-metrics-in-application-insights-deprecated).
- [Custom events and metrics](https://learn.microsoft.com/en-us/azure/azure-monitor/app/api-custom-events-metrics) that you code.
- [Trace logs](https://learn.microsoft.com/en-us/azure/azure-monitor/app/asp-net-trace-logs) if you configure the appropriate collector.

From [client webpages](https://learn.microsoft.com/en-us/azure/azure-monitor/app/javascript-sdk):

- Uncaught exceptions in your app, including information on
    
    - Stack trace
    - Exception details and message accompanying the error
    - Line & column number of error
    - URL where error was raised
    - Network Dependency Requests made by your app XML Http Request (XHR) and Fetch (fetch collection is disabled by default) requests, include information on:
        - Url of dependency source
        - Command & Method used to request the dependency
        - Duration of the request
        - Result code and success status of the request
        - ID (if any) of user making the request
        - Correlation context (if any) where request is made
- User information (for example, Location, network, IP)
    
- Device information (for example, Browser, OS, version, language, model)
    
- Session information
    
    Note
    
    For some applications, such as single-page applications (SPAs), the duration may not be recorded and will default to 0.
    
    For more information, see [Data collection, retention, and storage in Application Insights](https://learn.microsoft.com/en-us/previous-versions/azure/azure-monitor/app/data-retention-privacy).
    

From other sources, if you configure them:

- [Azure diagnostics](https://learn.microsoft.com/en-us/azure/azure-monitor/agents/diagnostics-extension-to-application-insights)
- [Import to Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api)
- [Log Analytics](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api)
- [Logstash](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/data-collector-api)


# [About Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview)
Azure Key Vault is one of several [key management solutions in Azure](https://learn.microsoft.com/en-us/azure/security/fundamentals/key-management), and helps solve the following problems:

- **Secrets Management** - Azure Key Vault can be used to Securely store and tightly control access to tokens, passwords, certificates, API keys, and other secrets
- **Key Management** - Azure Key Vault can be used as a Key Management solution. Azure Key Vault makes it easy to create and control the encryption keys used to encrypt your data.
- **Certificate Management** - Azure Key Vault lets you easily provision, manage, and deploy public and private Transport Layer Security/Secure Sockets Layer (TLS/SSL) certificates for use with Azure and your internal connected resources.

#  [Set up continuous integration and continuous delivery for a Composer bot](https://learn.microsoft.com/en-us/composer/how-to-cicd)
|File|Description|
|---|---|
|[buildAndDeploy.yaml](https://github.com/microsoft/BotBuilder-Samples/blob/main/composer-samples/csharp_dotnetcore/pipelines/CICDPipelineSample/build/yaml/buildAndDeploy.yaml)|The main YAML file used when the Azure DevOps pipeline is triggered. It maps Azure DevOps variables (see [Define variables](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/variables) for additional information) into YAML [runtime parameters](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/runtime-parameters) and then sequentially calls the YAML templates in the templates folder to build and deploy the bot.|
|[templates/installPrerequisites.yaml](https://github.com/microsoft/BotBuilder-Samples/blob/main/composer-samples/csharp_dotnetcore/pipelines/CICDPipelineSample/build/yaml/templates/installPrerequisites.yaml)|Installs the tools needed to run the pipeline, like npm, BF CLI, and .NET core.|
|[templates/buildAndDeployModels.yaml](https://github.com/microsoft/BotBuilder-Samples/blob/main/composer-samples/csharp_dotnetcore/pipelines/CICDPipelineSample/build/yaml/templates/buildAndDeployModels.yaml)|Builds, trains, and deploys LUIS and QnA Maker models. This template also creates a **generated** subfolder in your bot project's directory. The **generated** folder is needed by the bot.|
|[templates/buildAndDeployDotNetWebApp.yaml](https://github.com/microsoft/BotBuilder-Samples/blob/main/composer-samples/csharp_dotnetcore/pipelines/CICDPipelineSample/build/yaml/templates/buildAndDeployDotNetWebApp.yaml)|Builds the dotnet bot app, prepares the zip package, and deploys it to Azure. It also configures the app settings for the app in Azure once it's deployed.|
|[templates/Build-LUIS.ps1](https://github.com/microsoft/BotBuilder-Samples/blob/main/composer-samples/csharp_dotnetcore/pipelines/CICDPipelineSample/build/yaml/templates/Build-LUIS.ps1)|Builds and trains LUIS models.|
|[templates/Build-Orchestrator.ps1](https://github.com/microsoft/BotBuilder-Samples/blob/main/composer-samples/csharp_dotnetcore/pipelines/CICDPipelineSample/build/yaml/templates/Build-Orchestrator.ps1)|Builds and trains Orchestrator models.|
|[templates/LUUtils.ps1](https://github.com/microsoft/BotBuilder-Samples/blob/main/composer-samples/csharp_dotnetcore/pipelines/CICDPipelineSample/build/yaml/templates/LUUtils.ps1)|Contains language understanding functions used in other scripts.|


# [Test and debug with the Emulator](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-debug-emulator?view=azure-bot-service-4.0&tabs=csharp)
Bot Framework Emulator is a desktop application that allows bot developers to test and debug bots, either locally or remotely. Using the Emulator, you can chat with your bot and inspect the messages that your bot sends and receives. The Emulator displays messages as they would appear in a web chat UI and logs JSON requests and responses as you exchange messages with your bot. Before you deploy your bot to the cloud, run it locally and test it using the Emulator. You can test your bot using the Emulator even if you haven't yet [created](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-quickstart?view=azure-bot-service-4.0) it with Azure AI Bot Service or configured it to run on any channels.

## Connect to a bot running on localhost

[](https://learn.microsoft.com/en-us/azure/bot-service/bot-service-debug-emulator?view=azure-bot-service-4.0&tabs=csharp#configure-proxy-settings)

### Configure proxy settings

When you're developing behind a corporate proxy, the Emulator will use the configured environment variables `HTTP_PROXY` and `HTTPS_PROXY`, which specify the proxy URL route for HTTP and HTTPs requests respectively.

If you're connecting to a bot running on `localhost`, the Emulator will first try to route through the proxy before connecting to `localhost`. Typically, the proxy will block the connection unless you specify that it should be bypassed for `localhost`.

In order to bypass the `HTTP_PROXY` and `HTTPS_PROXY` settings and allow the Emulator to connect to `localhost`, on your local machine you must define the following environment variable:

Windows Command Prompt

```
NO_PROXY=localhost
```



# [Debug and validate language generation and understanding files](https://learn.microsoft.com/en-us/composer/how-to-validate?tabs=v2x)
This article introduces the validation functionality provided in Bot Framework Composer. The validation functionality helps you identify syntax errors and provide suggested fixes when you author [.lg](https://learn.microsoft.com/en-us/azure/bot-service/file-format/bot-builder-lg-file-format) files, [.lu](https://learn.microsoft.com/en-us/azure/bot-service/file-format/bot-builder-lu-file-format) files, and [expressions](https://learn.microsoft.com/en-us/azure/bot-service/bot-builder-concept-adaptive-expressions) during the process of developing a bot using Composer. With the help of the validation functionality, your bot-authoring experience will be improved and you can easily build a functional bot that can run correctly.

[](https://learn.microsoft.com/en-us/composer/how-to-validate?tabs=v2x#prerequisites)

## Prerequisites

- [Install Bot Framework Composer](https://learn.microsoft.com/en-us/composer/install-composer).
- A basic understanding of [language generation](https://learn.microsoft.com/en-us/composer/concept-language-generation).
- A basic understanding of [language understanding](https://learn.microsoft.com/en-us/composer/concept-language-understanding).
- A basic understanding of [adaptive expressions](https://learn.microsoft.com/en-us/azure/bot-service/bot-builder-concept-adaptive-expressions).

# [[Azure pricing ]]


[Link](https://azure.microsoft.com/en-gb/products/ai-services/ai-bot-service/)
[Book(**Developer’s Guide to Building AI Applications, Second Edition**)](https://info.microsoft.com/ww-landing-a-developers-guide-to-building-ai-applications.html)

### Microsoft AI Bot Service
- **Low-Code Graphical Interface**: This feature allows users to create bots without extensive coding knowledge, making bot development accessible to a wider audience.
- **Telemetry Tracking**: Ability to monitor critical metrics, helping you identify popular topics and potential improvements for user engagement.
- **SaaS Solution**: Consolidates various functionalities into a single platform, streamlining bot development and management.
- **Multi-Channel Support**: The service allows bots to be deployed across multiple platforms, enhancing reach and usability (e.g., websites, mobile apps, Facebook, Microsoft Teams).

### Microsoft Copilot Studio
- **Conversational Application Design**: Utilize generative AI and large language models to create sophisticated conversational agents.
- **Knowledge Access**: Agents can quickly retrieve answers from organizational websites or internal databases, improving response accuracy.
- **Trigger Actions**: Use Power Platform connectors and Power Automate flows to create responsive actions based on user interactions.
- **Data Connectors**: Offers extensive options for integrating data from both Microsoft and non-Microsoft sources.
- **Flexible Development**: Agents can be built using natural language, through a graphical interface, or with code, catering to different developer skill levels.
- **Escalation Capabilities**: Ability to escalate complex conversations to human agents, ensuring users receive the assistance they need.

### Power Platform Admin Center
- **Built-In Analytics**: Provides insights and analytics for monitoring bot performance, user interactions, and operational metrics.
