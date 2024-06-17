# Advanced Apache Pinot - Guide & Exercises

The following set of exercises aims to guide you through learning and mastering the various aspects of Apache Pinot.
For the most effective and structured learning experience, it's recommended to approach the exercises in the following order:

## 01 - Cluster Creation

In this first exercise, you'll learn how to create an Apache Pinot cluster using Docker Compose - a tool for defining and managing multi-container Docker applications.

*Keep in Mind* : Ensure Docker is installed and running on your machine before starting.

## 02 - Table Addition

This exercise introduces you to setting up schemas and creating tables in Apache Pinot.

*Keep in Mind* : A good schema design can lead to efficient storage and query performance.

## 03 - Batch Data Ingestion

Here, you'll delve into the process of ingesting data into offline tables in Apache Pinot.

*Keep in Mind* : Batch ingestion is suitable when you don't need data to be available immediately.

## 04 - Stream Data Ingestion

Experience how data ingestion into realtime tables works in this exercise. This is crucial for use cases that require immediate availability of data.

*Keep in Mind* : Proper setup of streaming sources is key for successful real-time ingestion.

## 05 - Querying

Learn about various types of queries supported by Apache Pinot.
This will be helpful for data extraction and analysis.

*Keep in Mind* : Understanding the right queries to use can help optimize your data analysis.

## 06 - Index Creation

Explore several types of index creation in Apache Pinot.
Indexing can help improve the speed and performance of your database.

*Keep in Mind* : Indexing requires considerations around your query patterns and storage costs.

## 07 - Data Transformation

This exercise walks you through the use of data transformation functions in Apache Pinot, allowing you to change the format, structure, or values of data.

*Keep in Mind* : Data transformations can be used for data cleaning or to prepare data for analysis.

## 08 - Upserts

Acquaint yourself with the Upsert operation in Apache Pinot.
Upsert can be used to insert rows into a table, and if the row already exists, it updates the row instead.

*Keep in Mind* : The upsert operation can be a powerful tool for keeping your data up to date.

## 09 - Minion Usage

Understand some options and features for Minion usage in Apache Pinot.
Minions help in handling heavy computation tasks in the cluster.

*Keep in Mind* : Correctly configuring Minion tasks can further enhance your cluster operation.

## 10 - Tenant Creation

Finally, you'll learn about the process of creating tenants in Apache Pinot.
Multi-tenancy allows for effective resource isolation and management in a shared cluster.

*Keep in Mind* : Appropriate tenant configuration is a cornerstone of managing resources in a shared Pinot cluster.
