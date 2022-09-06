# from store import writefile
from jinja2 import Environment, FileSystemLoader
from python.assets import *
import shutil
import os
import json


def initialize_python_app(destination_path, current_path, domain_json_path):
    current_path = current_path + "/python"
    with open(domain_json_path) as domainFile:
        domainJson = json.load(domainFile)

    print("App Initialized")
    print(domainJson['appName'])
    appName = domainJson['appName']
    appVersion = domainJson['appVersion']

    # generating manifest
    generateManifest(domainJson, destination_path)

    env = Environment(loader=FileSystemLoader(current_path + '/templates/'))
    # print("env"+str(env))

    # Generating discovery folder and native types discovery
    nativeTypeArray = domainJson['nativeType']
    nativeTypeInit = {}
    discovery_names = ""
    monitoring_names = ""
    monitoring_map = ""

    for nt in nativeTypeArray:
        ntName = nt['name']
        nativeTypeInit[ntName] = ntName.title().replace(" ", "")
        if len(discovery_names) > 0:
            discovery_names = discovery_names + "," + ntName.title().replace(" ", "") + "Discovery"
        else:
            discovery_names = ntName.title().replace(" ", "") + "Discovery"

        if len(monitoring_names) > 0:
            monitoring_names = monitoring_names + "," + ntName.title().replace(" ", "") + "Monitoring"
            monitoring_map = monitoring_map + ",'" + ntName + "':" + ntName.title().replace(" ", "") + "Monitoring"
        else:
            monitoring_names = ntName.title().replace(" ", "") + "Monitoring"
            monitoring_map = "{'" + ntName + "':" + ntName.title().replace(" ", "") + "Monitoring"

        discoveryTemplate = env.get_template('discovery.py')
        ntdiscoveryTemplate = discoveryTemplate.render(nativeType=ntName.title().replace(" ", ""), ntName=ntName)

        ntdiscoveryTemplateFile = destination_path + appName + '/discovery/_' + ntName.title().replace(" ",
                                                                                                       "") + '_discovery.py'
        os.makedirs(os.path.dirname(ntdiscoveryTemplateFile), exist_ok=True)

        with open(ntdiscoveryTemplateFile, "w") as f:
            f.write(ntdiscoveryTemplate)

        monitoringTemplate = env.get_template('monitoring.py')
        ntmonitoringTemplate = monitoringTemplate.render(nativeType=ntName.title().replace(" ", ""), ntName=ntName)

        ntMonitoringTemplateFile = destination_path + appName + '/monitoring/_' + ntName.title().replace(" ",
                                                                                                         "") + '_monitoring.py'
        os.makedirs(os.path.dirname(ntMonitoringTemplateFile), exist_ok=True)

        with open(ntMonitoringTemplateFile, "w") as f:
            f.write(ntmonitoringTemplate)

    # Generating target folder (discovery and monitoring)

    discoveryTemplate = env.get_template('target_discovery.py')
    ntdiscoveryTemplate = discoveryTemplate.render(nativeType=nativeTypeArray)

    ntdiscoveryTemplateFile = destination_path + appName + '/target/_discovery.py'
    os.makedirs(os.path.dirname(ntdiscoveryTemplateFile), exist_ok=True)

    with open(ntdiscoveryTemplateFile, "w") as f:
        f.write(ntdiscoveryTemplate)

    monitoringTemplate = env.get_template('target_monitoring.py')
    ntmonitoringTemplate = monitoringTemplate.render(nativeType=nativeTypeArray)

    ntMonitoringTemplateFile = destination_path + appName + '/target/_monitor.py'
    os.makedirs(os.path.dirname(ntMonitoringTemplateFile), exist_ok=True)

    with open(ntMonitoringTemplateFile, "w") as f:
        f.write(ntmonitoringTemplate)

    shutil.copy(current_path + '/templates/static/target/__init__.py',
                destination_path + appName + '/target/__init__.py')

    dm_dic = {"discovery": discovery_names, "monitoring": monitoring_names, "monitoringmap": monitoring_map + "}"}

    discoveryInit = env.get_template('discovery_init.py')
    discoveryInitTemplate = discoveryInit.render(native_type_dict=nativeTypeInit)

    discoveryInitTemplateFile = destination_path + appName + '/discovery/__init__.py'
    os.makedirs(os.path.dirname(discoveryInitTemplateFile), exist_ok=True)

    with open(discoveryInitTemplateFile, "w") as f:
        f.write(discoveryInitTemplate)

    monitoringInit = env.get_template('monitoring_init.py')
    monitoringInitTemplate = monitoringInit.render(native_type_dict=nativeTypeInit)

    monitoringInitTemplateFile = destination_path + appName + '/monitoring/__init__.py'
    os.makedirs(os.path.dirname(monitoringInitTemplateFile), exist_ok=True)

    with open(monitoringInitTemplateFile, "w") as f:
        f.write(monitoringInitTemplate)

    # Generating app.py
    generateAppFile(env, appName, dm_dic, destination_path)

    # Generating make file
    generateMakeFile(env, appName, appVersion, destination_path)

    # Generating helm file
    generateHelmCharts(env, appName, appVersion, destination_path, current_path)

    # Generating docker file
    generateDockerFile(appName, destination_path, current_path)

    # Generating requirements file
    shutil.copy(current_path + '/templates/requirements.txt', destination_path + appName + '/requirements.txt')

    if os.path.exists(destination_path + appName + '/debug'):
        shutil.rmtree(destination_path + appName + '/debug')
    shutil.copytree(current_path + '/templates/static/debug', destination_path + appName + '/debug')
    if os.path.exists(destination_path + appName + '/core'):
        shutil.rmtree(destination_path + appName + '/core')
    shutil.copytree(current_path + '/templates/static/core', destination_path + appName + '/core')
    if os.path.exists(destination_path + appName + '/handler'):
        shutil.rmtree(destination_path + appName + '/handler')
    shutil.copytree(current_path + '/templates/static/handler', destination_path + appName + '/handler')
    if os.path.exists(destination_path + appName + '/server'):
        shutil.rmtree(destination_path + appName + '/server')
    shutil.copytree(current_path + '/templates/static/server', destination_path + appName + '/server')
    if os.path.exists(destination_path + appName + '/logger'):
        shutil.rmtree(destination_path + appName + '/logger')
    shutil.copytree(current_path + '/templates/static/logger', destination_path + appName + '/logger')
    if os.path.exists(destination_path + appName + '/httpclient'):
        shutil.rmtree(destination_path + appName + '/httpclient')
    shutil.copytree(current_path + '/templates/static/httpclient', destination_path + appName + '/httpclient')
    # writefile()


