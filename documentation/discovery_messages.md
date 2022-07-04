# Discovery messages

## Discovery configuration update

<details><summary>Sequence Diagram</summary>

 ![alt text](https://github.com/opsramp/sdk2.0/blob/145def16b0b657edc66590c3450dde124b9669e8/images/discovery_configuration_update.png)
</details>

<details><summary>Message</summary>

```json
{
  "messageId": "e92fbcce-91a1-4a90-97dd-f90be627cdc9",
  "messageVersion": "2.0.0",
  "appIntegrationId": "INTG-c7afb76c-a74e-4c40-bfab-3bffd5223a2f",
  "managementProfileId": "9d3f3eec-28f9-4696-9b8b-1d801692e036",
  "gateway": "9d3f3eec-28f9-4696-9b8b-1d801692e036",
  "module": "Discovery",
  "subtype": "Configuration",
  "app": "mock-vcenter-tested",
  "action": "Update",
  "configurationId": "ADAPTER-MANIFEST-65a5e123-65ad-41bc-8247-e8b12b11c09c",
  "configurationName": "vCenterTest1",
  "payload": {
    "data": {
      "port": "45000",
      "ipAddress": "172.25.252.193",
      "vcenterName": "vcenter1",
      "protocol": "http",
      "credentialId": [
        "6tAMNkXh5mSgVKUUVyNyTeWv"
      ]
    },
    "nativeTypes": {
      "vm": {
        "resourceType": "Server"
      },
      "host": {
        "resourceType": "Server"
      }
    }
  },
  "requireAck": false,
  "sha": "b87430a5051dec140907ead5a7a0c4bd0ef6a15e104d1300c0e00d58c3a720a6"
}

```
</details>

---

## Discovery configuration delete

<details><summary>Sequence Diagram</summary>

![alt text](https://github.com/opsramp/sdk2.0/blob/145def16b0b657edc66590c3450dde124b9669e8/images/discovery_configuration_delete.png)

</details>

<details><summary>Message</summary>

```json
{
  "messageId": "461e8c70-fae6-4178-a085-d4097d98b862",
  "messageVersion": "2.0.0",
  "appIntegrationId": "INTG-e195bc0d-1bd7-4392-b87a-86a2d5304a04",
  "managementProfileId": "9d3f3eec-28f9-4696-9b8b-1d801692e036",
  "gateway": "9d3f3eec-28f9-4696-9b8b-1d801692e036",
  "module": "Discovery",
  "subtype": "Configuration",
  "app": "mock-vcenter-tested",
  "action": "Delete",
  "configurationId": "ADAPTER-MANIFEST-3c53e214-49fd-4755-85fe-883e6d6a0bfe",
  "configurationName": "vCenterTest",
  "payload": {
    "data": {
      "port": "45000",
      "protocol": "http",
      "ipAddress": "172.25.252.193",
      "vcenterName": "vcenter1",
      "credentialId": [
        "6tAMNkXh5mSgVKUUVyNyTeWv"
      ]
    },
    "nativeTypes": {
      "vm": {
        "resourceType": "Server"
      },
      "host": {
        "resourceType": "Server"
      }
    }
  },
  "requireAck": false
}

```
</details>

