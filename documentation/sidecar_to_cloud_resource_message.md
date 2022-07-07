# Resource Payload

```json
{
    "messageId":"43b4802e-3c05-4473-bf67-6c1f573b88b3",
    "messageVersion":"2.0.0",
    "profile":"f0338f2d-4a46-4dcf-a8f0-5befdc17e07f",
    "gateway":"ad3d80bd-fa8a-48f7-aad0-e73deaa40479",
    "collector":"GATEWAY",
    "app":"sample-sdk-app",
    "appId" : "52a47c79-be3f-48bb-bc5a-165baf5225c8",
    "configId": "da939b7f-cd92-4454-a010-c22ce5c6c69c",
    "module":"",
    "type":"RESOURCE",
    "subType":"RESOURCE",
    "action":"POST",
    "payload": {
        "resourceType": "server",
        "moId": "a0594f2e-3b26-2acf-b9e0-4a9fdc42a1a0",
        "resourceName" : "server-1234",
        "hostName" : "server-1234-hostname",
        "aliasName": "CustomName",
        "dnsName": "testdevice-api.com",
        "ipAddress" : "172.200.25.12",
        "alternateIpAddress" : "10.10.0.1",
        "macAddress" : "2E:8B:EB:32:7A:F9",
        "os" : "ubuntu 20.04 lts",
        "nativeType" : "Dell NAS",
        "make" : "dell, inc.",
        "model" : "model-xyz",
        "serialNumber" : "123456",
        "tags" : {
            "firmware" : "fireware-1",
            "bios" : "bios-1"
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
    },
    "timestamp":"2020-12-08T10:30:15+0000"
}
```
