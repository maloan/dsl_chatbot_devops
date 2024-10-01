````python
class UniversityChatbot:
    def __init__(self):
        self.faq = {
            "admission": "Admission starts in September.",
            "courses": "We offer courses in Computer Science, Engineering, and Business.",
            "library hours": "The library is open from 9 AM to 8 PM."
        }

    def get_response(self, query):
        return self.faq.get(query.lower(), "Sorry, I don't have an answer for that.")
````

