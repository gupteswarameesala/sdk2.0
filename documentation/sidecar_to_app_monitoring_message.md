# Monitoring message

<details><summary>Activity Diagram</summary>
  
 ![alt text](https://github.com/opsramp/sdk2.0/blob/9fba0395b1237b8fb8667160a63c7706db1bc311/images/monitoring_message_processing.png)
  
</details>

<details><summary>Message</summary>
  
```json
{
  "action": "Update",
  "app": "power-flex-dell",
  "appIntegrationI\nd": "INTG-86032f6a-78f3-4620-8460-3466a41aa247",
  "appVersion": "1.0.0",
  "configurationId": "ADAPTER-MANIFEST-80ee8f1a-26b5-43e5-af62-2e50edc8d070",
  "mess\nageId": "ba623a75-e9ad-45d0-8142-476afd4195ec",
  "messageVersion": "2.0.0",
  "module": "Monitoring",
  "payload": {
    "appConfig": {
      "data": {
        "alertConfiguration\n": "false",
        "credential": [
          {
            "credentialId": "tTn2gSZkKzN2kUS4CaTjAKuT",
            "credentialValue": {
              "data": {
                "cipher": "jIim958AQbRgM1TWDq+DrKrb3w441+eJ0u/hbI/uA\nHFfBXFLz57MLiGiYeFtsPXpUfVT7unEEPdRFdmzqw7QepPMRwhm+e6qxOwo9ZrOKIk36mjlB0Tv",
                "classId": "credential.cipher",
                "key1": "181c2af1a4c",
                "\ntype": "APPLICATION",
                "uuid": "tTn2gSZkKzN2kUS4CaTjAKuT",
                "ver": 2
              }
            },
            "fieldName": "credentials"
          }
        ],
        "credentialId": [
          {
            "fieldName": "credentials",
            "value": "tTn2gSZkKzN2kUS4CaTjAKuT"
          }
        ],
        "ipAddress": "10.60.89.132",
        "notificationAlert": "false",
        "protocol": "true"
      },
      "nativeTypes": {
        "Dell PowerFlex System": {
          "resourceType": "Storage"
        }
      }
    },
    "monitorId": "f852100d-c00b-4a96-85e0-c5f31908b196",
    "nativeType": {
      "Dell PowerFlex System": [
        "dell_powerflex_event_Statis\ntics"
      ]
    },
    "resources": [
      {
        "appConfigId": "ADAPTER-MANIFEST-80ee8f1a-26b5-43e5-af62-2e50edc8d070",
        "credential": [],
        "credentialId": [],
        "moId": "08a9c0c351\n862e0f",
        "resourceId": "e0a884dc-0c56-426a-b853-40adeb697053",
        "signature": "to be filled",
        "templateCustomization": {},
        "templates": [
          {
            "app": "power-fle\nx-dell",
            "nativeType": "Dell PowerFlex System",
            "templateId": "27dcc66a-a273-4fc5-8852-d6acaad97d03"
          }
        ]
      }
    ],
    "templateId": "27dcc66a-a273-4fc5-8852-d6acaad9\n7d03"
  },
  "subtype": "Configuration"
}
```
  
 </details>
