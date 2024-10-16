```yaml
trigger:
  branches:
    include:
      - main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.x'
    addToPath: true

- script: |
    pip install -r requirements.txt
    pytest
  displayName: 'Install dependencies and run unit tests'

- task: Docker@2
  inputs:
    containerRegistry: '<your-container-registry>'
    repository: '<your-repo>/chatbot-app'
    command: 'buildAndPush'
    dockerfile: '**/Dockerfile'
    tags: |
      $(Build.BuildId)

- task: AzureWebApp@1
  inputs:
    azureSubscription: '<azure-subscription>'
    appName: '<azure-app-name>'
    package: '$(System.DefaultWorkingDirectory)/_docker_build_output.zip'
```