# Resource

Resource payload contains two types of attributes

1. standard attributes

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

2. custom attributes

    1. tags

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
  }
}
```
