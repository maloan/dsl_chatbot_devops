````bash
# Dockerfile for containerizing a Python-based chatbot

# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the chatbot code to the container
COPY chatbot.py /app

# Install dependencies (if any)
# RUN pip install -r requirements.txt

# Command to run the chatbot
CMD ["python", "chatbot"]
````