def generateAppFile(env, appName, dm_dic, destination_path):
    appTemplate = env.get_template('app.py')
    appTemplateOutput = appTemplate.render(dm_dic=dm_dic)

    appTemplateFile = destination_path + appName + '/app.py'
    os.makedirs(os.path.dirname(appTemplateFile), exist_ok=True)

    with open(appTemplateFile, "w") as f:
        f.write(appTemplateOutput)


def generateDockerFile(appName, destination_path, current_path):
    shutil.copy(current_path + '/templates/Dockerfile', destination_path + appName + '/Dockerfile')


def generateMakeFile(env, appName, appVersion, destination_path):
    makefiletemplate = env.get_template('make.sh')
    makefiletemplateOutput = makefiletemplate.render(appName=appName, appVersion=appVersion)
    # print(makefiletemplateOutput)

    makeFile = destination_path + appName + '/make.sh'
    os.makedirs(os.path.dirname(makeFile), exist_ok=True)

    with open(makeFile, "w") as f:
        f.write(makefiletemplateOutput)


def generateHelmCharts(env, appName, appVersion, destination_path, current_path):
    # Copying Entire helm directoty
    if os.path.exists(destination_path + appName + '/assets/charts/' + appName):
        shutil.rmtree(destination_path + appName + '/assets/charts/' + appName)
    shutil.copytree(current_path + '/templates/helloworld-app-python',
                    destination_path + appName + '/assets/charts/' + appName)

    # Replacing values yaml file
    chartValuetemplate = env.get_template('/helloworld-app-python/values.yaml')
    chartValuetemplateOutput = chartValuetemplate.render(appName=appName)
    # print(output_from_parsed_template)

    chartValueFile = destination_path + appName + '/assets/charts/' + appName + '/values.yaml'
    os.makedirs(os.path.dirname(chartValueFile), exist_ok=True)

    with open(chartValueFile, "w") as f:
        f.write(chartValuetemplateOutput)

    # Replacing cluster yaml file
    chartClustertemplate = env.get_template('/helloworld-app-python/cluster.yaml')
    chartClustertemplateOutput = chartClustertemplate.render(appName=appName)
    # print(output_from_parsed_template)

    chartClusterFile = destination_path + appName + '/assets/charts/' + appName + '/cluster.yaml'
    os.makedirs(os.path.dirname(chartClusterFile), exist_ok=True)

    with open(chartClusterFile, "w") as f:
        f.write(chartClustertemplateOutput)

    # Replacing chart file
    charttemplate = env.get_template('/helloworld-app-python/Chart.yaml')
    charttemplateOutput = charttemplate.render(appName=appName, appVersion=appVersion)
    # print(output_from_parsed_template)

    chartFile = destination_path + appName + '/assets/charts/' + appName + '/Chart.yaml'
    os.makedirs(os.path.dirname(chartFile), exist_ok=True)

    with open(chartFile, "w") as f:
        f.write(charttemplateOutput)


def generateManifest(domainJson, destination_path):
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

    metadataObject = {'description': domainJson.get("description"), 'version': domainJson.get("appVersion"),
                      'deployment': "Image"}

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

    manifestFile = destination_path + domainJson.get('appName') + '/assets/manifest.json'
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
