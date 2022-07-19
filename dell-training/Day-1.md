# Day 1 Summary

<details><summary> Basics </summary>
  
- [Resource](#resource) 
- [Resource Type](#resource-type) 
- [Native Type](#native-type) 
- [Relationship](#relationship) 
- [Metric](#metric) 
- [Monitor](#monitor)
- [Template](#template)
- [DMP](#dmp)
  
###### Resource

[details](https://github.com/opsramp/sdk2.0/blob/main/documentation/resource.md)
  
###### Resource Type
Name of the type of resource in opsramp

###### Native Type
Name of the type of resource in target

###### Relationship
[details](https://github.com/opsramp/sdk2.0/blob/main/documentation/relationship.md)
  
###### Metric
- A metric capture a value pertaining to your system at specific point of time
- This contains Graph and Alert definition 

###### Monitor
Group of metrics with certain frequency
  
###### Template
Group of monitors

###### DMP
- A policy which will apply template on a resource automatically based on its filtering rules.
- This resides in cloud and continousely listens on the events of a resource and act accordingly <br />
  
Refer slides from 8-17 in the presentation [Link](https://github.com/opsramp/sdk2.0/blob/main/documentation/SDK%202.0%20-%20Dell%20Training%20Preso.pptx)

</details>

<details><summary> App Development </summary>
  
- [App development phases](#app-development-phases) 
- [Sample standalone app](#sample-standalone-app) 
- [App bootstrap](#app-bootstrap)
- [App incoming message flow](#app-incoming-message-flow)
- [App outgoing message flow to side car](#app-outgoing-message-flow-to-side-car)
- [Domain Json](#domain-json)
- [Manifest Json](#manifest-json)
- [Sample app with code generator](#sample-app-with-code-generator)
- [Building App](#building-app)
- [Gateway setup](#gateway-setup)
- [Publishing App](#publishing-app)
- [Installing App](#installing-app)
- [Resource Discovery](#resource-discovery)



###### App development phases
  
- Define
  - Domain model
  - Manifest
- Develop
  - Generate code
  - Fill stubs
  - Build
- Publish
  - Register App with Manifest
- Install
  - Install App
  - Configure target details
- Customize
  - Customize monitoring and Alert thresholds

Refer slides from 19-29 in the presentation [Link](https://github.com/opsramp/sdk2.0/blob/main/documentation/SDK%202.0%20-%20Dell%20Training%20Preso.pptx)

###### Sample standalone app

[Code](https://github.com/opsramp/sdk2.0/tree/main/projects/sample-app-python-basic)
  
###### App bootstrap
(App intialization flow)[https://github.com/opsramp/sdk2.0/blob/main/documentation/app_bootstrap.md)
  
###### App incoming message flow
- [Rest calls exposed by an app](https://github.com/opsramp/sdk2.0/blob/main/documentation/app_rest_calls.md)
- [Discovery message](https://github.com/opsramp/sdk2.0/blob/main/documentation/sidecar_to_app_discovery_message.md)
- [Monitoring message](https://github.com/opsramp/sdk2.0/blob/main/documentation/sidecar_to_app_monitoring_message.md)
- [Event message](https://github.com/opsramp/sdk2.0/blob/main/documentation/sidecar_to_app_event_message.md)
  
###### App outgoing message flow to side car
- [Rest calls expose by side car](https://github.com/opsramp/sdk2.0/blob/main/documentation/sidecar_rest_call.md)
- [Resource message](https://github.com/opsramp/sdk2.0/blob/main/documentation/app_to_sidecar_resource.md)
- [Relationship message](https://github.com/opsramp/sdk2.0/blob/main/documentation/app_to_sidecar_relationship.md)
- [Metric messsage](https://github.com/opsramp/sdk2.0/blob/main/documentation/app_to_sidecar_metric.md)
  
###### Domain Json
[domain.json](https://github.com/opsramp/sdk2.0/blob/main/documentation/sample-domain.json)
  
###### Manifest Json
[manifest.json](https://github.com/opsramp/sdk2.0/blob/main/documentation/sample-manifest.json)
  
###### Sample app with code generator
[Code](https://github.com/opsramp/sdk2.0/tree/main/projects/sample-app-python-code-generated)
  
###### Building App
[Make file](https://github.com/opsramp/sdk2.0/blob/main/projects/sample-app-python-code-generated/make.sh)
  
###### Gateway setup
[Setup through OVA](https://github.com/opsramp/sdk2.0/blob/main/documentation/gateway-setup.md)
[Setup up from scratch](https://github.com/opsramp/sdk2.0/blob/main/documentation/PA-SetupandDebugging-130722-0522-52.pdf)
  
###### Publishing App
[APIs](https://github.com/opsramp/sdk2.0/blob/main/documentation/app_publish_rest_calls.md)

Refer slides from 50 in the presentation [Link](https://github.com/opsramp/sdk2.0/blob/main/documentation/SDK%202.0%20-%20Dell%20Training%20Preso.pptx)
  
###### Installing App
Refer slides from 51 in the presentation [Link](https://github.com/opsramp/sdk2.0/blob/main/documentation/SDK%202.0%20-%20Dell%20Training%20Preso.pptx)
  
###### Resource Discovery

</details>
