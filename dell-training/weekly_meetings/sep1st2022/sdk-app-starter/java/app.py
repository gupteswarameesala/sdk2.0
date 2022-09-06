import re
import sys
from pathlib import Path

#from store import writefile
from jinja2 import Template, Environment, FileSystemLoader
from java.assets import *
import shutil
import os
import json




def initialize_java_app(destination_path, current_path,domain_json_path):
    current_path = current_path + "/java"
    domainJson = {}
    with open(domain_json_path) as domainFile:
        domainJson = json.load(domainFile)

    print("App Initialized")
    print(domainJson['appName'])
    appName = domainJson['appName']
    appVersion = domainJson['appVersion']

    manifestFile = {}
    with open(current_path+'/templates/manifest.json') as manifestFile:
        manifestJson = json.load(manifestFile)


    env = Environment(loader=FileSystemLoader(current_path+'/templates/'))



    # Generating discovery folder and native types discovery
    nativeTypeMonitorArray = domainJson['nativeType']
    nativeTypeDiscoveryArray = domainJson['nativeTypeMapping']
    nativeTypeInit = {}
    discovery_names = ""
    monitoring_names = ""
    monitoring_map = {}
    discovery_class = ""

    for nt in nativeTypeDiscoveryArray:
        ntName = nt['nativeType']
        nativeTypeInit[ntName] = ntName.title().replace(" ", "")
        if len(discovery_names) > 0:
            discovery_names = discovery_names + "," + ntName.title().replace(" ", "") + "Discovery"
            discovery_class = discovery_class + "," + ntName.title().replace(" ", "") + "Discovery.class"
        else:
            discovery_names = ntName.title().replace(" ", "") + "Discovery"
            discovery_class = ntName.title().replace(" ", "") + "Discovery.class"

        discoveryTemplate = env.get_template('Discovery.java')
        ntdiscoveryTemplate = discoveryTemplate.render(nativeType=ntName.title().replace(" ", ""), ntName=ntName)

        ntdiscoveryTemplateFile = destination_path + appName + '/core/src/main/java/com/opsramp/gateway/app/actions/impl/discovery/' + ntName.title().replace(
            " ", "") + 'Discovery.java'
        os.makedirs(os.path.dirname(ntdiscoveryTemplateFile), exist_ok=True)

        with open(ntdiscoveryTemplateFile, "w") as f:
            f.write(ntdiscoveryTemplate)

    for nt in nativeTypeMonitorArray:
        ntName = nt['name']
        nativeTypeInit[ntName] = ntName.title().replace(" ", "")

        if len(monitoring_names) > 0:
           monitoring_names = monitoring_names + "," + ntName.title().replace(" ", "") + "Monitor"
           monitoring_map.update({ ntName : ntName.title().replace(" ", "") + "Monitor"})
        else:
           monitoring_names = ntName.title().replace(" ", "") + "Monitor"
           monitoring_map.update({ntName: ntName.title().replace(" ", "") + "Monitor"})



        monitoringTemplate = env.get_template('Monitoring.java')
        ntmonitoringTemplate = monitoringTemplate.render(nativeType = ntName.title().replace(" ", ""),ntName=ntName)

        ntMonitoringTemplateFile = destination_path + appName + '/core/src/main/java/com/opsramp/gateway/app/actions/impl/monitor/' + ntName.title().replace(" ", "")+ 'Monitor.java'
        os.makedirs(os.path.dirname(ntMonitoringTemplateFile), exist_ok=True)

        with open(ntMonitoringTemplateFile, "w") as f:
            f.write(ntmonitoringTemplate)

    # copy monitoring util file
    shutil.copy(current_path + '/templates/static/MonitoringUtil.java',
                destination_path + appName + '/core/src/main/java/com/opsramp/gateway/app/actions/impl/monitor/MonitoringUtil.java')

    #copy discovery util file
    shutil.copy(current_path + '/templates/static/DiscoveryUtil.java',
                destination_path + appName + '/core/src/main/java/com/opsramp/gateway/app/actions/impl/discovery/DiscoveryUtil.java')

    #Generating target folder (discovery and monitoring)
    discoveryTemplate = env.get_template('TargetDiscovery.java')
    ntdiscoveryTemplate = discoveryTemplate.render(nativeType = nativeTypeDiscoveryArray)

    ntdiscoveryTemplateFile = destination_path + appName + '/core/src/main/java/com/opsramp/gateway/app/domain/TargetDiscovery.java'
    os.makedirs(os.path.dirname(ntdiscoveryTemplateFile), exist_ok=True)

    with open(ntdiscoveryTemplateFile, "w") as f:
        f.write(ntdiscoveryTemplate)

    monitoringTemplate = env.get_template('TargetMonitoring.java')
    ntmonitoringTemplate = monitoringTemplate.render(nativeType = nativeTypeMonitorArray)

    ntMonitoringTemplateFile = destination_path + appName + '/core/src/main/java/com/opsramp/gateway/app/domain/TargetMonitoring.java'
    os.makedirs(os.path.dirname(ntMonitoringTemplateFile), exist_ok=True)

    with open(ntMonitoringTemplateFile, "w") as f:
        f.write(ntmonitoringTemplate)

    dm_dic = {}
    dm_dic["discovery"] = discovery_names
    dm_dic["discoveryclass"] = discovery_class
    dm_dic["monitoring"] =  monitoring_names
    dm_dic["monitoringmap"] = monitoring_map

    res = re.sub('\W+', '', appName)


    # Generating helm file
    generateHelmCharts(env,appName,appVersion,destination_path, current_path)

    # Generating docker file
    generateDockerFile(env,appName,destination_path, current_path)


    #copying config.json file
    configTemplate = env.get_template('/cluster-adapter/config.json')
    configTemplateOutput = configTemplate.render(appName=appName,appVersion=appVersion)

    configTemplateFile = destination_path + appName + '/cluster-adapter/config.json'
    os.makedirs(os.path.dirname(configTemplateFile), exist_ok=True)

    with open(configTemplateFile, "w") as f:
        f.write(configTemplateOutput)

    #copying info.json file
    infoTemplate = env.get_template('/cluster-adapter/info.json')
    infoTemplateOutput = infoTemplate.render(appName=appName, appVersion=appVersion)

    infoTemplateFile = destination_path + appName + '/cluster-adapter/info.json'
    os.makedirs(os.path.dirname(infoTemplateFile), exist_ok=True)

    with open(infoTemplateFile, "w") as f:
        f.write(infoTemplateOutput)

    ##copying dependencies.json file
    shutil.copy(current_path + '/templates//cluster-adapter//dependencies.json', destination_path + appName + '/cluster-adapter/dependencies.json')

    shutil.copy(current_path + '/templates/static/classpath',
                destination_path + appName + '/classpath')

    #copy handlers folder in core
    if os.path.exists(destination_path + appName + '/core/src/main/java/com/opsramp/app/processor/handlers'):
        shutil.rmtree(destination_path + appName + '/core/src/main/java/com/opsramp/app/processor/handlers')
    shutil.copytree(current_path+'/templates/static//core/src/main/java/com/opsramp/app/processor/handlers', destination_path + appName + '/core/src/main/java/com/opsramp/app/processor/handlers')

    #copy resources folder in core
    if os.path.exists(destination_path + appName + '/core/src/main/resources'):
        shutil.rmtree(destination_path + appName + '/core/src/main/resources')
    shutil.copytree(current_path+'/templates/static/core/src/main/resources', destination_path + appName + '/core/src/main/resources')

    #copy util folder in core
    if os.path.exists(destination_path + appName + '/core/src/main/java/com/opsramp/gateway/app/util'):
        shutil.rmtree(destination_path + appName + '/core/src/main/java/com/opsramp/gateway/app/util')
    shutil.copytree(current_path+'/templates/static/util', destination_path + appName + '/core/src/main/java/com/opsramp/gateway/app/util')


    if os.path.exists(destination_path + appName + '/core/src/test'):
        shutil.rmtree(destination_path + appName + '/core/src/test')
    shutil.copytree(current_path + '/templates/static/core/src/test', destination_path + appName + '/core/src/test')

    generateClassicFolder(env, appName, appVersion,res,destination_path, current_path)

    generateClusterFolder(env, appName, appVersion,res,destination_path, current_path)

    # Generating handler.py
    generateHandlerFile(env, appName, dm_dic,destination_path, current_path)

    # Generating pom files
    generatePomFiles(env, appName, appVersion,res,destination_path, current_path)

    # Generating make file
    generateMakeFile(env, appName,appVersion,destination_path, current_path)

    # generating manifest
    generateManifest(domainJson, manifestJson,destination_path, current_path)

