# Relationship payload

```json
{
    "messageId":"43b4802e-3c05-4473-bf67-6c1f573b88b3",
    "messageVersion":"2.0.0",
    "id":"43b4802e-3c05-4473-bf67-6c1f573b88b3",
    "profile":"f0338f2d-4a46-4dcf-a8f0-5befdc17e07f",
    "gateway":"ad3d80bd-fa8a-48f7-aad0-e73deaa40479",
    "collector":"GATEWAY",
    "app":"sample-sdk-app",
    "appId" : "52a47c79-be3f-48bb-bc5a-165baf5225c8",
    "configId": "da939b7f-cd92-4454-a010-c22ce5c6c69c",
    "module":"",
    "type":"RELATIONSHIP",
    "subType":"RELATIONSHIP",
    "action":"CREATE",
    "payload":[
        {
            "type" : "runsOn",
            "sourceId" : "56d371b6-e2a9-40ae-b5dd-e7979b432c93",
            "targetId" : "8bea235f-fc37-4a6f-b7cd-100393e279af"
        },
        {
            "type" : "connectedTo",
            "sourceId" : "56d371b6-e2a9-40ae-b5dd-e7979b432c93",
            "targetId" : "735ab798-e9b4-474c-aa03-de9fb6a6e0f5"
        },
        {
            "type" : "dependsOn",
            "sourceId" : "735ab798-e9b4-474c-aa03-de9fb6a6e0f5",
            "targetId" : "c91b3cae-9873-4734-bfff-e23d2b1477c6"
        },
        {
            "type" : "componentOf",
            "sourceId" : "2b920550-f084-4fa3-b6bc-6cb4c663993c",
            "targetId" : "8beb384b-7c2b-49a8-a7ba-c6f213af586d"
        }
    ],
    "timestamp":"2020-12-08T10:30:15+0000"
}
```
