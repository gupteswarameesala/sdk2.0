import logging
import os
import requests
import json

logger = logging.getLogger(__name__)
def post_acknowledge(http_headers, s):
  
    logger.info("Post Acknowledgement.....")
    logger.info(http_headers)
    logger.info(s)
    logger.info(".....................")
    
    url = os.getenv('ADK_SERVICE_URI') + "/api/v2/messages/" + http_headers["AM-Message-Id"] + "?processInventory=" + s
    r = requests.put(url, headers=http_headers)
    if r.status_code == 200:
       logger.info("Acknowledge posted successfully.")
    else:
       logger.info("Acknowledge posted failed.")
    

def publish_resources(http_headers, resource_list):

    '''
    logger.info("Publish Resources")
    logger.info(http_headers)
    logger.info(resource_list)
    logger.info(".....................")
    '''
    url = os.getenv('ADK_SERVICE_URI') + "/api/v2/resources"
    r = requests.put(url, data=json.dumps(resource_list), headers=http_headers)
    if r.status_code == 200:
        logger.info("resources posted " + str(resource_list) + " with Poll Id " + str(
        http_headers["AM-Poll-Id"]))
    

def publish_relationships(http_headers, relationship_list):

    '''
    logger.info("Publish Relationships")
    logger.info(http_headers)
    logger.info(relationship_list)
    logger.info(".....................")
    '''
    url = os.getenv('ADK_SERVICE_URI') + "/api/v2/relationships"
    r = requests.put(url, data=json.dumps(relationship_list), headers=http_headers)
    if r.status_code == 200:
        logger.info("relationship list posted " + str(relationship_list) + " with Poll Id " + str(
        http_headers["AM-Poll-Id"]))
    


def publish_metrics(http_headers, metrics_map):

    '''
    logger.info("Publish Metrics")
    logger.info("headers")
    logger.info(http_headers)
    logger.info("metrics")
    logger.info(metrics_map)
    logger.info(".....................")

    '''
    url = os.getenv('ADK_SERVICE_URI') + "/api/v2/metrics?process=true"
    r = requests.post(url, data=json.dumps(metrics_map), headers=http_headers)
    if r.status_code == 200:
        logger.info("metrics posted " + str(metrics_map) + " with Poll Id " + str(
        http_headers["AM-Poll-Id"])) 
       

def post_monitoring_acknowledge(http_headers):

    '''
    logger.info("Publish Acknowledgment")
    logger.info(http_headers)
    logger.info(".....................")

    '''
    url = os.getenv('ADK_SERVICE_URI') + "/api/v2/messages/"+ http_headers["AM-Message-Id"]
    r = requests.put(url, headers=http_headers)
    if r.status_code == 200:
        logger.info("Acknowledge posted successfully.")
    else:
        logger.info("Acknowledge posted failed.")
    

def publish_alerts(http_headers, alert):

    '''
    logger.info("Publish Alerts")
    logger.info(http_headers)
    logger.info(alert)
    logger.info(".....................")

    '''
    url = os.getenv('ADK_SERVICE_URI') + "/api/v2/messages/outbound_channel/publish"
    status_code = requests.post(url, json.dumps(alert), http_headers)
    logger.info(json.dumps(alert))
    if status_code == 200:
        logger.info("alerts posted" + str(alert))
    else:
        logger.info("Acknowledge posted failed.")
        logger.info(str(status_code))
    

def publish_app_event(http_headers, app_event):

    '''
    logger.info("Publish events")
    logger.info(http_headers)
    logger.info(app_event)
    logger.info(".....................")

    '''
    url = os.getenv('ADK_SERVICE_URI') + "/api/v2/messages/outbound_channel/publish"
    status_code = requests.post(url, json.dumps(app_event), http_headers)
    logger.info(json.dumps(app_event))
    if status_code == 200:
        logger.info("App event posted" + str(app_event))
    else:
        logger.info("Acknowledge posted failed.")
        logger.info(str(status_code))
    