def generateClassicFolder(env, appName, appVersion,res,destination_path, current_path):
    if os.path.exists(destination_path + appName + '/classic-adapter'):
        shutil.rmtree(destination_path + appName + '/classic-adapter')
    classictemplate = env.get_template(
        '/static/classic-adapter/src/main/java/com/opsramp/gateway/sampleapp/classic/ClassicAdaptor.java')
    classictemplateOutput = classictemplate.render(res=res,appName = appName)

    makeFile = destination_path + appName + '/classic-adapter/src/main/java/com/opsramp/gateway/'+res+'/classic/ClassicAdaptor.java'
    os.makedirs(os.path.dirname(makeFile), exist_ok=True)

    #generte assembly.xml
    with open(makeFile, "w") as f:
        f.write(classictemplateOutput)
        shutil.copy(current_path + '/templates/static/classic-adapter/assembly.xml',
                    destination_path + appName + '/classic-adapter/assembly.xml')


def generateClusterFolder(env, appName, appVersion, res, destination_path, current_path):

    appdebugfiletemplate = env.get_template('/cluster-adapter/src/main/java/com/opsramp/gateway/sampleapp/cluster/AppDebugProcessor.java')
    appdebugfiletemplateOutput = appdebugfiletemplate.render(res=res)

    makeFile = destination_path + appName + '/cluster-adapter/src/main/java/com/opsramp/gateway/'+res+'/cluster/AppDebugProcessor.java'
    os.makedirs(os.path.dirname(makeFile), exist_ok=True)

    with open(makeFile, "w") as f:
        f.write(appdebugfiletemplateOutput)


    appprocessorfiletemplate = env.get_template(
        '/cluster-adapter/src/main/java/com/opsramp/gateway/sampleapp/cluster/ApplicationProcessor.java')
    appprocessorfiletemplateOutput = appprocessorfiletemplate.render(res=res)

    makeFile = destination_path + appName + '/cluster-adapter/src/main/java/com/opsramp/gateway/' + res + '/cluster/ApplicationProcessor.java'
    os.makedirs(os.path.dirname(makeFile), exist_ok=True)

    with open(makeFile, "w") as f:
        f.write(appprocessorfiletemplateOutput)

    logfiletemplate = env.get_template(
        '/cluster-adapter/src/main/java/com/opsramp/gateway/sampleapp/cluster/AppLogProcessor.java')
    logfiletemplateOutput = logfiletemplate.render(res=res)

    makeFile = destination_path + appName + '/cluster-adapter/src/main/java/com/opsramp/gateway/' + res + '/cluster/AppLogProcessor.java'
    os.makedirs(os.path.dirname(makeFile), exist_ok=True)

    with open(makeFile, "w") as f:
        f.write(logfiletemplateOutput)

    appfiletemplate = env.get_template(
        '/cluster-adapter/src/main/java/com/opsramp/gateway/sampleapp/cluster/AppMain.java')
    appfiletemplateOutput = appfiletemplate.render(res=res)

    makeFile = destination_path + appName + '/cluster-adapter/src/main/java/com/opsramp/gateway/' + res + '/cluster/AppMain.java'
    os.makedirs(os.path.dirname(makeFile), exist_ok=True)

    with open(makeFile, "w") as f:
        f.write(appfiletemplateOutput)

    appmainfiletemplate = env.get_template(
        '/cluster-adapter/src/main/java/com/opsramp/gateway/sampleapp/cluster/AppMainUtil.java')
    appmainfiletemplateOutput = appmainfiletemplate.render(res=res)

    makeFile = destination_path + appName + '/cluster-adapter/src/main/java/com/opsramp/gateway/' + res + '/cluster/AppMainUtil.java'
    os.makedirs(os.path.dirname(makeFile), exist_ok=True)

    with open(makeFile, "w") as f:
        f.write(appmainfiletemplateOutput)




