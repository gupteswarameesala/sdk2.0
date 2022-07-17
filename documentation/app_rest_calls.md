# Rest calls exposed by App

- [Liveness](#liveness) 
- [Readiness](#readiness)
- [Discovery message](#discovery-message)
- [Monitoring message](#monitoring-message)
- [Log Level](#log-level)
- [Debug App](#debug-app)

## Liveness

```yaml
- method: GET
  url: /api/v1/live
  response: 
    - status_code: 200
```

## Readiness
```yaml
- method: GET
  url: /api/v1/ready
  response: 
    - status_code: 200
```

## Discovery message
```yaml
- method: POST
  url: /api/v2/messages
  content-type: application/json
  body: 
    action: Update
    app: power-flex-dell
    appIntegrationId: INTG-86032f6a-78f3-4620-8460-3466a41aa247
    appVersion: 1.0.0
    configurationId: ADAPTER-MANIFEST-80ee8f1a-26b5-43e5-af62-2e50edc8d070
    configurationName: demo
    deployment: Image
    gateway: 900010b8-51a8-4541-929f-e054c80b6c41
    managementProfileId: 900010b8-51a8-4541-929f-e054c80b6c41
    messageId: 7c10a775-127c-4319-bb51-3a335502d776
    messageVersion: 2.0.0
    module: Discovery
    payload:
      data:
        alertConfiguration: 'false'
        credential:
        - credentialId: tTn2gSZkKzN2kUS4CaTjAKuT
          credentialValue:
            data:
              cipher: jIim958AQbRgM1TWDq+DrKrb3w441+eJ0u/hbI/uAHFfBXFLz57MLiGiYeFtsPXpUfVT7unEEPdRFdmzqw7QepPMRwhm+e6qxOwo9ZrOKIk36mjlB0TvPi
              classId: credential.cipher
              key1: 181c2af1a4c
              type: APPLICATION
              uuid: tTn2gSZkKzN2kUS4CaTjAKuT
              ver: 2
          fieldName: credentials
        ipAddress: 10.60.89.132
        notificationAlert: 'false'
        protocol: 'true'
      nativeTypes:
        Dell PowerFlex System:
          resourceType: Storage
    requireAck: false
    sha: b8e123a520e70034f5619e5d0e2662604a2d7c706c5412758700b1d08d07fae8
    subtype: Configuration
  response: 
    - status_code: 200
```


## Monitoring message
```yaml
- method: POST
  url: /api/v2/messages
  content-type: application/json
  body: 
    action: Update
    app: power-flex-dell
    appIntegrationId: INTG-86032f6a-78f3-4620-8460-3466a41aa247
    appVersion: 1.0.0
    configurationId: ADAPTER-MANIFEST-80ee8f1a-26b5-43e5-af62-2e50edc8d070
    messageId: ba623a75-e9ad-45d0-8142-476afd4195ec
    messageVersion: 2.0.0
    module: Monitoring
    subtype: Configuration
    payload:
      appConfig:
        data:
          alertConfiguration: 'false'
          credential:
          - credentialId: tTn2gSZkKzN2kUS4CaTjAKuT
            credentialValue:
              data:
                cipher: v
                classId: credential.cipher
                key1: 181c2af1a4c
                type: APPLICATION
                uuid: tTn2gSZkKzN2kUS4CaTjAKuT
                ver: 2
            fieldName: credentials
          credentialId:
          - fieldName: credentials
            value: tTn2gSZkKzN2kUS4CaTjAKuT
          ipAddress: 10.60.89.132
          notificationAlert: 'false'
          protocol: 'true'
        nativeTypes:
          Dell PowerFlex System:
            resourceType: Storage
      monitorId: f852100d-c00b-4a96-85e0-c5f31908b196
      nativeType:
        Dell PowerFlex System:
        - dell_powerflex_event_Statistics
      resources:
        - appConfigId: ADAPTER-MANIFEST-80ee8f1a-26b5-43e5-af62-2e50edc8d070
          credential: []
          credentialId: []
          moId: '08a9c0c351862e0f'
          resourceId: e0a884dc-0c56-426a-b853-40adeb697053
          signature: to be filled
          templateCustomization: {}
          templates:
          - app: power-flex-dell
            nativeType: Dell PowerFlex System
            templateId: 27dcc66a-a273-4fc5-8852-d6acaad97d03
      templateId: 27dcc66a-a273-4fc5-8852-d6acaad97d03
    

  response: 
    - status_code: 200
```

## Log Level
```yaml
- method: PUT
  url: /api/v1/log?level=DEBUG
  response: 
    - status_code: 200
```

## Debug App
```yaml
- method: POST
  url: /api/v1/debug
  body: 
    apiVersion: debug/v1
    module: Device
    app: dell-sdk-app
    action: Reachability
    payload:
      vcenterName: vcenter5
      protocol: http
      ipAddress: 172.25.252.193
      port: '45000'
  response: 
    - status_code: 200
      status_description: success json message
    - status_code: 500
      status_description: failure json message
```

