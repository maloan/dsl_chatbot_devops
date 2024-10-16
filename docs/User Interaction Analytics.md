---
created: 2024-10-14 15:19
updated: 2024-10-14 15:19
---
# [Mixpanel](https://docs.mixpanel.com/docs/what-is-mixpanel)
# What is Mixpanel?

Mixpanel will help you better understand your customers and answer questions about your product. It enables you to track how users engage with your product and analyze this data with interactive reports that let you query and visualize the results with just a few clicks.

Mixpanel is built on three key concepts: [**Events**](https://docs.mixpanel.com/docs/what-is-mixpanel#events), [**Users**](https://docs.mixpanel.com/docs/what-is-mixpanel#users), and [**Properties**](https://docs.mixpanel.com/docs/what-is-mixpanel#properties).

  

## Concepts[](https://docs.mixpanel.com/docs/what-is-mixpanel#concepts)

Before you get started, you should know three Mixpanel concepts:

- **Events** are actions that happen in your product
- **Users** are the people who use your product
- **Properties** are the attributes of your users and events

### Events[](https://docs.mixpanel.com/docs/what-is-mixpanel#events)

An event is a data point that represents an interaction between a user and your product. Events can be a wide range of interactions.

Imagine you run a cafe where customers can purchase a coffee via an app. Each purchase is an event that can be tracked in Mixpanel.

![image](https://docs.mixpanel.com/_next/static/media/event-1.8ee874fe.svg)

### Users[](https://docs.mixpanel.com/docs/what-is-mixpanel#users)

On the other side of an event is a user — the specific individual who completed an interaction with your product.

Each user has a unique identifier that you can use to track their activity. This identifier can be an email address, a username, or a unique ID. Mixpanel uses a unique ID to identify users.

![image](https://docs.mixpanel.com/_next/static/media/events-and-users.bafc63dc.svg)

### Properties[](https://docs.mixpanel.com/docs/what-is-mixpanel#properties)

You can track additional information about **users** and **events**. These details are called **properties**.

An **Event Property** describes an event. For a coffee purchase, the event would be _Purchased Item_ and the event properties could be _type_ (in this case a Coffee) and _price_ (in this case $2.50).

![image](https://docs.mixpanel.com/_next/static/media/event.c66d7b09.svg)

A **User Property** describes a User. This could be their name, email, age, etc.

![image](https://docs.mixpanel.com/_next/static/media/user-profile.08673eed.svg)

Properties allow you to create groups of users (aka [cohorts](https://docs.mixpanel.com/docs/users/cohorts)) and also enable you to filter for certain events or users. These powerful features make it easy to identify trends and new customer insights.