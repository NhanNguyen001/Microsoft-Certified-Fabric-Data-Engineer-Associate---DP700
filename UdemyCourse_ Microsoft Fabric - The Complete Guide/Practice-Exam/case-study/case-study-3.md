# Case Study 3

---

## Overview

Litware, Inc. is a publishing company that has an online bookstore and several retail bookstores worldwide. Litware also manages an online advertising business for the authors it represents.

---

## Existing Environment

### Fabric Environment

- Litware has a Fabric workspace named **Workspace1**. High concurrency is enabled for Workspace1.
- The company has a data engineering team that uses **Python** for data processing.

### Data Processing

- The retail bookstores send sales data at the end of each business day, while the online bookstore constantly provides logs and sales data to a central enterprise resource planning (ERP) system.
- Litware implements a **medallion architecture** by using the following three layers: **bronze**, **silver**, and **gold**.
- The sales data is ingested from the ERP system as **Parquet files** that land in the **Files** folder in a lakehouse.
- Notebooks are used to transform the files in a Delta table for the bronze and silver layers.
- The gold layer is in a **warehouse** that has **V-Order disabled**.
- Litware has image files of book covers in **Azure Blob Storage**. The files are loaded into the Files folder.

### Sales Data

- Month-end sales data is processed on the first calendar day of each month. Data that is older than one month never changes.
- In the source system, the sales data refreshes every six hours starting at midnight each day.
- The sales data is captured in a **Dataflow Gen2** dataflow.
- When the dataflow runs, new and historical data is captured. The dataflow captures the following fields of the source:
  - Sales Date
  - Author
  - Price
  - Units
  - SKU
- A table named **AuthorSales** stores the sales data that relates to each author. The table contains a column named **AuthorEmail**. Authors authenticate to a guest Fabric tenant by using their email address.

### Security Groups

Litware has the following security groups:
- **Sales**
- **Fabric Admins**
- **Streaming Admins**

### Performance Issues

- Business users perform ad-hoc queries against the warehouse. The business users indicate that reports against the warehouse sometimes run for **two hours** and fail to load as expected.
- Upon further investigation, the data engineering team receives the following error message when the reports fail to load: *"The SQL query failed while running."*
- The data engineering team wants to debug the issue and find queries that cause more than one failure.
- When the authors have new book releases, there is often an increase in sales activity. This increase slows the data ingestion process.
- The company's sales team reports that during the last month, the sales data has **NOT** been up-to-date when they arrive at work in the morning.

---

## Requirements

### Planned Changes

- Litware recently signed a contract to receive book reviews. The provider of the reviews exposes the data in **Amazon Simple Storage Service (Amazon S3)** buckets.
- Litware plans to manage **Search Engine Optimization (SEO)** for the authors. The SEO data will be streamed from a REST API.

### Version Control

- Litware plans to implement a version control solution in Fabric that will use **GitHub integration** and follow the **principle of least privilege**.

### Governance Requirements

- To control data platform costs, the data platform must use **only Fabric services and items**.
- Additional Azure resources must **NOT** be provisioned.

### Data Requirements

Litware identifies the following data requirements:
- Process the SEO data in **near-real-time (NRT)**.
- Make the book reviews available in the lakehouse **without making a copy of the data**.
- When a new book cover image arrives in the Files folder, process the image **as soon as possible**.
