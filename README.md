# AppSync Serverless Framework Sample App

## Description

This is the sample codes building AppSync with Serverless Framework.

You can build the application that you can ...

- build AppSync service
- understand how to use Lambda Resolver
- call GraphQL API

## Requirements

- node.js
- AWS CLI
- python 3.8
- Serverless Framework 1.6 >=

## Building

This is the step of building the app from your local.

### set up AWS account

- sign up AWS
- create AWS IAM user for building app and get access key and secret access key
  - Administration role is required becourse of CloudFormation

### set environment vars

- set below vars to environment vars
  - AWS access key
  - AWS secret access key
  - AWS default region

- If you use Windows, you can use set_env.bat.example
  - rename it to set_env.bat and edit it

### set configurations

- sls_configuration/config/common.yml
  - edit and set below vars
    - ACCOUNT_ID : AWS Account ID

### install required softwares and libs

- install required softwares
  - serverless framework
    ```
    npm install -g serverless
    ```
  - aws cli
    - ref: `https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/install-cliv2-windows.html`
- install plugins of servereless framework
  - node modules
    ```
    npm install serverless-appsync-plugin
    ```
  - ref: `https://www.npmjs.com/package/serverless-appsync-plugin`

### build app at local and deploy to AWS

- deploy serverless app
  ```
  sls deploy
  ```

## Reference
- Serverless Framework : https://serverless.com/
- serverless-appsync-plugin : https://www.npmjs.com/package/serverless-appsync-plugin
- AWS : https://aws.amazon.com/
