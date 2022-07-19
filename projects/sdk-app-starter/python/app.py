import sys
from pathlib import Path

#from store import writefile
from jinja2 import Template, Environment, FileSystemLoader
from python.assets import *
import shutil
import os
import json

def initialize_python_app(destination_path,current_path):
    current_path = current_path + "/python"
    domainJson = {}
    with open(current_path+'/domain.json') as domainFile:
        domainJson = json.load(domainFile)

    print("App Initialized")
    print(domainJson['appName'])
    appName = domainJson['appName']
    appVersion = domainJson['appVersion']

    manifestFile = {}
    with open(current_path+'/templates/manifest.json') as manifestFile:
        manifestJson = json.load(manifestFile)

    #generating manifest
    generateManifest(domainJson, manifestJson,destination_path,current_path)

    env = Environment(loader=FileSystemLoader(current_path+'/templates/'))
    #print("env"+str(env))

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
           monitoring_map = monitoring_map + ",'" + ntName+"':" + ntName.title().replace(" ", "") + "Monitoring"
        else:
           monitoring_names = ntName.title().replace(" ", "") + "Monitoring"
           monitoring_map = "{'" + ntName+"':" + ntName.title().replace(" ", "") + "Monitoring"

        discoveryTemplate = env.get_template('discovery.py')
        ntdiscoveryTemplate = discoveryTemplate.render(nativeType = ntName.title().replace(" ", ""),ntName=ntName)

        ntdiscoveryTemplateFile = destination_path + appName + '/discovery/_' + ntName.title().replace(" ", "") + '_discovery.py'
        os.makedirs(os.path.dirname(ntdiscoveryTemplateFile), exist_ok=True)

        with open(ntdiscoveryTemplateFile, "w") as f:
            f.write(ntdiscoveryTemplate)

        monitoringTemplate = env.get_template('monitoring.py')
        ntmonitoringTemplate = monitoringTemplate.render(nativeType = ntName.title().replace(" ", ""),ntName=ntName)

        ntMonitoringTemplateFile = destination_path + appName + '/monitoring/_' + ntName.title().replace(" ", "") + '_monitoring.py'
        os.makedirs(os.path.dirname(ntMonitoringTemplateFile), exist_ok=True)

        with open(ntMonitoringTemplateFile, "w") as f:
            f.write(ntmonitoringTemplate)

    #Generating target folder (discovery and monitoring)

    discoveryTemplate = env.get_template('target_discovery.py')
    ntdiscoveryTemplate = discoveryTemplate.render(nativeType = nativeTypeArray)

    ntdiscoveryTemplateFile = destination_path + appName + '/target/_discovery.py'
    os.makedirs(os.path.dirname(ntdiscoveryTemplateFile), exist_ok=True)

    with open(ntdiscoveryTemplateFile, "w") as f:
        f.write(ntdiscoveryTemplate)

    monitoringTemplate = env.get_template('target_monitoring.py')
    ntmonitoringTemplate = monitoringTemplate.render(nativeType = nativeTypeArray)

    ntMonitoringTemplateFile = destination_path + appName + '/target/_monitor.py'
    os.makedirs(os.path.dirname(ntMonitoringTemplateFile), exist_ok=True)

    with open(ntMonitoringTemplateFile, "w") as f:
        f.write(ntmonitoringTemplate)

    shutil.copy(current_path + '/templates/static/target/__init__.py', destination_path + appName + '/target/__init__.py')

    dm_dic = {}
    dm_dic["discovery"] = discovery_names
    dm_dic["monitoring"] =  monitoring_names
    dm_dic["monitoringmap"] = monitoring_map + "}"

    discoveryInit = env.get_template('discovery_init.py')
    discoveryInitTemplate = discoveryInit.render(native_type_dict = nativeTypeInit)

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
    generateAppFile(env,appName,dm_dic,destination_path,current_path)

    # Generating make file
    generateMakeFile(env,appName,destination_path,current_path)

    # Generating helm file
    generateHelmCharts(env,appName,appVersion,destination_path,current_path)

    # Generating docker file
    generateDockerFile(appName,destination_path,current_path)

    # Generating requirements file
    shutil.copy(current_path+'/templates/requirements.txt', destination_path + appName + '/requirements.txt')

    '''
    generateManifest(domainJson)
    generateHelmChart(domainJson)
    generateDockerFile(domainJson)
    generateMakeFile(domainJson)
    '''
    if os.path.exists(destination_path + appName + '/debug'):
        shutil.rmtree(destination_path + appName + '/debug')
    shutil.copytree(current_path+'/templates/static/debug', destination_path + appName + '/debug')
    if os.path.exists(destination_path + appName + '/core'):
        shutil.rmtree(destination_path + appName + '/core')
    shutil.copytree(current_path+'/templates/static/core', destination_path + appName + '/core')
    if os.path.exists(destination_path + appName + '/handler'):
        shutil.rmtree(destination_path + appName + '/handler')
    shutil.copytree(current_path+'/templates/static/handler', destination_path+ appName + '/handler')
    if os.path.exists(destination_path + appName + '/server'):
        shutil.rmtree(destination_path + appName + '/server')
    shutil.copytree(current_path+'/templates/static/server', destination_path + appName + '/server')
    if os.path.exists(destination_path + appName + '/logger'):
        shutil.rmtree(destination_path + appName + '/logger')
    shutil.copytree(current_path+'/templates/static/logger', destination_path + appName + '/logger')
    if os.path.exists(destination_path + appName + '/httpclient'):
        shutil.rmtree(destination_path + appName + '/httpclient')
    shutil.copytree(current_path+'/templates/static/httpclient', destination_path + appName + '/httpclient')
    #writefile()



