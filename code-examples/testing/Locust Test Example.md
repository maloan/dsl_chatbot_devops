```python
from locust import HttpUser, task

class ChatbotUser(HttpUser):
    @task
    def send_message(self):
        self.client.post("/api/messages", json={"message": "Hello"})
```