def generateHandlerFile(env,appName,dm_dic,destination_path, current_path):

    handlerTemplate = env.get_template('GenericMessageHandler.java')
    handlerTemplateOutput = handlerTemplate.render(dm_dic=dm_dic)
    try:
        handleTemplateFile = destination_path + appName + '/core/src/main/java/com/opsramp/app/processor/handlers/GenericMessageHandler.java'
        os.makedirs(os.path.dirname(handleTemplateFile),exist_ok=True)

        with open(handleTemplateFile, "w") as f:
            f.write(handlerTemplateOutput)
    except Exception as e:
        print(e)




def generateDockerFile(env,appName,destination_path, current_path):
    #root
    dockerfiletemplate = env.get_template('Dockerfile')
    dockerfiletemplateOutput = dockerfiletemplate.render(appName=appName)
    dockerFile = destination_path + appName + '/Dockerfile'
    os.makedirs(os.path.dirname(dockerFile), exist_ok=True)

    with open(dockerFile, "w") as f:
        f.write(dockerfiletemplateOutput)
    #cluster-adapter

    dockerfiletemplate = env.get_template('Dockerfile')
    dockerfiletemplateOutput = dockerfiletemplate.render(appName=appName)
    dockerFile = destination_path + appName + '/Dockerfile'
    os.makedirs(os.path.dirname(dockerFile), exist_ok=True)



