# Relationship

Relationship gives the information about how resources are connected together.

This will be helpful to view how the target system is inter-connected

There are four types of relationships

- runsOn
- connectedTo
- dependsOn
- componentOf

Use any of the four relationships based on the connection type.

Relationship payload contains three attributes

1. type : Relationship Type
2. sourceId : Source Resource MOID
3. targetId : Target Resource MOID

### Sample JSON Message

```json
[
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
    ]
```
