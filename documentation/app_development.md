# App development 

- [Domain Json](#domain-json) 
- [Code Generator](#custom-attributes)
- [Sample App Code]
- [Building App]
- [Publishing App]
- [Installing App]
- [Create Configuration]
- [App attributes](#app-attributes)
- [Signatures](#signatures)

[Sample JSON Message](#sample-json-message)

### Domain json

   These attributes are standard across domain

   mandatory attributes

    1. moId
    2. resourceType
    3. nativeType
    4. resourceName

   optional attributes[Generic domain attributes]

    1. hostName
    2. aliasName
    3. dnsName
    4. ipAddress
    5. alternateIpAddress
    6. macAddress
    7. os
    8. make
    9. model
    10. serialNumber
    11. systemUID
    12. hasRelationship

### Custom attributes

    Native attributes specific to that domain, tags is a json object, add key value to tags 

    1. tags

### App attributes
  
    Add any key of your choice and value as json object, anything specific to app for that resource can be injected here

    ```json
    *"{appName}" : {
            "key1" : "value1",  
            "key2" : "value2"
        }
    ```

### Signatures

    Signatures are the identities for a resource, used for resource reconcilation when a same resource is discovered from multiple apps.

    ```json
    "signatures" : [
              "172.200.25.12@@@2E:8B:EB:32:7A:F9",
              "server-1234-hostname@@@dell, inc.@@@model-xyz",
              "123456@@@testdevice-api.com@@@2E:8B:EB:32:7A:F9",
              "a0594f2e-3b26-2acf-b9e0-4a9fdc42a1a0"
        ]
    ```


### Sample JSON message
```json
{
  "resourceType": "server",
  "moId": "a0594f2e-3b26-2acf-b9e0-4a9fdc42a1a0",
  "resourceName": "server-1234",
  "hostName": "server-1234-hostname",
  "aliasName": "CustomName",
  "dnsName": "testdevice-api.com",
  "ipAddress": "172.200.25.12",
  "alternateIpAddress": "10.10.0.1",
  "macAddress": "2E:8B:EB:32:7A:F9",
  "os": "ubuntu 20.04 lts",
  "nativeType": "Dell NAS",
  "make": "dell, inc.",
  "model": "model-xyz",
  "serialNumber": "123456",
  "systemUID": "567891-900790-766678-66577-09861",
  "hasRelationship": true,
  "tags": {
    "firmware": "fireware-1",
    "bios": "bios-1"
  },
  "{appName}" : {
            "key1" : "value1",  
            "key2" : "value2"
        },
  "signatures" : [
              "172.200.25.12@@@2E:8B:EB:32:7A:F9",
              "server-1234-hostname@@@dell, inc.@@@model-xyz",
              "123456@@@testdevice-api.com@@@2E:8B:EB:32:7A:F9",
              "a0594f2e-3b26-2acf-b9e0-4a9fdc42a1a0"
        ]
}
```

![alt text](https://github.com/opsramp/sdk2.0/blob/main/images/resource_schema.png)

[Home](#resource)