def generateMakeFile(env,appName,appVersion,destination_path, current_path):
    makefiletemplate = env.get_template('make.sh')
    makefiletemplateOutput = makefiletemplate.render(appName=appName,appVersion=appVersion)

    makeFile = destination_path + appName + '/make.sh'
    os.makedirs(os.path.dirname(makeFile), exist_ok=True)

    with open(makeFile, "w") as f:
        f.write(makefiletemplateOutput)


def generateHelmCharts(env,appName,appVersion,destination_path, current_path):
    # Copying Entire helm directoty

    if os.path.exists(destination_path + appName + '/cluster-adapter'):
        shutil.rmtree(destination_path + appName + '/cluster-adapter')
    shutil.copytree(current_path + '/templates/cluster-adapter/app-helm/mock-vcenter-tested/templates', destination_path + appName + '/cluster-adapter/app-helm/'+ appName+ '/templates')

    shutil.copy(current_path + '/templates/cluster-adapter/app-helm/mock-vcenter-tested/jvm.properties',
                    destination_path + appName + '/cluster-adapter/app-helm/' + appName + '/jvm.properties')
    # Replacing values yaml file
    chartValuetemplate = env.get_template('/cluster-adapter/app-helm/mock-vcenter-tested/values.yaml')
    chartValuetemplateOutput = chartValuetemplate.render(appName=appName)

    chartValueFile = destination_path + appName + '/cluster-adapter/app-helm/' + appName + '/values.yaml'
    os.makedirs(os.path.dirname(chartValueFile), exist_ok=True)

    with open(chartValueFile, "w") as f:
        f.write(chartValuetemplateOutput)

    # Replacing cluster yaml file
    chartClustertemplate = env.get_template('/cluster-adapter/app-helm/mock-vcenter-tested/cluster.yaml')
    chartClustertemplateOutput = chartClustertemplate.render(appName=appName)


    chartClusterFile = destination_path + appName + '/cluster-adapter/app-helm/' + appName + '/cluster.yaml'
    os.makedirs(os.path.dirname(chartClusterFile), exist_ok=True)

    with open(chartClusterFile, "w") as f:
        f.write(chartClustertemplateOutput)

    # Replacing chart file
    charttemplate = env.get_template('/cluster-adapter/app-helm/mock-vcenter-tested/Chart.yaml')
    charttemplateOutput = charttemplate.render(appName=appName, appVersion=appVersion)

    chartFile = destination_path + appName + '/cluster-adapter/app-helm/' + appName + '/Chart.yaml'
    os.makedirs(os.path.dirname(chartFile), exist_ok=True)

    with open(chartFile, "w") as f:
        f.write(charttemplateOutput)


