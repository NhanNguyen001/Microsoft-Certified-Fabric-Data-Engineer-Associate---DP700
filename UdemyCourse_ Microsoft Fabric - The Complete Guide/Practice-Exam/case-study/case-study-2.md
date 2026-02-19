# Case Study 2

## Overview

### Company Overview

Contoso, Ltd. is an online retail company that wants to modernize its analytics platform by moving to Fabric. The company plans to begin using Fabric for marketing analytics.

### IT Structure

- The company's IT department has a team of **data analysts** and a team of **data engineers** that use analytics systems.
- The data engineers perform the ingestion, transformation, and loading of data. They prefer to use **Python or SQL** to transform the data.
- The data analysts query data and create semantic models and reports. They are qualified to write queries in **Power Query** and **T-SQL**.

---

## Existing Environment

### Fabric

- Contoso has an **F64** capacity named **Cap1**. All Fabric users are allowed to create items.
- Contoso has two workspaces named **WorkspaceA** and **WorkspaceB** that currently use **Pro license mode**.

### Source Systems

- Contoso has a point of sale (POS) system named **POS1** that uses an instance of **SQL Server on Azure Virtual Machines** in the same Microsoft Entra tenant as Fabric. The host virtual machine is on a **private virtual network** that has **public access blocked**.
- POS1 contains all the sales transactions that were processed on the company's website.
- The company has a software as a service (SaaS) online marketing app named **MAR1**. MAR1 has **seven entities**. The entities contain data that relates to email open rates and interaction rates, as well as website interactions. The data can be exported from MAR1 by calling **REST APIs**. Each entity has a different endpoint.
- Contoso has been using MAR1 for one year. Data from prior years is stored in **Parquet files** in an **Amazon Simple Storage Service (Amazon S3)** bucket. There are **12 files** that range in size from **300 MB to 900 MB** and relate to email interactions.

### Product Data

- POS1 contains a product list and related data. The data comes from the following three tables:
  - **Products**
  - **ProductCategories**
  - **ProductSubcategories**
- In the data, products are related to product subcategories, and subcategories are related to product categories.

### Azure

- Contoso has a Microsoft Entra tenant that has the following mail-enabled security groups:
  - **DataAnalysts**: Contains the data analysts
  - **DataEngineers**: Contains the data engineers
- Contoso has an Azure subscription.
- The company has an existing **Azure DevOps** organization and creates a new project for repositories that relate to Fabric.

### User Problems

- The VP of marketing at Contoso requires analysis on the effectiveness of different types of email content. It typically takes a **week** to manually compile and analyze the data. Contoso wants to reduce the time to **less than one day** by using Fabric.
- The data engineering team has successfully exported data from MAR1. The team experiences **transient connectivity errors**, which causes the data exports to fail.

---

## Requirements

### Planned Changes

- Contoso plans to create the following two lakehouses:
  - **Lakehouse1**: Will store both raw and cleansed data from the sources
  - **Lakehouse2**: Will serve data in a dimensional model to users for analytical queries
- Additional items will be added to facilitate data ingestion and transformation.
- Contoso plans to use **Azure Repos** for source control in Fabric.

### Technical Requirements

- The new lakehouses must follow a **medallion architecture** by using the following three layers: **bronze**, **silver**, and **gold**.
- There will be extensive data cleansing required to populate the MAR1 data in the silver layer, including **deduplication**, the **handling of missing values**, and the **standardizing of capitalization**.
- Each layer must be fully populated before moving on to the next layer.
- If any step in populating the lakehouses fails, an **email must be sent** to the data engineers.
- Data imports must run **simultaneously**, when possible.
- The use of email data from the Amazon S3 bucket must meet the following requirements:
  - **Minimize egress costs** associated with cross-cloud data access.
  - **Prevent saving a copy** of the raw data in the lakehouses.
- Items that relate to data ingestion must meet the following requirements:
  - The items must be **source controlled** alongside other workspace items.
  - Ingested data must land in the bronze layer of Lakehouse1 in the **Delta format**.
  - **No changes** other than changes to the file formats must be implemented before the data lands in the bronze layer.
  - Development effort must be **minimized** and a **built-in connection** must be used to import the source data.
  - In the event of a connectivity error, the ingestion processes must **attempt the connection again**.
- Lakehouses, data pipelines, and notebooks must be stored in **WorkspaceA**.
- Semantic models, reports, and dataflows must be stored in **WorkspaceB**.
- Once a week, old files that are no longer referenced by a Delta table log must be **removed**.

### Data Transformation

- In the POS1 product data, **ProductID** values are unique.
- The product dimension in the gold layer must include only **active products** from product list. Active products are identified by an **IsActive** value of **1**.
- Some product categories and subcategories are **NOT** assigned to any product. They are **NOT** analytically relevant and must be **omitted** from the product dimension in the gold layer.

### Data Security

Security in Fabric must meet the following requirements:

- The data engineers must have **read and write access** to all the lakehouses, including the underlying files.
- The data analysts must only have **read access** to the Delta tables in the gold layer.
- The data analysts must **NOT** have access to the data in the bronze and silver layers.
- The data engineers must be able to **commit changes** to source control in WorkspaceA.