def generateAppFile(env,appName,dm_dic,destination_path,current_path):
    appTemplate = env.get_template('app.py')
    appTemplateOutput = appTemplate.render(dm_dic=dm_dic)

    appTemplateFile = destination_path + appName + '/app.py'
    os.makedirs(os.path.dirname(appTemplateFile), exist_ok=True)

    with open(appTemplateFile, "w") as f:
        f.write(appTemplateOutput)


def generateDockerFile(appName,destination_path,current_path):
    shutil.copy(current_path+'/templates/Dockerfile', destination_path + appName + '/Dockerfile')


def generateMakeFile(env,appName,destination_path,current_path):
    makefiletemplate = env.get_template('make.sh')
    makefiletemplateOutput = makefiletemplate.render(appName=appName)
    #print(makefiletemplateOutput)

    makeFile = destination_path + appName + '/make.sh'
    os.makedirs(os.path.dirname(makeFile), exist_ok=True)

    with open(makeFile, "w") as f:
        f.write(makefiletemplateOutput)


def generateHelmCharts(env,appName,appVersion,destination_path,current_path):
    # Copying Entire helm directoty
    if os.path.exists(destination_path + appName + '/assets/charts/' + appName):
        shutil.rmtree(destination_path + appName + '/assets/charts/' + appName)
    shutil.copytree(current_path+'/templates/helloworld-app-python',
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
    charttemplateOutput = charttemplate.render(appName=appName,appVersion=appVersion)
    # print(output_from_parsed_template)

    chartFile = destination_path + appName + '/assets/charts/' + appName + '/Chart.yaml'
    os.makedirs(os.path.dirname(chartFile), exist_ok=True)

    with open(chartFile, "w") as f:
        f.write(charttemplateOutput)


def generateManifest(domainJson, manifestJsonTemplate,destination_path,current_path):
    manifestJson = {}
    manifestJson["name"] = domainJson['appName']
    manifestJson["displayName"] = domainJson['appName']
    manifestJson["appVersion"] = "1.0.0"
    manifestJson["description"] = 'This is a ' + domainJson['appName'] + ' App'
    manifestJson["category"] = 'SDK'
    manifestJson["appScope"] = 'Private'
    manifestJson["assets"] = manifestJsonTemplate["assets"]

    # version object
    versionObject = {}
    versionObject["apiVersion"] = "api/v2"
    versionObject["kind"] = "AppVersion"

    metadataObject = {}
    # metadataObject['appName'] = domainJson['appName']
    # metadataObject['displayName'] = domainJson['appName']
    metadataObject['description'] = 'Sample app Integrates with sample vcenter APIs'
    metadataObject['version'] = '1.0.0'
    metadataObject['deployment'] = "Image"

    # categoriesArray = ['DISCOVERY AND MONITORING']
    # metadataObject['categories'] = categoriesArray
    versionObject["metadata"] = metadataObject

    specObject = {}
    assetsObject = {}

    helmObject = {}
    helmObject['pullType'] = 'image'
    helmObject['url'] = 'us-docker.pkg.dev/gateway-images/gateway-cluster-charts'
    assetsObject['helm'] = helmObject

    mavenObject = {}
    mavenObject['url'] = ''
    mavenObject['digest'] = ''
    assetsObject['maven'] = mavenObject

    iconObject = {}
    iconObject['type'] = ''
    iconObject['url'] = ''
    assetsObject['icon'] = iconObject

    mdObject = {}
    mdObject['url'] = ''
    assetsObject['md'] = mdObject

    imageArray = []
    assetsObject['images'] = imageArray

    manifestObject = {}

    try :
        dataObject = domainJson["data"]
    except KeyError:
        dataObject = {}
    manifestObject['data'] = dataObject

    nativeTypeMeticArrayMap = {}
    nativeTypeMonitorArrayMap = {}
    for nativeTypeMetric in domainJson['nativeType']:
        nativeTypeMeticArrayMap[nativeTypeMetric['name']] = nativeTypeMetric['metric']
        nativeTypeMonitorArrayMap[nativeTypeMetric['name']] = nativeTypeMetric['monitors']
    nativeTypeObject = {}
    for nativeType in domainJson['nativeTypeMapping']:

        domainNativeTypeObject = {}
        domainNativeTypeObject["resourceType"] = nativeType['opsrampResourceType']

        metricsObject = {}
        try:
            metricsArray = nativeTypeMeticArrayMap[nativeType['nativeType']]
        except KeyError:
            continue
        for metric in metricsArray:
            metricObject = {}
            metricObject['alertOn'] = metric['alertOn']
            metricObject['name'] = metric['name']
            metricObject['displayName'] = metric['name']
            metricObject['description'] = 'provides ' + metric['name']
            metricObject['units'] = metric['units']
            metricObject['factor'] = metric['factor']
            metricObject['dataPoint'] = metric['dataPoint']
            metricObject['alertSummary'] = metric['alertSummary']
            metricObject['alertDescription'] = metric['alertDescription']

            warningObject = metric['warning']
            metricObject['warning'] = warningObject

            criticalObject = metric['critical']
            metricObject['critical'] = criticalObject

            metricObject['availability'] = metric['availability']
            metricObject['graphPoint'] = metric['graphPoint']
            metricObject['raiseAlert'] = metric['raiseAlert']
            metricObject['formatPlottedValue'] = metric['formatPlottedValue']

            if metricObject['units'] == "":
                try:
                    datapointObject = metric["dataPointConverisonOptions"]
                except KeyError:
                    datapointObject = [{"1": "true"}, {"0": "false"}]
            else:
                datapointObject = [{"1": "true"}, {"0": "false"}]

            metricObject['dataPointConverisonOptions'] = datapointObject
            metricObject['formatGraph'] = metric['formatGraph']
            metricObject['formatAlert'] = metric['formatAlert']

            metricsObject[metric['name']] = metricObject

        monitorsObject = {}

        monitorArray = nativeTypeMonitorArrayMap[nativeType['nativeType']]
        for monitor in monitorArray:
            monitorObject = {}
            monitorObject['title'] = monitor['title']
            monitorObject['frequency'] = monitor['frequency']
            monitorObject['metrics'] = monitor['metric']

            monitorsObject[monitor['title']] = monitorObject

        domainNativeTypeObject['metrics'] = metricsObject
        domainNativeTypeObject['monitors'] = monitorsObject

        nativeTypeObject[nativeType['nativeType']] = domainNativeTypeObject

    manifestObject['nativeTypes'] = nativeTypeObject

    schemaObject = {}
    propertiesObject = {}
    try:
        requiredObject = domainJson["required"]
    except KeyError:
        requiredObject = []
    for schema in domainJson['discoveryConfiguration']:
        propertyObject = {'type': schema['dataType']}
        propertiesObject[schema['propertyName']] = propertyObject

    schemaObject['properties'] = propertiesObject
    schemaObject['required'] = requiredObject
    schemaObject['type'] = "object"
    manifestObject['schema'] = schemaObject
    # print(schemaObject)

    uischemaObject = {}
    elementsObject = []
    notifylis = []
    for schema in domainJson['discoveryConfiguration']:
        if schema['propertyName'] == "alertConfiguration" or schema['propertyName'] == "alertSeverity" or schema[
            'propertyName'] == "alertOnRootResource" or schema['propertyName'] == "alertSeverityMapping":
            notifylis.append(schema)
            continue
        try:
            OptionsObject = {}
            OptionsObject["placeholder"] = schema["placeholder"]
            OptionsObject["credentialType"] = schema["credentialType"]
            OptionsObject["format"] = "credential"
        except KeyError:
            pass
        elementObject = {'type': "Control", 'scope': '#/properties/' + schema['propertyName'],
                         'label': schema['label']}
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

    manifestFile = destination_path + domainJson['appName'] + '/assets/manifest.json'
    os.makedirs(os.path.dirname(manifestFile), exist_ok=True)

    with open(manifestFile, "w") as f:
        f.write(json.dumps(manifestJson))


def getNotifyData(notifyLis):
    true = True
    return {
        "type": "Group",
        "label": "Event Polling",
        "elements": [
            {
                "type": "Control",
                "scope": "#/properties/alertConfiguration"
            },
            {
                "type": "Group",
                "elements": [
                    {
                        "type": "Control",
                        "scope": "#/properties/alertOnRootResource"
                    },
                    {
                        "type": "Control",
                        "scope": "#/properties/alertSeverity",
                        "label": "alertSeverity",
                        "options": {
                            "placeholder": "alertSeverity"
                        }
                    },
                    {
                        "type": "Control",
                        "scope": "#/properties/alertSeverityMapping",
                        "options": {
                            "placeholder": "alertSeverityMapping"
                        }
                    }
                ],
                "rule": {
                    "effect": "SHOW",
                    "condition": {
                        "scope": "#/properties/alertConfiguration",
                        "schema": {
                            "const": true
                        }
                    }
                }
            }
        ]
    }