def generatePomFiles(env,appName, appVersion,res,destination_path, current_path):

    clusterAdapterPomtemplate= env.get_template('/cluster-adapter/pom.xml')
    clusterAdapterPomtemplateOutput = clusterAdapterPomtemplate.render(appName=appName, appVersion=appVersion,res=res)

    clusterAdapterPomFile = destination_path + appName + '/cluster-adapter/pom.xml'
    os.makedirs(os.path.dirname(clusterAdapterPomFile), exist_ok=True)

    with open(clusterAdapterPomFile, "w") as f:
        f.write(clusterAdapterPomtemplateOutput)

    corePomtemplate = env.get_template('/static/core/pom.xml')
    corePomtemplateOutput = corePomtemplate.render(appName=appName, appVersion=appVersion)

    corePomFile = destination_path + appName + '/core/pom.xml'
    os.makedirs(os.path.dirname(corePomFile), exist_ok=True)

    with open(corePomFile, "w") as f:
        f.write(corePomtemplateOutput)

    classicPomtemplate = env.get_template('/static/classic-adapter/pom.xml')
    classicPomtemplateOutput = classicPomtemplate.render(appName=appName, appVersion=appVersion,res=res)

    classicPomFile = destination_path + appName + '/classic-adapter/pom.xml'
    os.makedirs(os.path.dirname(classicPomFile), exist_ok=True)

    with open(classicPomFile, "w") as f:
        f.write(classicPomtemplateOutput)

    rootPomtemplate = env.get_template('/root_pom.xml')
    rootPomtemplateOutput = rootPomtemplate.render(appName=appName, appVersion=appVersion)

    rootPomFile = destination_path + appName + '/pom.xml'
    os.makedirs(os.path.dirname(rootPomFile), exist_ok=True)

    with open(rootPomFile, "w") as f:
        f.write(rootPomtemplateOutput)
    shutil.copy(current_path + '/templates/static/classic-adapter/assembly.xml',
                    destination_path + appName + '/classic-adapter/assembly.xml')


def generateManifest(domainJson, manifestJsonTemplate,destination_path, current_path):
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
    #metadataObject['appName'] = domainJson['appName']
    #metadataObject['displayName'] = domainJson['appName']
    metadataObject['description'] = 'Sample app Integrates with sample vcenter APIs'
    metadataObject['version'] = '1.0.0'

    #categoriesArray = ['DISCOVERY AND MONITORING']
    #metadataObject['categories'] = categoriesArray
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

    try:
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
            metricObject['description'] = 'provides '+metric['name']
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
        requiredObject=[]
    for schema in domainJson['discoveryConfiguration']:
        propertyObject = {'type': schema['dataType']}
        propertiesObject[schema['propertyName']] = propertyObject

    schemaObject['properties'] = propertiesObject
    schemaObject['required'] = requiredObject
    schemaObject['type'] = "object"
    manifestObject['schema'] = schemaObject
    #print(schemaObject)

    uischemaObject = {}
    elementsObject = []
    notifylis = []
    for schema in domainJson['discoveryConfiguration']:
        if schema['propertyName'] =="alertConfiguration" or schema['propertyName'] =="alertSeverity" or schema['propertyName'] == "alertOnRootResource" or schema['propertyName'] =="alertSeverityMapping":
            notifylis.append(schema)
            continue
        try:
            OptionsObject={}
            OptionsObject["placeholder"] = schema["placeholder"]
            OptionsObject["credentialType"] = schema["credentialType"]
            OptionsObject["format"] = "credential"
        except KeyError:
            pass
        elementObject = {'type': "Control",'scope': '#/properties/' + schema['propertyName'],
                         'label': schema['label']}
        if len(OptionsObject) > 0:
            elementObject['options'] = OptionsObject

        elementsObject.append(elementObject)
    if len(notifylis)>0:
        notifyobject = getNotifyData(notifylis)
        elementsObject.append(notifyobject)
    uischemaObject['elements'] = elementsObject
    uischemaObject['type'] = "VerticalLayout"
    manifestObject['uischema'] = uischemaObject

    assetsObject['manifest'] = manifestObject

    specObject['assets'] = assetsObject
    versionObject["spec"] = specObject

    manifestJson["version"] = versionObject

    manifestFile = destination_path + domainJson['appName'] + '/cluster-adapter/production/manifest.json'
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
