# Overview

- [Setup](#setup)
- [Prepare Domain model json](#prepare-domain-model-json)
- [Generate code from domain json](#generate-code-from-domain-json)
- [Fill target stubs](#fill-target-stubs)
- [Building project](#building-project)
- [Publishing app](#publishing-app)
- [Installing app](#installing-app)
- [Add configuration](#add-configuration)
- [Resource discovery and monitoring reports](#resource-discovery-and-monitoring-reports)
- [Debugging logs](#debugging-logs)


## Setup

**Setup pycharam** <br>

1. Make sure python with version 3.8 and above is installed
2. Download **pycharam** community version from this link https://www.jetbrains.com/pycharm/download/#section=linux <br>
3. The file pycharm*.tar.gz will be downloaded, extract this file <br>
4. Go to bin folder in the extracted folder and run **sh pycharam.sh** <br>
5. pycharam editor will be open and ready to use <br>

**Install virtual environment** <br>

```shell
python3 -m pip install --user virtualenv
```

## Prepare Domain model json

```json
{
  "appName": "dell-brightclustermanager",
  "appVersion": "1.0.0",
  "discoveryConfiguration": [
    {
      "propertyName": "dellBCMIP",
      "label": "Dell BCM Manager IP Address",
      "dataType": "string"
    },
    {
      "propertyName": "managerCredentials",
      "label": "Dell BCM Manager Credentials",
      "dataType": "string",
      "credentialType": "SSH",
      "placeholder": "Select Credentials"
    },
    {
      "propertyName": "appFailureNotifications",
      "label": "App Failure Notifications",
      "dataType": "boolean"
    }
  ],
  "required": [
    "dellBCMIP",
    "managerCredentials"
  ],
  "data": {
    "appFailureNotifications": false
  },
  "nativeTypeMapping": [
    {
      "nativeType": "Dell BrightCluster Manager",
      "opsrampResourceType": "Cluster"
    },
    {
      "nativeType": "Dell BCM Head Node",
      "opsrampResourceType": "Server"
    },
    {
      "nativeType": "Dell BCM Virtual Node",
      "opsrampResourceType": "Server"
    },
    {
      "nativeType": "Dell BCM Physical Node",
      "opsrampResourceType": "Server"
    },
    {
      "nativeType": "Dell BCM Switch",
      "opsrampResourceType": "Switch"
    },
    {
      "nativeType": "Dell BCM PDU",
      "opsrampResourceType": "Power"
    }
  ],
  "nativeType": [
    {
      "name": "Dell BrightCluster Manager",
      "metric": [],
      "monitors": [
        {
          "title": "Dell BrightCluster Manager Monitor",
          "frequency": 30,
          "metric": []
        }
      ]
    },
    {
      "name": "Dell BCM Head Node",
      "metric": [
        {
          "name": "dell_bcm_headNode_healthStatus",
          "units": "",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${component.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Component: ${component.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": "NONE",
            "value": "0",
            "repeat": 1
          },
          "critical": {
            "operator": "NOT_EQUAL",
            "value": "0",
            "repeat": 1
          },
          "availability": true,
          "graphPoint": true,
          "raiseAlert": true,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false,
          "dataPointConverisonOptions": [
            {
              "pass": "0"
            },
            {
              "fail": "1"
            }
          ]
        },
        {
          "name": "dell_bcm_headNode_blockedProcesses",
          "units": "count",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_headNode_systemCpuTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_headNode_cpuWaitTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        }
      ],
      "monitors": [
        {
          "title": "Dell BCM HeadNode Health Status Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_headNode_healthStatus"
          ]
        },
        {
          "title": "Dell BCM HeadNode Performance Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_headNode_blockedProcesses",
            "dell_bcm_headNode_systemCpuTime",
            "dell_bcm_headNode_cpuWaitTime"
          ]
        }
      ]
    },
    {
      "name": "Dell BCM Virtual Node",
      "metric": [
        {
          "name": "dell_bcm_virtualNode_healthStatus",
          "units": "",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${component.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Component: ${component.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": "NONE",
            "value": "0",
            "repeat": 1
          },
          "critical": {
            "operator": "NOT_EQUAL",
            "value": "0",
            "repeat": 1
          },
          "availability": true,
          "graphPoint": true,
          "raiseAlert": true,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false,
          "dataPointConverisonOptions": [
            {
              "pass": "0"
            },
            {
              "fail": "1"
            }
          ]
        },
        {
          "name": "dell_bcm_virtualNode_blockedProcesses",
          "units": "count",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_virtualNode_systemCpuTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_virtualNode_cpuWaitTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        }
      ],
      "monitors": [
        {
          "title": "Dell BCM VirtualNode Health Status Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_virtualNode_healthStatus"
          ]
        },
        {
          "title": "Dell BCM VirtualNode Performance Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_virtualNode_blockedProcesses",
            "dell_bcm_virtualNode_systemCpuTime",
            "dell_bcm_virtualNode_cpuWaitTime"
          ]
        }
      ]
    },
    {
      "name": "Dell BCM Physical Node",
      "metric": [
        {
          "name": "dell_bcm_physicalNode_healthStatus",
          "units": "",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${component.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Component: ${component.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": "NONE",
            "value": "0",
            "repeat": 1
          },
          "critical": {
            "operator": "NOT_EQUAL",
            "value": "0",
            "repeat": 1
          },
          "availability": true,
          "graphPoint": true,
          "raiseAlert": true,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false,
          "dataPointConverisonOptions": [
            {
              "pass": "0"
            },
            {
              "fail": "1"
            }
          ]
        },
        {
          "name": "dell_bcm_physicalNode_blockedProcesses",
          "units": "count",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_physicalNode_systemCpuTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        },
        {
          "name": "dell_bcm_physicalNode_cpuWaitTime",
          "units": "Jiffies",
          "alertOn": "STATIC",
          "factor": 1,
          "dataPoint": "Gauge",
          "alertSummary": "${severity} - Resource: ${resource.name} - ${metric.value} (${threshold})",
          "alertDescription": "${severity} - ${component.name}, Resource name: ${resource.name}, IP Address: ${resource.ip}, Metric Name: ${metric.name}, Severity: ${severity}, Value: ${metric.value}, Reason: ${metric.value} (${threshold})",
          "warning": {
            "operator": ">=",
            "value": "10",
            "repeat": 1
          },
          "critical": {
            "operator": ">=",
            "value": "20",
            "repeat": 1
          },
          "availability": false,
          "graphPoint": true,
          "raiseAlert": false,
          "formatPlottedValue": true,
          "formatGraph": false,
          "formatAlert": false
        }
      ],
      "monitors": [
        {
          "title": "Dell BCM PhysicalNode Health Status Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_physicalNode_healthStatus"
          ]
        },
        {
          "title": "Dell BCM PhysicalNode Performance Monitor",
          "frequency": 15,
          "metric": [
            "dell_bcm_physicalNode_blockedProcesses",
            "dell_bcm_physicalNode_systemCpuTime",
            "dell_bcm_physicalNode_cpuWaitTime"
          ]
        }
      ]
    },
    {
      "name": "Dell BCM Switch",
      "metric": [],
      "monitors": [
        {
          "title": "Dell BCM Switch Monitor",
          "frequency": 30,
          "metric": []
        }
      ]
    },
    {
      "name": "Dell BCM PDU",
      "metric": [],
      "monitors": [
        {
          "title": "Dell BCM PDU Monitor",
          "frequency": 30,
          "metric": []
        }
      ]
    }
  ]
}

```

## Generate code from domain json

Once the domain.json file is done, than we need to generate code to build the App, follow the below steps

- Clone the sdk-app-starter project in local environment[https://github.com/opsramp/sdk2.0/tree/main/projects/sdk-app-starter]
- Replace the above domain.json file in python folder present in the above project 
- Execute this command coming to sdk-app-starter project: **python3 app.py destination-folder-path python**
- An App will be created with the destination-folder-path
- Once app created successfully, than open the project in pycharm
  
  ![pycharam editor](https://github.com/opsramp/sdk2.0/blob/9af5decfb70dbe9a27e2b5f4ce1ecfaafb83aa7e/images/bcm-pycharm-editor.png)
  
- Open a terminal pointing app folder
- create virtual environment python3 -m venv env
- source env/bin/activate
- Run **gunicorn --bind 0.0.0.0:25000 app:app** make sure App is running locally

Code generator generates below artifacts

- App skeleton code
- Manifest
- Helm chart
- Docker file
- Make file


## Fill target stubs

App developer need to fill the stubs by following below steps

1. Talking to target
2. Process target data
3. Return data back with opsramp domain model


## Building project

Run the below make file from the project folder

```shell
sh make.sh
```

Running this command will execute the following steps in sequence
- Building python code
- Building docker image
- Pushing docker image to repo
- Pushing helm chart to repo

Make file log

```shell
(venv) demouser@abc123:~/dell-brightclustermanager$ sudo sh make.sh
sudo password for demouser:
Building dell-brightclustermanager docker image...!!
Sending build context to Docker daemon 41.52MB
Step 1/7 : FROM ubuntu:20.04
---> 20fffa419e3a
Step 2/7 : WORKDIR /app
---> Using cache
---> 2c2034d4c83c
Step 3/7 : RUN apt-get update && apt-get install -y python3-pip
---> Using cache
---> 7d441cf66925
Step 4/7 : COPY requirements.txt /app/requirements.txt
---> Using cache
---> ce7ab9f06e97
Step 5/7 : RUN pip install -r requirements.txt
---> Using cache
---> 4f32a1f590d8
Step 6/7 : COPY . /app
---> e0d96611fe28
Step 7/7 : CMD 25000", "app:app"
---> Running in 39362e2d91b4
Removing intermediate container 39362e2d91b4
---> 7d32a8f82af8
Successfully built 7d32a8f82af8
Successfully tagged us-docker.pkg.dev/gateway-images/gateway-cluster-images/dell-brightclustermanager:1.0.0
---------------------------------------------
Pushing dell-brightclustermanager docker image to repo!!
The push refers to repository us-docker.pkg.dev/gateway-images/gateway-cluster-images/dell-brightclustermanager
acf0a57f9cd5: Pushed
8a791b080d48: Layer already exists
86db6618cd96: Layer already exists
41387345cb29: Layer already exists
710841616aa3: Layer already exists
af7ed92504ae: Layer already exists
1.0.0: digest: sha256:e298480fde88f751b60078daff525ed2b990edc713b2609afc423289500f3dae size: 1579
---------------------------------------------
Saving dell-brightclustermanager helm chart
ref: us-docker.pkg.dev/gateway-images/gateway-cluster-charts/dell-brightclustermanager:1.0.0
digest: 421ae05cae991d4f594010275c5b432422c9d0b5f8d94f299504d74fe78af89d
size: 3.0 KiB
name: dell-brightclustermanager
version: 1.0.0
1.0.0: saved
---------------------------------------------
Pushing dell-brightclustermanager helm chart to repo
The push refers to repository us-docker.pkg.dev/gateway-images/gateway-cluster-charts/dell-brightclustermanager
ref: us-docker.pkg.dev/gateway-images/gateway-cluster-charts/dell-brightclustermanager:1.0.0
digest: 31040b014b29f21471dee57f2120d59a5c1b5a30fd7e626363a2f153bf384927
size: 3.0 KiB
name: dell-brightclustermanager
version: 1.0.0
1.0.0: pushed to remote (1 layer, 3.0 KiB total)
---------------------------------------------
```

## Publishing app

Publishing App requries following data

1. Client id
2. Client OAuth2.0 token
3. Manifest.json  

Follow the APIs in the [link](https://github.com/opsramp/sdk2.0/blob/41574c5f5a0edad7000054950e6b0372842dd37b/documentation/app_publish_rest_calls.md) 
to publish the App

## Installing app

Once app is published, login to cloud portal and check whether app is available in the manage apps list

Login to cloud portal
1. Select -->Partner-->Client
2. Go to Setup-->Integrations and Apps
3. Click on Manage Apps button to see list of Apps
4. The published App should be seen like below

![Install App](https://github.com/opsramp/sdk2.0/blob/8ffd5ad6acb135050872d8c875ebae90035e57a4/images/install-bright-cluster-manager.png)

5. Select the gateway to install the App
![Select Gateway](https://github.com/opsramp/sdk2.0/blob/c810cb26cf62248573f0889d7d33379dc765f1c3/images/gateway-install-bcm-app.png)

## Add configuration

Add the target configuration details for the App to discover and monitor the resources

![Add configuration](https://github.com/opsramp/sdk2.0/blob/5868e0009ef0c5e749c61a70b959e073465e80d2/images/add-configuration-bcm.png)

## Resource discovery and monitoring reports

Cluster discovery

![Cluster discovery](https://github.com/opsramp/sdk2.0/blob/1f0f005750e2a1d35eed764f4972b2fc9d335cf4/images/bcm-cluster-discovery.png)

Components in the Cluster node

![Components in the Cluster node](https://github.com/opsramp/sdk2.0/blob/c630491c9f48f1a89bc118810398c4479b2718ac/images/bcm-components-in-cluster.png)

BCM Head Node Attributes

![BCM Head Node Attributes](https://github.com/opsramp/sdk2.0/blob/888e7d1f2c51899dd38618d7afdc500fd6d626c2/images/bcm-head-node-attributes.png)

Applied Monitors

![Applied Monitors](https://github.com/opsramp/sdk2.0/blob/main/images/bcm-applied-monitors.png)

Metrics

![Metrics](https://github.com/opsramp/sdk2.0/blob/main/images/bcm-metrics.png)

## Debugging logs

Login to gateway

Check whether app is running or not using kubectl get pods command

```shell
sudo kubectl get pods
```

![kubectl get pods](https://github.com/opsramp/sdk2.0/blob/1e9bbdd154fa26d7c3d52e5cfa88ff7e04b03e14/images/bcm-kubectl-get-pods.png)

Check Sidecar logs

```shell
sudo kubectl logs -f dell-brightclustermanager-7b54d77fbd-9vb2j -c dell-brightclustermanager-sidecar
```

![Sidecar logs](https://github.com/opsramp/sdk2.0/blob/1e9bbdd154fa26d7c3d52e5cfa88ff7e04b03e14/images/bcm-sidecar-logs.png)

Check App logs

```shell
sudo kubectl logs -f dell-brightclustermanager-7b54d77fbd-9vb2j -c dell-brightclustermanager-app
```

![App logs](https://github.com/opsramp/sdk2.0/blob/main/images/bcm-app-logs.png)






















