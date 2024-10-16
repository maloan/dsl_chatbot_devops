---
created: 2024-10-16 09:42
updated: 2024-10-16 09:42
---

# [Managing Chat History at scale in Generative AI Chatbots](https://community.aws/content/2j9daS4A39fteekgv9t1Hty11Qy/managing-chat-history-at-scale-in-generative-ai-chatbots)
#### 

**The Problem:**

---

1. Maintaining Accurate Conversation Context:
    
    - Users expect chatbots to understand previous interactions and provide relevant, personalized responses. Without efficient access to chat history, responses can become disjointed and impersonal.
        
2. Token Limit Constraints of LLMs:
    
    - LLMs have a maximum input token limit, restricting how much context they can consider at once.
        
    - Directly passing large chat histories to an LLM can exceed this limit, leading to incomplete context or errors.
        
3. Relevance vs. Redundancy:
    
    - Passing too much data to the LLM can introduce noise, reducing response quality.
        
    - Including redundant information overwhelms the LLM and consumes valuable tokens.
        
4. Data Management Challenges:
    
    - The chat system must efficiently handle growing volumes of messages.
        
    - Ensuring each message is quickly stored and queried is critical for performance.
        

#### 

**The Solution**

---

![](https://community.aws/_next/image?url=https%3A%2F%2Fassets.community.aws%2Fa%2F2j9fM357nm65A7IXajGo9D7W1m0%2Farch.webp%3FimgSize%3D1236x798&w=3840&q=75 "Architecture")

Architecture

The solution involves three key components that work together to ensure chat history is stored, summarized, and queried efficiently:

1. **In-Memory Chat History Storage (Redis):**
    
    - **Purpose:** Provides immediate access to recent chat messages, reducing latency during live conversations.
        
    - **Structure:** Messages are stored in user-specific Redis stacks, organized by batch for fast retrieval and summarization.
        
    - **Use:** Offers high-speed reads/writes, serving as a buffer before data is persisted to DynamoDB.
        
2. **Persistent Chat History Storage (DynamoDB):**
    
    - **Purpose:** Ensures reliable and scalable storage of all historical chat data.
        
    - **Structure:** Uses a composite primary key to query messages based on `UserId` and `Timestamp`.
        
    - **Use:** Enables consistent long-term storage and retrieval, allowing access to complete historical data.
        
3. **Summarization Logic:**
    
    - **Purpose:** Aggregates every 20 messages into a summary to provide concise conversation context.
        
    - **Batch Summaries:** Summaries contain essential details that are more relevant than passing all messages individually to the LLM.
        
    - **Use:** Provides a compact overview of conversations, reducing input size for LLMs while maintaining relevant historical context.

# [Lesson 5: 05 - Chat History and Memory Management](https://pythonmldaily.com/lesson/python-chatbot-langchain/chat-history-memory-management)
Great, so we have the first response from our chatbot. But quite often, in real-life scenarios, we need to continue with a follow-up question.

With our current code, if we launch the second request to the `chain()`, it will NOT remember the previous question/answer. Let's fix this.

A straightforward way is to save the history in a local variable and pass it every time:

```
history = [] query = 'Do you have a team plan?'response = chain.invoke({"question": query, "chat_history": history})history.append([query, response['answer']]) query2 = 'And what about free plan?'response = chain.invoke({"question": query2, "chat_history": history})history.append([query2, response['answer']])
```

But a more structured approach would be to use a specific class for it from LangChain, called `ConversationBufferMemory()`, passing it as the third parameter to the chain `from_llm()` function.

Then, the response would automatically contain the item of the `chat_history` or whatever the `memory_key` value you provide.

```
import osfrom langchain.document_loaders.csv_loader import CSVLoaderfrom langchain_openai import OpenAIEmbeddingsfrom langchain_community.vectorstores import FAISSfrom langchain_openai import ChatOpenAIfrom langchain.chains import ConversationalRetrievalChainfrom langchain.memory import ConversationBufferMemory  os.environ["OPENAI_API_KEY"] = 'sk-...' loader = CSVLoader(file_path="faq.csv")documents = loader.load() vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings()) memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)  chain = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(),                                              retriever=vectorstore.as_retriever(),                                              memory=memory)  query = "Do you have a team plan?" response = chain.invoke({"question": query})  query2 = 'And what about free plan?' response = chain.invoke({"question": query2})  print(response['chat_history']) 
```

```
# Output:[  HumanMessage(content='Do you have a team plan?'),  AIMessage(content='Yes, we do have a team plan. The team plan is available on a yearly basis for up to 7 team members and costs $299 per year. We also offer a lifetime membership for teams with up to 7 members, which is priced at $799.'),  HumanMessage(content='And what about free plan?'),  AIMessage(content='Based on the given context, there is no mention of a free plan. Therefore, it can be inferred that there is no free plan available.')]
```

That's it, not much to add here. The history of the conversation would be saved throughout the lifetime of the Python script.

Now, if you want to save that history outside of the script, then it's a separate big topic. You would probably need a database to store the messages, assign them to specific users or chat sessions, etc. We will not cover such history management in this tutorial.

# [Implementing Session-based Chat History for a Chatbot using Langchain and Database](https://blog.gopenai.com/implementing-session-based-chat-history-for-a-chatbot-using-langchain-and-database-cda0734f6344)

# What is MongoDB?[](https://www.mongodb.com/docs/manual/#what-is-mongodb- "Permalink to this heading")

MongoDB is a document database designed for ease of application development and scaling.

You can run MongoDB in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server)
    

