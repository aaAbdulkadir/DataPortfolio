# CoinMarketCap Cryptocurrency Monitoring

An automated data pipeline which consists of using Terraform, Docker, Airflow, Spark, Azure and PowerBI.

## Overview

### Objective 

This project consists of working with batch data to create a dashboard for monitoring crypto currencies on a daily basis. The data will be collected from CoinMarketCap (a crypto currency website) and transformations will be applied to have the data ready for monitoring via a dashboard.


### Technologies and Architecture


- Terraform
  - Create the Azure infrastructure using code
- Azure
  - Deploy resources and specifically a VM to host the pipeline to run on
- Docker
  - Hosts Airflow via docker-compose and all the dependencies needed for Spark and Python via Dockerfile
- Apache Airflow
  - The pipeline governing the process of moving data
- Apache Spark
  - Transforming the data
- PowerBI
  - Visualise the data


![image](https://user-images.githubusercontent.com/72317571/189979496-bd6b6c8c-4819-40a7-9cc6-f9c36b276c35.png)

### Final Result

![image](https://user-images.githubusercontent.com/72317571/189973524-320d0fee-0c44-4ef9-b519-23627ab3971a.png)

## Methodology

### Prerequisites

Before starting the project, the following must be installed or created:

- Azure
  - An account with a subscription
  - [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- Terraform
  - [Download](https://learn.hashicorp.com/tutorials/terraform/install-cli)

### Project Walkthrough

The first step in this project is to create an Infrastructure using terraform i.e. the resources needed on Azure. In this case, the resources that are created are a resource group with a storage account, blob storage and a virtual machine with all its dependencies. The IaC can be seen [here](https://github.com/aaAbdulkadir/Data-Science/blob/main/ZoomCamp/Project/Terraform/main.tf). 

Once the infrastructure is written, it can be deployed by firstly logging into the Azure CLI through the terminal:

```bash
az login
```

This redirects to the browser to log into your Azure account. Once logged in, the IaC needs to be initialised, which can be done as follows:

```bash
terraform init
```

This initialises a working directory containing Terraform configuration files.

```bash
terraform plan -out main.tfplan
```

This creates a Terraform plan which can then be pushed to create the plan on Azure using the following:


```bash
terraform apply main.tfplan
```

![image](https://user-images.githubusercontent.com/72317571/189697582-990fe968-aa22-485f-8a25-5a518e250050.png)

![image](https://user-images.githubusercontent.com/72317571/189698064-8edef73e-8b20-4a24-b959-e128df25a08b.png)

![image](https://user-images.githubusercontent.com/72317571/189697958-9b2aa7ae-63f4-4bf4-b86d-3f8b64b06a64.png)

![image](https://user-images.githubusercontent.com/72317571/189716955-38a48a20-c817-400f-a6e6-4136516d303f.png)


![image](https://user-images.githubusercontent.com/72317571/189716741-68f5f195-1e81-4163-be8b-327ef8964d7f.png)


![image](https://user-images.githubusercontent.com/72317571/189702901-3091cf92-c6e5-4aba-9f5d-cc606417b543.png)





automation

![image](https://user-images.githubusercontent.com/72317571/189703825-c54b2e5e-3771-45b8-aeeb-1c1f7f84163d.png)
