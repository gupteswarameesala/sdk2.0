# App lifecycle

## Install App

<details><summary>Sequence Diagram</summary>

  ![alt text](https://github.com/opsramp/sdk2.0/blob/145def16b0b657edc66590c3450dde124b9669e8/images/app_install_flow.png)

</details>

<details><summary>Message</summary>

```json
{
  "messageId": "5a578452-bfd6-4614-8d79-bda3bb0adfa9",
  "messageVersion": "2.0.0",
  "appIntegrationId": "0bc95e12-ac99-427b-bf48-2235f198d970",
  "referenceId": "dc8abeaf-fd1f-44e0-b3ee-1142d277b040",
  "app": "AppController",
  "module": "App",
  "subtype": "Core",
  "action": "Install",
  "managementProfileId": "b4a64f28-e531-455e-b0ea-d5c853b4078a",
  "payload": {
    "app": "sample-sdk-app",
    "version": "1.0.0",
    "helm": {
      "pullType": "chart",
      "url": null,
      "credentials": {
        "username": null,
        "password": null,
        "token": null
      }
    },
    "maven": {
      "url": null
    }
  }
}

```
</details>

---

## Upgrade App

<details><summary>Sequence Diagram</summary>
  
![alt text](https://github.com/opsramp/sdk2.0/blob/145def16b0b657edc66590c3450dde124b9669e8/images/app_upgrade_flow.png)

</details>

<details><summary>Message</summary>

```json
{
  "messageId": "3cff7fd9-a629-4c25-954b-7cc7611ca6ab",
  "messageVersion": "2.0.0",
  "appIntegrationId": "0bc95e12-ac99-427b-bf48-2235f198d970",
  "referenceId": "cce5d149-d09e-42b8-9b0a-b4da951cce59",
  "app": "AppController",
  "module": "App",
  "subtype": "Core",
  "action": "Update",
  "managementProfileId": "b4a64f28-e531-455e-b0ea-d5c853b4078a",
  "payload": {
    "app": "sample-sdk-app",
    "version": "1.1.0",
    "helm": {
      "pullType": "chart",
      "url": null,
      "credentials": {
        "username": null,
        "password": null,
        "token": null
      }
    },
    "maven": {
      "url": null
    }
  }
}

```
</details>

---

## Uninstall App

<details><summary>Sequence Diagram</summary>
  
  ![alt text](https://github.com/opsramp/sdk2.0/blob/145def16b0b657edc66590c3450dde124b9669e8/images/app_uninstall_flow.png)

</details>

<details><summary>Message</summary>

```json
{
  "messageId": "b660d3ba-8f23-4f10-92ac-753fc5253e9e",
  "messageVersion": "2.0.0",
  "appIntegrationId": "0bc95e12-ac99-427b-bf48-2235f198d970",
  "referenceId": "2cc4cd9e-dde4-48e9-8936-77d553da1526",
  "app": "AppController",
  "module": "App",
  "subtype": "Core",
  "action": "Uninstall",
  "managementProfileId": "b4a64f28-e531-455e-b0ea-d5c853b4078a",
  "payload": {
    "app": "sample-sdk-app"
  }
}

```
</details>