- [](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully managed service for MongoDB deployments in the cloud
    

- [MongoDB Enterprise](https://www.mongodb.com/docs/manual/administration/install-enterprise/#std-label-install-mdb-enterprise)
    

- [](https://www.mongodb.com/docs/manual/administration/install-enterprise/#std-label-install-mdb-enterprise): The subscription-based, self-managed version of MongoDB
    
- [MongoDB Community](https://www.mongodb.com/docs/manual/administration/install-community/#std-label-install-mdb-community-edition)
    
[](https://www.mongodb.com/docs/manual/administration/install-community/#std-label-install-mdb-community-edition): The source-available, free-to-use, and self-managed version of MongoDB 

## Secure Your MongoDB Atlas Deployments[](https://www.mongodb.com/docs/manual/security/#secure-your-mongodb-atlas-deployments "Permalink to this heading")

MongoDB Atlas, the fully managed service for MongoDB deployments in the cloud, comes preconfigured with secure default settings. Atlas also provides the following key security features:

|Security Feature|Description|
|---|---|
|Authentication and Authorization|In Atlas, you configure database users to access your deployments. Atlas provides various ways to perform user authentication and authorization, including LDAP, OIDC, and X.509. To learn more, see [Configure Authentication and Authorization.](https://www.mongodb.com/docs/atlas/security/config-db-auth/)|
|Encryption|By default, Atlas encrypts all data stored in your deployments and uses TLS/SSL to encrypt the connections to your databases. To add another layer of security, you can configure [Encryption at Rest using Customer Key Management.](https://www.mongodb.com/docs/atlas/security-kms-encryption/)|
|IP Access List|Atlas allows connections only from addresses specified in the IP access list. To learn how to manage client connections in Atlas, see [Configure IP Access List Entries.](https://www.mongodb.com/docs/atlas/security/ip-access-list/)|
|Cloud Provider Support|Atlas supports network peering connections and private endpoints to secure your deployments hosted on AWS, Azure, and Google Cloud. To learn more, see [Set Up a Network Peering Connection](https://www.mongodb.com/docs/atlas/security-vpc-peering/) and [Configure Private Endpoints.](https://www.mongodb.com/docs/atlas/security-configure-private-endpoints/)|

## Does MongoDB support SQL?[](https://www.mongodb.com/docs/manual/faq/fundamentals/#does-mongodb-support-sql- "Permalink to this heading")

Not directly, no. However, MongoDB does support a rich query language of its own. For examples on using MongoDB's query language, see [MongoDB CRUD Operations.](https://www.mongodb.com/docs/manual/crud/#std-label-crud)

You can also use the [MongoDB Connector for BI](https://www.mongodb.com/products/bi-connector) to query MongoDB collections with SQL.

If you are considering migrating your SQL application to MongoDB, download the [MongoDB Application Modernization Guide](https://www.mongodb.com/modernize?tck=docs_server) for a best practices migration guide, reference schema, and other helpful resources.




# MongoDB Pricing

The data platform built by - and for - developers

## MongoDB Atlas

The multi-cloud developer data platform available on AWS, Azure, and Google Cloud

![](https://webimages.mongodb.com/_com_assets/cms/kr1forpyj7n2f6uw3-Elastic_Icon.svg?auto=format%2Ccompress&ch=DPR&fix=max&h=30)

### Serverless

from

$0.10/million reads

[Sign Up](https://www.mongodb.com/cloud/atlas/register)(i) Per 1 million reads

For serverless applications with variable or infrequent traffic. Minimal configuration required.

Up to 1TB of storageResources scale seamlessly to meet your workloadPay only for the operations you run

Always-on security and backups[View pricing](https://www.mongodb.com/pricing#mdb-modal-serverless)

![](https://webimages.mongodb.com/_com_assets/cms/kr1fnjggpyn4wa67k-Dedicated_Icon.svg?auto=format%2Ccompress&ch=DPR&fix=max&h=30)

### Dedicated

from

$57/month

[Sign Up](https://www.mongodb.com/cloud/atlas/register)(i) Estimated based on $0.08 per hour

For production applications with sophisticated workload requirements. Advanced configuration controls.

10GB to 4TB of storage

2GB to 768GB RAM

Network isolation and fine-grained access controls

Multi-region and multi-cloud options available[View pricing](https://www.mongodb.com/pricing#mdb-modal-dedicated)

![](https://webimages.mongodb.com/_com_assets/cms/kr1fpoi6njksy0sfl-Playground_Icon.svg?auto=format%2Ccompress&ch=DPR&fix=max&h=30)

### Shared

from

$0/month

[Try for Free](https://www.mongodb.com/cloud/atlas/register)(i) Free forever for free clusters

For learning and exploring MongoDB in a cloud environment. Basic configuration options.

512MB to 5GB of storageShared RAMUpgrade to dedicated clusters for full functionality

No credit card required to start[View pricing](https://www.mongodb.com/pricing#mdb-modal-shared)

# MongoDB Pricing

The data platform built by - and for - developers

## MongoDB Enterprise Advanced

The best way to run MongoDB on-premises or in your private cloud

#### Featured Highlights

- MongoDB Enterprise Server
- [Ops Manager](https://www.mongodb.com/products/ops-manager), the management platform for MongoDB
- Kubernetes Operator
- Enterprise security features
- Business intelligence integration and visualization

- Commercial license
- Self-serve training content
- Rich onboarding and regular check-ins
- Consultative support with fast [initial response goals](https://www.mongodb.com/support-policy)

[

### Enterprise Server

Unlock advanced security and operations features to drive commercial use cases. Use pluggable storage engines for in-memory performance and encryption. Connect MongoDB to existing IT infrastructure with SNMP.

](https://www.mongodb.com/try/download/enterprise)

---

[![mdb_ops_manager](https://webimages.mongodb.com/_com_assets/icons/mdb_ops_manager.svg)

### Ops Manager

Automate time-consuming administration work like deployment, monitoring & alerting, backups, and scaling of your databases from one place. Track over 100 performance metrics and set up custom alerts with ease.

](https://www.mongodb.com/products/ops-manager)

---

[![connectors_bi_connector](https://webimages.mongodb.com/_com_assets/icons/connectors_bi_connector.svg)

### BI Connector

Turn MongoDB into a powerful data source. Streamline BI architecture by connecting MongoDB directly to your analytics and visualization platforms of choice. Avoid complex ETL processes; unlock data for others.

](https://www.mongodb.com/products/bi-connector)

---

[![connectors_kubernetes_operator](https://webimages.mongodb.com/_com_assets/icons/connectors_kubernetes_operator.svg)

### Enterprise Operator for Kubernetes

Orchestrate MongoDB from a single Kubernetes control plane. Get a consistent experience across deployment environments. Automate MongoDB database creation into scalable, repeatable, standardized processes.

](https://www.mongodb.com/kubernetes)


[VectorShift](https://docs.vectorshift.ai/vectorshift/platform/chatbots/conversation-history-and-analytics)

# Conversation History & Analytics

How to manage your conversation history and analytic.

The chatbot manager lets you see your chatbots' conversation history and analytics and download your chatbots. Navigate to the chatbot manager by clicking "Manage chatbot analytics" on the "Chatbots" tab. Within the tab, you can use the pull-down menu to select which chatbot you want to see data about.

![](https://docs.vectorshift.ai/~gitbook/image?url=https%3A%2F%2F2337131889-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8TCaopv9gy4bGub1g4jr%252Fuploads%252FE6m0YJp1QUe6jfrTqqnj%252FCleanShot%25202024-08-24%2520at%252000.31.22%25402x.png%3Falt%3Dmedia%26token%3D25cb0ae4-0182-4937-8506-5582e2b6c03f&width=768&dpr=4&quality=100&sign=1b420d1&sv=1)

Accessing chatbot analytics

## 

[](https://docs.vectorshift.ai/vectorshift/platform/chatbots/conversation-history-and-analytics#chatbot-analytics)

Chatbot Analytics

The Chatbot Analytics feature in VectorShift.ai provides insights into the performance and usage of your chatbot.

![](https://docs.vectorshift.ai/~gitbook/image?url=https%3A%2F%2F2337131889-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8TCaopv9gy4bGub1g4jr%252Fuploads%252F7fGU4gM2EYRakTyuAc3x%252FCleanShot%25202024-08-24%2520at%252000.37.07%25402x.png%3Falt%3Dmedia%26token%3D7b296e1d-78ec-4bb6-b474-b3df10f10d4d&width=768&dpr=4&quality=100&sign=a03ae2f8&sv=1)

1. **Conversation History:** Displays a list of recent interactions, such as "Pancake Making Guide" and "Cat Drawing Request." This helps track popular topics and user interests.
    
2. **Conversations:**
    
    - **Total Conversations:** Shows the total number of conversations, providing an overview of chatbot engagement.
        
    - **Messages:** Indicates the total number of messages exchanged, helping assess interaction volume.
        
    
3. **Cost:** This displays the cost associated with running the chatbot, calculated based on usage and shown in USD. It helps monitor expenses.
    
4. **Feedback:** Tracks the number of positive and negative interactions.
    
5. **Graphical Representation:** A visual graph shows the trend of messages and conversations over time, helping identify patterns and peaks in usage.
    
6. **Download All**: Allow users to choose between downloading the data in CSV or JSON format for all conversations.
    

## 

[](https://docs.vectorshift.ai/vectorshift/platform/chatbots/conversation-history-and-analytics#managing-conversation-history)

Managing Conversation History

The Conversation History allows you to manage and analyze past interactions with your chatbot. You can view, manage, and analyze past interactions with your chatbot:

1. **Conversation List:** This option displays a list of all recent conversations. It helps you track popular topics and understand user interests.
    
2. **Viewing Conversations:** Click on a conversation to view detailed exchanges between the user and the bot. This includes timestamps and message content, providing user behavior and preferences insights.
    
3. **Download Conversations:** Use the "Download" button to export individual conversation histories in CSV or JSON format. This feature allows for offline analysis and record-keeping.
    

![](https://docs.vectorshift.ai/~gitbook/image?url=https%3A%2F%2F2337131889-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8TCaopv9gy4bGub1g4jr%252Fuploads%252FuObTxWEfyTd3efmz9jPG%252FCleanShot%25202024-08-24%2520at%252000.40.56%25402x.png%3Falt%3Dmedia%26token%3Dc1bbf377-e42f-46db-bb41-b49f31c2d211&width=768&dpr=4&quality=100&sign=fe6ce9ca&sv=1)

[PreviousExport Chatbot - API Export](https://docs.vectorshift.ai/vectorshift/platform/chatbots/export-chatbot-api-export)[NextSearch](https://docs.vectorshift.ai/vectorshift/platform/search)

# VectorShift Platform Overview

An overview of the VectorShift Platform

VectorShift's platform allows you to design, prototype, build, deploy, and manage generative AI workflows and automation across two interfaces: no-code and code SDK. Example use cases:

- **Chatbots:** Build a fully functional AI chatbot and embed it into your website. AI chatbots can respond to user queries and answer questions based on a knowledge base (e.g., product documentation, support articles, live-synced Google Drive).
    
- **Search**: Centralize and live-sync your data across your applications (e.g., Google Drive, Slack, One Drive, etc.) in one knowledge base and perform search queries over all your data.
    
- **Automations:** Automate workflows end-to-end, schedule workflows to run at certain time intervals, or allow certain triggers (e.g., email, Slack message) to trigger the running of a workflow; have the VectorShift platform automatically perform actions (e.g., send an email, create a notion document, add data to an Airtable database).
    
- **Content Creation:** Create marketing copy, personalized outbound emails, call summaries, proposals, and graphics at scale and in a predetermined format and style.
    
- **Workflow Automation:** Replicate the logical thinking of a process by breaking down a task into sub-tasks and having different LLMs perform them.

[Chat Memory](https://docs.vectorshift.ai/vectorshift/platform/pipelines/chat/chat-memory)
Give your Pipelines access to Chatbot conversation history using Chat Memory nodes.

An overview of Chat Memory node

## 

[Chat Memory](https://docs.vectorshift.ai/vectorshift/platform/pipelines/chat/chat-memory#chat-memory)



Inherently, LLMs do not have "memory" - they do not remember previous conversation history. However, having a memory in a Chatbot may be useful to refer to previous contexts and outputs.

Essentially, what the chat memory node does it is takes the conversation history and if connected to an LLM, will pass the history back to the LLM so the LLM can reference it / reason with it.

_Note: within the no-code builder, you must run the pipeline as a chatbot (not the "standard" run interface) to reference previous messages._

![](https://docs.vectorshift.ai/~gitbook/image?url=https%3A%2F%2F2337131889-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8TCaopv9gy4bGub1g4jr%252Fuploads%252Fzpg78M6k8xJwIxfeWxzb%252FScreenshot%25202024-03-22%2520at%25209.49.25%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D636ceb73-107b-4694-9089-7fbe7bea51fd&width=768&dpr=4&quality=100&sign=ccd9df93&sv=1)

## 

[](https://docs.vectorshift.ai/vectorshift/platform/pipelines/chat/chat-memory#different-types-of-chat-memory)

**Different types of chat memory**

You can select the following types of chat memory with the full down menu within the chat memory node. The default is "Token Buffer"

### 

[](https://docs.vectorshift.ai/vectorshift/platform/pipelines/chat/chat-memory#full-formatted)

_Full - Formatted_

Returns all previous chat history, with user messages prepended with "Human" and output messages prepended with "AI". Useful for handling short conversations, but may run into token limits once conversations start becoming longer.

### 

[](https://docs.vectorshift.ai/vectorshift/platform/pipelines/chat/chat-memory#full-raw)

_Full - Raw_

Returns a Python list with elements in the following format: `{"type": type, "message": message}`, where `type` is `"input"` (i.e., Human) or `"output"` (i.e., AI) and `message` contains the contents of the message. Useful for developers looking to execute custom logic with their chat history using [Transformations](https://docs.vectorshift.ai/vectorshift/platform/transformations).

### 

[](https://docs.vectorshift.ai/vectorshift/platform/pipelines/chat/chat-memory#message-buffer)

_Message Buffer_

Returns a set number of previous consecutive messages. This number defaults to 10 and can be changed by right-clicking the Chat Memory node and clicking "Details". Both Human messages and AI messages count toward the limit.

### 

[](https://docs.vectorshift.ai/vectorshift/platform/pipelines/chat/chat-memory#token-buffer)

_Token Buffer_

Returns previous consecutive messages until adding an additional message would cause the total history size to be larger than the Max Tokens. The default number of Max Tokens is 2048 and can be changed by right-clicking the Chat Memory node and clicking "Details".

![](https://docs.vectorshift.ai/~gitbook/image?url=https%3A%2F%2F2337131889-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252F8TCaopv9gy4bGub1g4jr%252Fuploads%252FZ74md7hJgvtn7bVjodrB%252FScreenshot%25202024-01-14%2520at%25205.35.54%25E2%2580%25AFPM.png%3Falt%3Dmedia%26token%3D897091b3-e6dc-4abf-b091-3e83665874a5&width=768&dpr=4&quality=100&sign=3df0b97&sv=1)

## 

[](https://docs.vectorshift.ai/vectorshift/platform/pipelines/chat/chat-memory#using-the-chat-memory-node)

**Using the Chat memory node**

The chat memory node doesn't have any inputs but has one output. The output is usually connected to the prompt field of a LLM node or a text node. Essentially, the chat memory takes the text in historical conversations and feeds it back into a prompt for a LLM. Hence, chatbots often have this structure:

1. Within the prompt (either in the LLM node or in a text node), we create a variable that the chat memory node can be connected to (in the below example, it is called "{{History}}". Then we label the variable as "Conversation History" so the LLM can understand.
    
2. As a result, when the pipeline is run, the LLM will get all the information it needs to answer based on what the user wants (input block), relevant data (from the Knowledge base node), and conversation history (from the chat memory node).



# Amazon DynamoDB

Serverless, NoSQL, fully managed database with single-digit millisecond performance at any scale


# PostgreSQL: The World's Most Advanced Open Source Relational Database
PostgreSQL is a powerful, open source object-relational database system with over 35 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

There is a wealth of information to be found describing how to [install](https://www.postgresql.org/download/) and [use](https://www.postgresql.org/docs/) PostgreSQL through the [official documentation](https://www.postgresql.org/docs/). The [open source community](https://www.postgresql.org/community/) provides many helpful places to become familiar with PostgreSQL, discover how it works, and find career opportunities. Learn more on how to [engage with the community](https://www.postgresql.org/community/).

# [Connect PostgreSQL to your chatbot](https://www.csml.dev/studio/integrations/postgresql/)

## Connect with a PostgreSQL database from your CSML Chatbot

---

With this PostgreSQL integration, you can easily perform read and write queries on your PostgreSQL database directly from your chatbot.

To get started, you need a publicly-accessible PostgreSQL database. All recent versions of PostgreSQL should be compatible with this integration.

## [](https://www.csml.dev/studio/integrations/postgresql/#setup)

## Setup

To configure this integration, provide your database connection settings in the environment variables of this App. You will need the host, port, user, password and database name.

## [](https://www.csml.dev/studio/integrations/postgresql/#usage)


