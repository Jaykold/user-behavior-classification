### Deployment to the cloud using Azure App Service

1. Install Azure CLI

Use this [link](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) to install it for your preferred operating system

2. Login to Azure CLI

```
az login
```

3. Create a Resource group or skip this step to use an existing Resource group

```
az group create --name <myResourceGroup> --location eastus
```

4. Create an App Service Plan

```
az appservice plan create --name <myAppServicePlan> --resource-group <myResourceGroup> --sku B1 --is-linux
```

5. Create the Web App

```
az webapp create --resource-group <myResourceGroup> --plan <myAppServicePlan> --name <myFlaskApp> --deployment-container-image-name <mydockerhubusername/myflaskapp:latest>
```

6. Deploy to Azure

```
az webapp up --name <myFlaskApp> --resource-group <myResourceGroup> --plan <myAppServicePlan> --location eastus
```

7. Get app URL

```
az webapp show --name <myFlaskApp> --resource-group <myResourceGroup> --query "defaultHostName"
```
