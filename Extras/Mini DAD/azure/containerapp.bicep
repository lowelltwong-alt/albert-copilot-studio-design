@description('Name of an existing Container Apps environment in the deployment resource group')
param managedEnvironmentName string
param containerAppName string = 'digital-assets-mcp'
param image string
param storageAccountName string
@secure()
param storageAccountKey string
param fileShareName string = 'digital-assets-state'
param allowedHost string
param allowedOrigin string
@secure()
param readerApiKey string
@secure()
param intakeApiKey string

resource managedEnvironment 'Microsoft.App/managedEnvironments@2023-05-01' existing = {
  name: managedEnvironmentName
}

resource stateStorage 'Microsoft.App/managedEnvironments/storages@2023-05-01' = {
  parent: managedEnvironment
  name: '${containerAppName}-state'
  properties: {
    azureFile: {
      accountName: storageAccountName
      accountKey: storageAccountKey
      shareName: fileShareName
      accessMode: 'ReadWrite'
    }
  }
}

resource app 'Microsoft.App/containerApps@2023-05-01' = {
  name: containerAppName
  location: managedEnvironment.location
  properties: {
    managedEnvironmentId: managedEnvironment.id
    configuration: {
      secrets: [
        { name: 'reader-api-key'; value: readerApiKey }
        { name: 'intake-api-key'; value: intakeApiKey }
      ]
      ingress: {
        external: true
        targetPort: 8765
        transport: 'http'
        allowInsecure: false
        traffic: [{ weight: 100; latestRevision: true }]
      }
    }
    template: {
      containers: [{
        name: 'digital-assets-mcp'
        image: image
        resources: { cpu: 0.5; memory: '1Gi' }
        env: [
          { name: 'ALBERT_API_KEY'; secretRef: 'reader-api-key' }
          { name: 'ALBERT_INTAKE_API_KEY'; secretRef: 'intake-api-key' }
          { name: 'ALBERT_ALLOWED_HOSTS'; value: allowedHost }
          { name: 'ALBERT_ALLOWED_ORIGINS'; value: allowedOrigin }
          { name: 'ALBERT_LESSON_INTAKE_ENABLED'; value: 'true' }
          { name: 'ALBERT_LESSON_REVIEW_ENABLED'; value: 'false' }
          { name: 'ALBERT_BIND_HOST'; value: '0.0.0.0' }
          { name: 'ALBERT_BIND_PORT'; value: '8765' }
        ]
        volumeMounts: [{ volumeName: 'state'; mountPath: '/app/state' }]
      }]
      volumes: [{ name: 'state'; storageType: 'AzureFile'; storageName: stateStorage.name }]
      scale: { minReplicas: 1; maxReplicas: 2 }
    }
  }
}

output appName string = app.name
