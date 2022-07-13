# Resource messages

## Resource configuration update

<details><summary>Sequence Diagram</summary>

 ![alt text](https://github.com/opsramp/sdk2.0/blob/55a9b1c8959b44da3f93d2b3b933642122aee7a4/images/resource_configuration_update.png)
</details>

<details><summary>Message</summary>

```json
{
  "messageId": "9f9df5e7-1849-4c50-b78d-a075dad7ca25",
  "messageVersion": "2.0.0",
  "module": "Monitoring",
  "subtype": "Resource",
  "action": "Update",
  "managementProfileId": "9d3f3eec-28f9-4696-9b8b-1d801692e036",
  "payload": {
    "resources": {
      "resourceId": "cb17e82a-dc35-4334-8c46-7539ecef4f8f",
      "moId": "vcenter1@host1",
      "appConfigId": "ADAPTER-MANIFEST-65a5e123-65ad-41bc-8247-e8b12b11c09c",
      "signature": "to be filled",
      "templateCustomization": {},
      "credentialId": [],
      "templates": [
        {
          "templateId": "2ff1793f-edbc-426d-ada1-1cd30af71c55",
          "app": "mock-vcenter-tested",
          "nativeType": "host"
        }
      ]
    }
  }
}

```
</details>

---

## Resource configuration delete

<details><summary>Sequence Diagram</summary>

![alt text](https://github.com/opsramp/sdk2.0/blob/8ed6146eac803981ecabc6ddfeaeb408a0b1fcce/images/resource_configuration_delete.png)

</details>

<details><summary>Message</summary>

```json
{
  "messageId": "4d52ee94-78be-4574-bee0-245cade5398d",
  "messageVersion": "2.0.0",
  "app": "mock-vcenter-tested",
  "module": "Monitoring",
  "subtype": "Resource",
  "action": "Delete",
  "managementProfileId": "9d3f3eec-28f9-4696-9b8b-1d801692e036",
  "appConfigId": "ADAPTER-MANIFEST-3c53e214-49fd-4755-85fe-883e6d6a0bfe",
  "payload": {
    "resourceId": "cf9335ae-0e18-4c8b-89a0-b53915beb7c6"
  }
}

```
</details>

---

## Resource configuration unassign

<details><summary>Sequence Diagram</summary>

![alt text](https://github.com/opsramp/sdk2.0/blob/8ed6146eac803981ecabc6ddfeaeb408a0b1fcce/images/resource_configuration_unassign.png)

</details>

<details><summary>Message</summary>

```json
{
  "messageId": "c76339e8-b5d1-499e-9a45-54a17648c8a5",
  "messageVersion": "2.0.0",
  "module": "Monitoring",
  "subtype": "Resource",
  "action": "UnAssign",
  "managementProfileId": "9d3f3eec-28f9-4696-9b8b-1d801692e036",
  "payload": {
    "resources": {
      "resourceId": [
        "8a09ba6b-dc73-4076-be55-500430105025"
      ],
      "templateId": "2ff1793f-edbc-426d-ada1-1cd30af71c55",
      "app": "mock-vcenter-tested",
      "nativeType": "host",
      "appConfigId": "ADAPTER-MANIFEST-678227c7-0e12-4cac-b36c-6b640f708997"
    }
  }
}

```
</details>

