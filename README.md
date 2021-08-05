# IoT Core + Kinesis + Elasticsearch

## Overview

The goal of this project is to deploy, using AWS CDK, a sample stack to analyze sensor data from *Distribution Power Transformers*. The best way to simulate these *power transformers* is to use [IoT Device Simulator](https://aws.amazon.com/solutions/implementations/iot-device-simulator/).

But you can use any code that can send messages to a Topic on AWS to simulate your devices. Include a sample client provided.

![IoT + Kinesis + Elasticsearch architecture](iot-kinesis-es-kibana.png "IoT Analytics")

## Components

- IoT Core: Role in the solution...

- Kinesis

- Lambda Functions

- DynamoDB

- S3

- Amazon Elasticsearch

- Amazon Cognito

- Kibana

## Kibana Dashboards

### Overview Dashboard

![Overview Dashboard](overview-dashboard.png "Overview Dashboard")

### Details Dashboard

![Details Dashboard](details-dashboard.png "Details Dashboard")

### Alarms/Anomaly Detection

Kibana + SNS

## TODO

[See](TODO.md)

