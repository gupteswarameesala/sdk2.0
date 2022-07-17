# Rest calls exposed by Side car

- [Publish Resources](#publish-resources) 
- [Publish Relationships](#publish-relationships)
- [Publish Metrics](#publish-metrics)
- [Post Acknowledgement](#post-acknowledgement)
- [Post Alert](#post-alert)
- [Post App Event](#post-app-event)

## Publish Resources

```yaml
- METHOD: PUT
  URL: /api/v2/resources
  CONTENT-TYPE: application/json
  BODY:
    - resourceType: server
      nativeType: host
      moId: vcenter2@host1
      resourceName: vcenter2host1
      hostName: vcenter2host1
      ipAddress: 177.22.151.207
    - resourceType: server
      nativeType: host
      moId: vcenter2@host2
      resourceName: vcenter2host2
      hostName: vcenter2host2
      ipAddress: 221.93.10.194
  RESPONSE: 
    - status_code: 200
```

## Publish Relationships
```yaml
- METHOD: PUT
  URL: /api/v2/relationships
  CONTENT-TYPE: application/json
  BODY:
    - type: componentOf
      sourceId: vcenter2@host1
      targetId: vcenter2@host1@vm1
    - type: componentOf
      sourceId: vcenter2@host1
      targetId: vcenter2@host1@vm2
    - type: componentOf
      sourceId: vcenter2@host2
      targetId: vcenter2@host2@vm1
    - type: componentOf
      sourceId: vcenter2@host2
      targetId: vcenter2@host2@vm2

  RESPONSE: 
    - status_code: 200
```
## Publish Metrics
```yaml
- METHOD: POST
  URL: /api/v2/metrics?process=true
  CONTENT-TYPE: application/json
  BODY:
    - resourceId: dc791d58-c94e-4060-8688-c0dd5578ec61
      resourceType: host
      templateId: ff4666b5-dbe5-4dd7-9079-9c10cdc8893d
      monitorId: 1d7258c0-c4b3-4be5-8733-e5466388ff53
      data:
      - metricName: dell_ashok_host_system_cpu_usage_utilization
        instanceVal: '25.922893704949633'
        ts: '1657186200'
      - metricName: dell_ashok_host_system_memory_usage_utilization
        instanceVal: '68.72716025995211'
        ts: '1657186200'
      - metricName: dell_ashok_host_system_cpu_load
        instanceVal: '16.26574818653396'
        ts: '1657186200'
      - metricName: dell_ashok_host_system_disk_usage_freespace
        instanceVal: '37.99532105684557'
        ts: '1657186200'
      - metricName: dell_ashok_host_system_disk_usage_usedspace
        instanceVal: '0.35550107530404884'
        ts: '1657186200'
      - metricName: dell_ashok_host_system_memory_usage_usedspace
        instanceVal: '1.1485607914230256'
        ts: '1657186200'
      - metricName: dell_ashok_host_system_os_uptime
        instanceVal: '10.514033091814024'
        ts: '1657186200'
      - metricName: dell_ashok_host_system_network_interface_utilization
        instanceVal: '29.496634937144872'
        ts: '1657186200'
      - metricName: dell_ashok_host_system_cpu_usage_stats
        instanceVal: '32.66075477065075'
        ts: '1657186200'
      - metricName: dell_ashok_host_system_process_stats_count
        instanceVal: '29.50087874467676'
        ts: '1657186200'

  RESPONSE: 
    - status_code: 200
```

## Post Acknowledgement
```yaml
- method: PUT
  url: "/api/v2/messages/{AM-Message-Id}?processInventory=true
  response: 
    - status_code: 200
```

## Post Alert

```yaml
- METHOD: POST
  URL: /api/v2/messages/outbound_channel/publish
  CONTENT-TYPE: application/json
  BODY:
    version: 1.0.0
    id: f92e909a-288b-4a17-bb55-1c4db3486925
    app: sample-app-python-basic
    appId: INTG-e990c1f9-fb8e-436b-849c-fc772608a49f
    configId: ADAPTER-MANIFEST-3bd5fdf2-26ba-419e-b713-62963cda7abe
    module: ''
    type: ALERT
    subType: ''
    action: POST
    payload:
      resourceId: resourceId
      alertType: Monitoring
      serviceName: metricName
      subject: sample app target event processed as alert
      description: sample app target event processed as alert
      currentState: Critical
      alertTime: '1658067360'
  RESPONSE: 
        - status_code: 200
```

## Post App Event

```yaml
- METHOD: POST
  URL: /api/v2/messages/outbound_channel/publish
  CONTENT-TYPE: application/json
  BODY:
    version: 1.0.0
    id: f92e909a-288b-4a17-bb55-1c4db3486925
    profile: 4cd8aebf-7e46-4b23-8dac-2e107f1b8caa
    gateway: 4cd8aebf-7e46-4b23-8dac-2e107f1b8caa
    app: sample-app-python-basic
    collector: GATEWAY
    appId: INTG-e990c1f9-fb8e-436b-849c-fc772608a49f
    configId: ADAPTER-MANIFEST-3bd5fdf2-26ba-419e-b713-62963cda7abe
    type: LOG
    action: POST
    payload:
      message: Discovery completed successfully
      statusCode: '200'
      logLevel: INFO
    timestamp: '1658067360'
  RESPONSE: 
        - status_code: 200
```

