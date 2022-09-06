import json
import os


def generateManifest(domainJson, destination_path, app_language):
    manifestJson = {"name": domainJson.get('appName'), "displayName": domainJson.get('displayName'),
                    "appVersion": domainJson.get("appVersion"), "description": domainJson.get("description"),
                    "category": 'SDK', "appScope": 'Private'}
    assetObject = {}

    iconObject = {'type': "png", "url": domainJson.get("iconUrl")}
    assetObject['icon'] = iconObject

    mdObject = {'url': ""}
    assetObject['md'] = mdObject

    imageArray = []
    assetObject['images'] = imageArray

    manifestJson["assets"] = assetObject

    # version object
    versionObject = {"apiVersion": "api/v2", "kind": "AppVersion"}

    metadataObject = {}
    if app_language == "python":
        metadataObject['description'] = 'Sample app Integrates with sample vcenter APIs'
        metadataObject['version'] = '1.0.0'
        metadataObject['deployment'] = "Image"
    elif app_language == "java":
        metadataObject['description'] = 'Sample app Integrates with sample vcenter APIs'
        metadataObject['version'] = '1.0.0'

    versionObject["metadata"] = metadataObject

    specObject = {}
    assetsObject = {}

    helmObject = {'pullType': 'image', 'url': domainJson.get("helmUrl")}
    assetsObject['helm'] = helmObject

    mavenObject = {'url': domainJson.get("mavenUrl"), 'digest': ''}
    assetsObject['maven'] = mavenObject

    iconObject = {'type': "", 'url': ""}
    assetsObject['icon'] = iconObject

    mdObject = {'url': ''}
    assetsObject['md'] = mdObject

    imageArray = []
    assetsObject['images'] = imageArray

    manifestObject = {}

    dataObject = domainJson.get("data")
    if dataObject is None:
        dataObject = {}
    manifestObject['data'] = dataObject

    nativeTypeMeticArrayMap = {}
    nativeTypeMonitorArrayMap = {}
    for nativeTypeMetric in domainJson.get('nativeType'):
        nativeTypeMeticArrayMap[nativeTypeMetric.get('name')] = nativeTypeMetric.get('metric')
        nativeTypeMonitorArrayMap[nativeTypeMetric.get('name')] = nativeTypeMetric.get('monitors')
    nativeTypeObject = {}
    for nativeType in domainJson.get('nativeTypeMapping'):

        domainNativeTypeObject = {"resourceType": nativeType.get('opsrampResourceType')}

        metricsObject = {}
        try:
            metricsArray = nativeTypeMeticArrayMap[nativeType.get('nativeType')]
        except KeyError:
            continue
        for metric in metricsArray:
            metricObject = {'alertOn': metric.get('alertOn'), 'name': metric.get('name'),
                            'displayName': metric.get('name'),
                            'description': 'provides ' + metric.get('name') if metric.get(
                                "description") is None else metric.get("description"), 'units': metric.get('units'),
                            'factor': metric.get('factor'), 'dataPoint': metric.get('dataPoint'),
                            'alertSummary': metric.get('alertSummary'),
                            'alertDescription': metric.get('alertDescription')}

            warningObject = metric.get('warning')
            metricObject['warning'] = warningObject

            criticalObject = metric.get('critical')
            metricObject['critical'] = criticalObject

            metricObject['availability'] = metric.get('availability')
            metricObject['graphPoint'] = metric.get('graphPoint')
            metricObject['raiseAlert'] = metric.get('raiseAlert')
            metricObject['formatPlottedValue'] = metric.get('formatPlottedValue')

            if metricObject.get("units") is None:
                datapointObject = metric.get("dataPointConverisonOptions")
            else:
                datapointObject = [{"1": "true"}, {"0": "false"}]

            metricObject['dataPointConverisonOptions'] = datapointObject
            metricObject['formatGraph'] = metric.get('formatGraph')
            metricObject['formatAlert'] = metric.get('formatAlert')

            metricsObject[metric.get('name')] = metricObject

        monitorsObject = {}

        monitorArray = nativeTypeMonitorArrayMap[nativeType.get('nativeType')]
        for monitor in monitorArray:
            monitorObject = {'title': monitor.get('title'), 'frequency': monitor.get('frequency'),
                             'metrics': monitor.get('metric')}

            monitorsObject[monitor.get('title')] = monitorObject

        domainNativeTypeObject['metrics'] = metricsObject
        domainNativeTypeObject['monitors'] = monitorsObject

        nativeTypeObject[nativeType.get('nativeType')] = domainNativeTypeObject

    manifestObject['nativeTypes'] = nativeTypeObject

    schemaObject = {}
    propertiesObject = {}

    requiredObject = domainJson.get("required")
    if requiredObject is None:
        requiredObject = []

    # schema
    for schema in domainJson.get('discoveryConfiguration'):
        propertyObject = {'type': schema.get('dataType')}
        propertiesObject[schema.get('propertyName')] = propertyObject

    schemaObject['properties'] = propertiesObject
    schemaObject['required'] = requiredObject
    schemaObject['type'] = "object"
    manifestObject['schema'] = schemaObject
    # print(schemaObject)

    uischemaObject = {}
    elementsObject = []
    notifylis = []
    for schema in domainJson.get('discoveryConfiguration'):
        if schema.get('propertyName') == "alertConfiguration" or schema.get('propertyName') == "alertSeverity" or \
                schema.get('propertyName') == "alertOnRootResource" or \
                schema.get("propertyName") == "alertSeverityMapping":
            notifylis.append(schema)
            continue
        OptionsObject = {}
        if schema.get("placeholder") is not None:
            OptionsObject["placeholder"] = schema.get("placeholder")
        if schema.get("credentialType") is not None:
            OptionsObject["credentialType"] = schema.get("credentialType")
            OptionsObject["format"] = "credential"

        elementObject = {'type': "Control", 'scope': '#/properties/' + schema.get('propertyName'),
                         'label': schema.get('label')}
        if len(OptionsObject) > 0:
            elementObject['options'] = OptionsObject

        elementsObject.append(elementObject)
    if len(notifylis) > 0:
        notifyobject = getNotifyData(notifylis)
        elementsObject.append(notifyobject)
    uischemaObject['elements'] = elementsObject
    uischemaObject['type'] = "VerticalLayout"
    manifestObject['uischema'] = uischemaObject

    assetsObject['manifest'] = manifestObject

    specObject['assets'] = assetsObject
    versionObject["spec"] = specObject

    manifestJson["version"] = versionObject

    manifestFile = destination_path + '/manifest/manifest.json'
    os.makedirs(os.path.dirname(manifestFile), exist_ok=True)

    with open(manifestFile, "w") as f:
        f.write(json.dumps(manifestJson))


def getNotifyData(notifyLis):
    true = True
    eventsObject = {}
    eventObject = {}
    elemetObject = []
    rule = {}
    rootelement = {}
    for i in notifyLis:
        if i.get("propertyName") == "alertConfiguration":

            rootelement = {"type": "Control",
                           "scope": "#/properties/" + i.get("propertyName")}
            condition = {
                "scope": "#/properties/" + i.get("propertyName"),
                "schema": {
                    "const": true
                }
            }
            rule = {"effect": "SHOW", "condition": condition}

        else:
            element = {"type": "Control",
                       "scope": "#/properties/" + i.get("propertyName")}
            if i.get("label") is not None:
                element.update({"label": i.get("label")})
                optionObject = {"placeholder": i.get("label")}
                element.update({"options": optionObject})

            elemetObject.append(element)
            eventObject.update({"type": "Group", "elements": elemetObject})
            eventObject.update({"rule": rule})
    elemetsObject = [rootelement, eventObject]
    eventsObject.update({"type": "Group", "elements": elemetsObject})
    return eventsObject
