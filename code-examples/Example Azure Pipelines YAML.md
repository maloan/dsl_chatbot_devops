```yaml
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UseDotNet@2
  inputs:
    packageType: 'sdk'
    version: '5.x'
    installationPath: $(Agent.ToolsDirectory)/dotnet

- script: |
    dotnet restore
    dotnet build --configuration Release
    dotnet test --configuration Release --no-build
  displayName: 'Build and Test'

- task: PublishBuildArtifacts@1
  inputs:
    PathtoPublish: '$(Build.ArtifactStagingDirectory)'
    ArtifactName: 'drop'
    publishLocation: 'Container'

- task: AzureWebApp@1
  inputs:
    azureSubscription: 'Azure Subscription'
    appName: 'my-webapp'
    package: $(Build.ArtifactStagingDirectory)/drop
```