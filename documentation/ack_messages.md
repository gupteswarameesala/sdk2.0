# Ack messages

## Resource Ack message

<details><summary>Sequence Diagram</summary>

 ![alt text](https://github.com/opsramp/sdk2.0/blob/6b46f9381348e10b49e6e391b493db6d0a340a65/images/resource_ack_message.png)
</details>

<details><summary>Message</summary>

```json
{
  "messageId": "cadc2215-ebcd-11ec-8fd4-a1704ebc7e62",
  "messageVersion": "2.0.0",
  "type": "RESOURCE",
  "action": "ACK",
  "collector": "GATEWAY",
  "subtype": "RESOURCE",
  "module": "App",
  "app": "sdkapp-vcenters-code-gen",
  "configId": "ADAPTER-MANIFEST-b0a54565-c558-45bb-8a6d-741070c1ba3b",
  "appId": "INTG-d6e1d6bd-4d88-40a9-87d3-10b3c95beaaa",
  "profile": "826a496a-67b2-4b52-bd5c-dcacf9ee9db5",
  "gateway": "826a496a-67b2-4b52-bd5c-dcacf9ee9db5",
  "payload": [
    {
      "resourceUUID": "b508610e-1e0d-405a-9822-4d1fc492b78b",
      "tenantID": "62a73da6-7239-4ef0-8141-82ce3e5a481c",
      "moId": "vcenter3@host1"
    },
    {
      "resourceUUID": "4024f075-c3a1-49bd-a707-d84e48466fe1",
      "tenantID": "62a73da6-7239-4ef0-8141-82ce3e5a481c",
      "moId": "vcenter3@host2"
    }
  ],
  "timestamp": "Tue Jun 14 10:36:04 GMT 2022"
}
```
</details>

---

## Relationship ack message

<details><summary>Sequence Diagram</summary>

![alt text](https://github.com/opsramp/sdk2.0/blob/6b46f9381348e10b49e6e391b493db6d0a340a65/images/relationship_ack_message.png)

</details>

<details><summary>Message</summary>

```json
{
  "messageId": "cadc2215-ebcd-11ec-8fd4-a1704ebc7e62",
  "messageVersion": "2.0.0",
  "profile": "826a496a-67b2-4b52-bd5c-dcacf9ee9db5",
  "gateway": "826a496a-67b2-4b52-bd5c-dcacf9ee9db5",
  "collector": "GATEWAY",
  "app": "sdkapp-vcenters-code-gen",
  "appId": "INTG-d6e1d6bd-4d88-40a9-87d3-10b3c95beaaa",
  "configId": "ADAPTER-MANIFEST-b0a54565-c558-45bb-8a6d-741070c1ba3b",
  "module": "App",
  "type": "RELATIONSHIP",
  "subtype": "RELATIONSHIP",
  "action": "ACK",
  "payload": [
    {
      "type": "componentOf",
      "sourceMoId": "vcenter3@host1",
      "targetMoId": "vcenter3@host1@vm1"
    },
    {
      "type": "componentOf",
      "sourceMoId": "vcenter3@host1",
      "targetMoId": "vcenter3@host1@vm2"
    },
    {
      "type": "componentOf",
      "sourceMoId": "vcenter3@host2",
      "targetMoId": "vcenter3@host2@vm1"
    },
    {
      "type": "componentOf",
      "sourceMoId": "vcenter3@host2",
      "targetMoId": "vcenter3@host2@vm2"
    }
  ],
  "timestamp": "2022-06-14T10:36:14.957Z"
}

```
</details>

