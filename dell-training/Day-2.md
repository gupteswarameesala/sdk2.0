# Day 2 Summary

- [App development phases](#app-development-phases)
- [App Anatomy](#app-anatomy) 
- [App Sidecar](#app-sidecar) 
- [Deploying vcenter simulator](#deploying-vcenter-simulator) 
- [Developing standalone stub code](#developing-standalone-stub-code) 
- [Request context](#request-context)
- [Powerflex domain analysis](#powerflex-domain-analysis)
- [Generating Powerflex App with code generator](#generating-powerflex-app-with-code-generator)
- [Deploying Gateway in local through docker desktop](#deploying-gateway-in-local-through-docker-desktop)

### App development phases

![App development phases](/images/app-development-phases.png)

### App Anatomy

![App Anatomy](/images/app-anatomy.png)
  
### App Sidecar

![App sidecar](/images/app-sidecar.png)

- Sidecar is a utlity to App
- Filters resources and relationships
- Resource and Relationships delta calculations
- Alerting
- Decrypting app credentials

### Deploying vcenter simulator
[Code](https://github.com/opsramp/sdk2.0/tree/main/projects/target_endpoint_pythonsdkapp_addedfourthAPI)

### Developing standalone stub code
[Code](https://github.com/opsramp/sdk2.0/tree/main/projects/sample-requestcontext)
  
### Request context

![Request context](images/request-context.png)

- Maintains the state data across resource types for a single discovery configuration request message
- It used to pass data from resource type to another resource type during discovery lifecycle 

### Powerflex domain analysis
[Json file](https://github.com/opsramp/sdk2.0/blob/main/documentation/domain-powerflex-da.json)
  
### Generating Powerflex App with code generator
[Code](https://github.com/opsramp/sdk2.0/tree/main/projects/powerflex-code-generated)

### Deploying Gateway in local through docker desktop
- Enable kubernetes in Docker desktop
- Download and install helm for windows
- set path variable
- Download Opsramp windows gateway collector binary
- Register gateway
