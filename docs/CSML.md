---
created: 2024-10-16 09:41
updated: 2024-10-16 09:41
---
# CSML

What is CSML?

CSML (Conversational Standard Meta Language) is an **Open-Source,** **Domain-Specific Language** designed for **developing rich conversational experiences easily**. It makes creating powerful chatbots extremely easy.

Written itself in Rust, the purpose of this language is to simplify the creation and maintenance of rich conversational interactions between humans and machines. With a very expressive and text-only syntax, CSML flows are easy to write and understand, making it easy to deploy and maintain conversational agents.

CSML natively handles short and long-term memory slots, metadata injection, and connecting to any third party API or injecting arbitrary code in any programming language thanks to its powerful runtime APIs.

By using the CSML language, any developer can integrate arbitrarily complex conversational agents on any channel (Facebook Messenger, Slack, Facebook Workplace, Microsoft Teams, custom webapp, ...) and make any bot available to any end user. In addition to the language itself, [CSML Studio](https://studio.csml.dev), an online, full-featured development and deployment platform, comes with a large number of channel integrations that work out of the box, but developers are free to add new custom integrations by using the CSML interfaces.

https://bluexp.netapp.com/blog/azure-anf-blg-azure-database-pricing-sql-database-mysql-cosmosdb-and-more
## Pricing Plans

All our plans allow full access to CSML Studio, the most powerful CSML development environment, including hundreds of connectors to the most popular apps and APIs.

#### Free

For small chatbots  
and independent developers

Free

- 2,000 conversation requests
- Up to 5 installed apps
- 1 deployed free channel
- NLP with Dialogflow, Amazon Lex, MS Luis
- Community Support

[Get Started](https://studio.csml.dev)

30 days free trial of CSML Studio Pro

#### Pro

For agencies and professional  
chatbot developers

$20 /month

- 10,000 conversation requests*
- NLP & Livechat integration
- Unlimited team members
- Unlimited apps
- 5 deployed pro channels
- Custom webapp channel branding
- Broadcasts
- Email Support

[Get Started](https://studio.csml.dev)

30 days free trial

#### Enterprise

For enterprise chatbots  
with bespoke requirements

starting at $1500 /month

- 50,000 conversation requests*
- Unlimited channels
- Enterprise SLA
- SAMLv2 SSO
- On-Premise or Private Cloud
- Custom development services
- Private Integrations
- Team roles management
- Custom analytics
- Security audit reports
- Dedicated Support

# Introduction

**CSML (Conversational Standard Meta Language) is an open-source programming language dedicated to building chatbots**.

It acts as a linguistic/syntactic abstraction layer, designed for humans who want to let other humans interact with any machine, in any setting. The syntax is designed to be learned in a matter of minutes, but also scales to any complexity of chatbot.

CSML handles seamlessy and automatically **short and long-term memory** slots, **metadata** injection, and can be plugged in with any external system by means of [**channel integrations**](https://docs.csml.dev/studio/channels/introduction) or [**custom APIs**](https://docs.csml.dev/studio/api/introduction), as well as consume scripts **in any programming languages** using built-in parallelized runtimes.

To learn more about CSML, you can read this [article](https://medium.com/clevyio/announcing-csml-a-new-open-source-language-to-easily-build-full-featured-chatbots-3787e43ab707).

## 

[](https://docs.csml.dev/studio#build-your-chatbot-with-csml-studio)

Build your chatbot with CSML Studio

The easiest way to develop CSML chatbots is by using the [CSML development studio](https://studio.csml.dev/), using a sample bot available in your library or by creating your own.

Each bot gives you a full access to the CSML framework - a set of specialized tools to make and customize your chatbots : code editor, chatbox, apps, functions and files library, analytics and channels.

![](https://docs.csml.dev/~gitbook/image?url=https%3A%2F%2F2862118938-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M6OZMoZlXP9VSWYMW_T%252F-Mfmvx0-cs1b-KXocNid%252F-Mfwh7H9MANVDUG_2l-W%252Fimage.png%3Falt%3Dmedia%26token%3D236a94b4-1616-4db7-9313-0fcfecfeb5c9&width=768&dpr=4&quality=100&sign=447852a6&sv=1)

Some of the Chatbot Templates available in CSML Studio

## 

[](https://docs.csml.dev/studio#create-your-own-conversational-experiences)

**Create your own conversational experiences**

You can create your own conversations by modifying an existing flow or [creating your own](https://docs.csml.dev/studio/getting-started/create-your-first-bot).

A flow is a CSML file which contains several steps to be followed during a conversation with a user. The first instructions have to be placed in the start step, then you can move from a step to the next one using `goto stepname`, and finish the current conversation using `goto end`. Each step contains instructions on how to handle the interactions within the step: what to say, what to remember, where to go...

For the bot to say a sentence, you just need to use the keyword `say` followed by the [type of message](https://docs.csml.dev/language/sending-receiving-messages) you want to send.The keyword `say` allows:

- to display a message: text, questions, urls, components (image, video, audio, buttons…)
    
- to simulate behaviors, such as waiting time (Wait) or message composition (Typing)
    

## 

[](https://docs.csml.dev/studio#manage-interactions)

**Manage interactions**

Like a human, a chatbot is supposed to understand and react to messages sent by the user.

In a conversational logic, CSML allows the chatbot to wait for a user answer using the keyword `hold`, and interpret the expected user input (called `event`) to trigger an action.

Here is an example of a simple interaction where the bot is asking if the user likes guitar and waiting for two specific answers in order to trigger actions.

![](https://docs.csml.dev/~gitbook/image?url=https%3A%2F%2F2862118938-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M6OZMoZlXP9VSWYMW_T%252F-MbL6xOPZFNfhluIe1Si%252F-MbLEsLfPHhAK-smpYyJ%252FCleanShot%25202021-06-04%2520at%252010.34.57.gif%3Falt%3Dmedia%26token%3D7cd1e08c-147f-40dd-b67b-f91118d2258e&width=768&dpr=4&quality=100&sign=e2e2303&sv=1)

## 

[](https://docs.csml.dev/studio#memory-and-local-variables)

**Memory and local variables**

[Memory](https://docs.csml.dev/language/memory) is essential in the CSML logic. When two people are chatting, they constantly memorize and update information to be reused in future discussions. CSML provides two types of variables: local variables, with a very short life cycle, and persistent variables, called memories.

The memories are assigned as followed use the keyword `remember` and can be reused in every step or in a future conversation, while the local variables are executed within one step, assigned with the `use` keyword.

You can output any variable into a string value with the double curly braces.

## 

[](https://docs.csml.dev/studio#connect-apps-and-execute-your-own-functions)

**Connect apps and execute your own functions**

You can select an existing integration in the apps library or add your own function coded in any language. Find a few examples in our [GitHub repository](https://github.com/CSML-by-Clevy) and how to use functions in our [documentation.](https://docs.csml.dev/#custom-code-execution)

Once your function is uploaded, you can test it and call it in a CSML flow. [Read more about functions and apps here](https://docs.csml.dev/studio/getting-started/using-csml-apps)!

## 

[](https://docs.csml.dev/studio#deploy-your-chatbot)

**Deploy your chatbot**

Once your chatbot is ready to chat with your users, you can select the channel you want to connect on. For example, using the [CSML Studio](https://studio.csml.dev) you can connect your bots to Slack, Messenger, Whatsapp and other channels, or use the [CSML Client API](https://docs.csml.dev/studio/api/api-reference/chat-api) to receive requests.

