terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
    }
  }
}

provider "azurerm" {
  features {}
}

# create resource group
resource "azurerm_resource_group" "terraform_rg" {
  name = "terraform_rg"
  location = "eastus"
}

# create storage account
resource "azurerm_storage_account" "terraformstrg1" {
  name                     = "terraformstrg1"
  resource_group_name      = azurerm_resource_group.terraform_rg.name
  location                 = azurerm_resource_group.terraform_rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

# create blob storage
resource "azurerm_storage_container" "terraformblob" {
  name                  = "terraformblob"
  storage_account_name  = azurerm_storage_account.terraformstrg1.name
  container_access_type = "private"
}

# create data lake storage gen2
resource "azurerm_storage_data_lake_gen2_filesystem" "terraformlake" {
  name               = "terraformlake"
  storage_account_id = azurerm_storage_account.terraformstrg1.id
}