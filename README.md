# API Data Ingestion to DynamoDB

This repository contains a project designed for ingesting data from an API and storing it in AWS DynamoDB. The project uses Python along with the Boto3 library to facilitate interactions with the AWS DynamoDB service.


## Overview

The API Data Ingestion to DynamoDB project aims to automate the process of retrieving data from a specified API and storing it into a DynamoDB table. This is useful for scenarios where data needs to be continuously or periodically collected from an API and stored in a NoSQL database for further processing or analysis.

## Architecture

The project consists of:
- **API Client**: A Python script that makes HTTP requests to the API.
- **Data Processor**: A Python script that processes and formats the data.
- **DynamoDB Interface**: Python code using the Boto3 library to interact with AWS DynamoDB for data storage.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- **Python**: Version 3.6 or higher
- **Boto3**: The AWS SDK for Python
- **AWS Credentials**: Properly configured AWS credentials with permissions to access DynamoDB

You can install Boto3 using pip:

```bash
pip install boto3


## Usage

- **Run the API Client**: Execute the API client script to retrieve data from the API.

  ```bash
  python api_client.py
