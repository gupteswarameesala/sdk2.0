
# Monitoring configuration update

<details><summary>Sequence Diagram</summary>

![alt text](https://github.com/opsramp/sdk2.0/blob/145def16b0b657edc66590c3450dde124b9669e8/images/monitoring_configuration_update.png)

</details>

<details><summary>Message</summary>

```json
{
  "messageId": "73f8ad5a-2619-443e-9034-0b8b80f08ab1",
  "messageVersion": "2.0.0",
  "app": "mock-vcenter-tested",
  "module": "Monitoring",
  "subtype": "Configuration",
  "action": "Update",
  "payload": {
    "templateId": "2ff1793f-edbc-426d-ada1-1cd30af71c55",
    "nativeType": "host",
    "monitors": {
      "Performance Monitor mock-vcenter-tested host ": {
        "name": "Performance Monitor mock-vcenter-tested host ",
        "uuid": "1cec604c-3362-438a-8f8d-adcb9d23b400",
        "frequency": 5,
        "metrics": {
          "system_cpu_usage_utilization": {
            "availibityMetric": true,
            "units": "%",
            "graph": {
              "graphPoint": true
            },
            "notification": {
              "raiseAlert": true,
              "alertOn": "Static",
              "warn": {
                "operator": "GREATER_THAN",
                "value": "50",
                "repeat": 1
              },
              "critical": {
                "operator": "GREATER_THAN",
                "value": "70",
                "repeat": 1
              }
            },
            "formatPlottedValue": false
          }
        }
      }
    },
    "templateCustomization": {
      "customComponentThresholds": []
    }
  }
}

```
</details>


# Monitoring configuration delete

<details><summary>Sequence Diagram</summary>

![alt text](https://github.com/opsramp/sdk2.0/blob/145def16b0b657edc66590c3450dde124b9669e8/images/monitoring_configuration_delete.png)

</details>

<details><summary>Message</summary>
</details>
