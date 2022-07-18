# Content covered as part of Day 1

<details><summary> Basics </summary>
  
- [Resource](#resource) 
- [Resource Type](#resource-type) 
- [Native Type](#native-type) 
- [Relationship](#realtionship) 
- [Metric](#metric) 
- [Monitor](#monitor)
- [Template](#template)
- [DMP](#dmp)
  
###### Resource

[details](https://github.com/opsramp/sdk2.0/blob/main/documentation/resource.md)
  
###### Resource Type
Equivalent name of the native type in opsramp

###### Native Type
Name of the resource type in target domain

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
  
Refer slides from 8-17 in the presentation

</details>

<details><summary> App Development </summary>
  
- [App development phases](#app-development-phases) 
- [Sample standalone app](#sample-standalone-app) 
- [App incoming message flow](#app-incoming-message-flow)
- [App outgoing message flow](#app-outgoing-message-flow)
- [Domain Json](#domain-json)
- [Sample app with code generator](#sample-app-with-code-generator)
- [Building App](#building-app)
- [Gateway setup](#gateway-setup)
- [Publishing App](#publishing-app)
- [Installing App](#installing-app)
- [Resource Discovery](#resource-discovery)
- [Manifest Json](#manifest-json)


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

Refer slides from 19-29 in the presentation

</details>
