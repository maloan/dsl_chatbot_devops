```yaml
name: Chatbot CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install Dependencies
      run: pip install -r requirements.txt

    - name: Run Unit Tests
      run: pytest

    - name: Build Docker Image
      run: docker build -t chatbot-app .

    - name: Push Docker Image
      run: docker push <your-repo>/chatbot-app

    - name: Deploy to Azure (Optional)
      uses: azure/webapps-deploy@v2
      with:
        app-name: '<azure-app-name>'
        publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
```
