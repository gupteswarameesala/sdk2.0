import datetime
import json

import requests

from core import Time
from httpclient import Url
import logging

from util import Util
from util.baseutil import getKeys, get_pattern
from util.constants import Constants

logger = logging.getLogger(__name__)

factor = 1048576.0


class TargetMonitoring:

    def process_DellPowerflexSystem_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                #resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                system_data = Util().getResponse(requestContext, Constants.SYSTEM, moId, Constants.STATISTICS)
                '''_data = open('resources/System_Statistics.json')
                system_data = json.load(_data)'''
                for metric in metrics:
                    value = self.get_system_metrics(metric, system_data)
                    if value != None:
                        metric_data = {Constants.METRIC_NAME: metric, Constants.INSTANCE_VALUE: str(value),
                                       Constants.TIME_STAMP: Time().get_current_time()}
                        metrics_list.append(metric_data)

                metric_map['data'] = metrics_list
                metric_list.append(metric_map)
            return metric_list
        except Exception as e:
            logger.exception(e)

    def process_DellPowerflexStoragePool_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                #resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                sp_data = Util().getResponse(requestContext, Constants.STORAGE_POOL_NATIVE_TYPE, moId,Constants.STATISTICS)
                logger.info("sp_data" + str(sp_data))
                '''_data = open('resources/System_Statistics.json')
                sp_data = json.load(_data)'''
                sp_state_data = Util().getResponse(requestContext, Constants.STORAGE_POOL_NATIVE_TYPE, moId)
                logger.info("sp_state_data" + str(sp_state_data))
                '''_data = open('response-new/storage_pool_mdata.json')
                sp_state_data = json.load(_data)'''
                for metric in metrics:
                    if metric == Constants.STOREAGE_POOL_STATE:
                        value = self.get_sp_metrics(metric, sp_state_data)
                    else:
                        value = self.get_sp_metrics(metric, sp_data)
                    if value != None:
                        metric_data = {Constants.METRIC_NAME: metric, Constants.INSTANCE_VALUE: str(value),
                                       Constants.TIME_STAMP: Time().get_current_time()}
                        metrics_list.append(metric_data)

                metric_map['data'] = metrics_list
                metric_list.append(metric_map)
            return metric_list
        except Exception as e:
            logger.exception(e)

    def process_DellPowerflexMdmCluster_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                #resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                mdm_data = Util().getResponse(requestContext, Constants.MDM)
                mdm_data = mdm_data[0]
                '''_data = open('response-new/system_cluster_mdata.json')
                mdm_data = json.load(_data)'''
                if mdm_data != None:
                    for metric in metrics:
                        value = self.get_mdm_metrics(metric, mdm_data)
                        if value != None:
                            metric_data = {Constants.METRIC_NAME: metric, Constants.INSTANCE_VALUE: str(value),
                                           Constants.TIME_STAMP: Time().get_current_time()}
                            metrics_list.append(metric_data)

                    metric_map['data'] = metrics_list
                metric_list.append(metric_map)
            return metric_list
        except Exception as e:
            logger.exception(e)
        return None

    def process_DellPowerflexSdc_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                #resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                sdc_data = Util().getResponse(requestContext, Constants.SDC, moId)
                logger.info("sdc_data" + str(sdc_data))
                '''_data = open('response-new/sdc_mdata.json')
                sdc_data = json.load(_data)'''
                if sdc_data != None:
                    for metric in metrics:
                        value = self.get_sdc_metrics(metric, sdc_data)
                        if value != None:
                            metric_data = {Constants.METRIC_NAME: metric, Constants.INSTANCE_VALUE: str(value),
                                           Constants.TIME_STAMP: Time().get_current_time()}
                            metrics_list.append(metric_data)

                    metric_map['data'] = metrics_list
                metric_list.append(metric_map)
            return metric_list
        except Exception as e:
            logger.exception(e)
        return None

    def process_DellPowerflexProtectionDomain_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                #resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                pd_data = Util().getResponse(requestContext, Constants.PROTECTION_DOMAIN, moId)
                logger.info("pd_data" + str(pd_data))
                '''_data = open('response-new/pd_mdata.json')
                pd_data = json.load(_data)'''
                if pd_data != None:
                    for metric in metrics:
                        value = self.get_pd_metrics(metric, pd_data)
                        if value != None:
                            metric_data = {Constants.METRIC_NAME: metric, Constants.INSTANCE_VALUE: str(value),
                                           Constants.TIME_STAMP: Time().get_current_time()}
                            metrics_list.append(metric_data)

                    metric_map['data'] = metrics_list
                metric_list.append(metric_map)
            return metric_list
        except Exception as e:
            logger.exception(e)
        return None

    def process_DellPowerflexSds_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                #resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                sds_data = Util().getResponse(requestContext, Constants.SDS, moId)
                logger.info("sds_data" + str(sds_data))
                '''_data = open('response-new/sds_mdata.json')
                sds_data = json.load(_data)'''
                if sds_data != None:
                    for metric in metrics:
                        value = self.get_sds_metrics(metric, sds_data)
                        if value != None:
                            metric_data = {Constants.METRIC_NAME: metric, Constants.INSTANCE_VALUE: str(value),
                                           Constants.TIME_STAMP: Time().get_current_time()}
                            metrics_list.append(metric_data)

                    metric_map['data'] = metrics_list
                metric_list.append(metric_map)
            return metric_list
        except Exception as e:
            logger.exception(e)
        return None

    def process_DellPowerflexDevice_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                #resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                device_data = Util().getResponse(requestContext, Constants.SDS, moId)
                '''_data = open('response-new/device_mdata.json')
                device_data = json.load(_data)'''
                logger.info("device_data"+str(device_data))
                if device_data != None:
                    for metric in metrics:
                        value = self.get_device_metrics(metric, device_data)
                        if value != None:
                            metric_data = {Constants.METRIC_NAME: metric, Constants.INSTANCE_VALUE: str(value),
                                           Constants.TIME_STAMP: Time().get_current_time()}
                            metrics_list.append(metric_data)

                    metric_map['data'] = metrics_list
                metric_list.append(metric_map)
            return metric_list
        except Exception as e:
            logger.exception(e)
        return None

    def process_DellPowerflexVolume_metrics(self, requestContext):
        return None

    def process_DellPowerflexVtree_metrics(self, requestContext):
        return None

    def get_system_metrics(self, metric, system_data):
        if metric == Constants.SYSTEM_CAPACITY_UTILIZATION:
            max_capacity = system_data.get(Constants.MAX_CAPACITY)
            unused_capacity = system_data.get(Constants.UNUSED_CAPACITY)
            value = (unused_capacity * 100) // max_capacity

        elif metric == Constants.SYSTEM_TOTAL_USED_CAPACITY:
            max_capacity = system_data.get(Constants.MAX_CAPACITY)
            unused_capacity = system_data.get(Constants.UNUSED_CAPACITY)
            print(max_capacity,unused_capacity)
            value = (max_capacity - unused_capacity) // factor


        else:

            pattern = Constants.START_PATTERN + getKeys(metric)
            system_lis = get_pattern(pattern, system_data)
            if len(system_lis) > 0:
                value = system_lis[0] // factor
            else:
                return

        return value

    def get_sp_metrics(self,metric, sp_data):

        pattern = Constants.START_PATTERN + getKeys(metric)
        sp_lis = get_pattern(pattern, sp_data)
        logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(sp_lis))
        if len(sp_lis) > 0 :
            if metric == Constants.STOREAGE_POOL_STATE:
                value = 0 if sp_lis[0] == Constants.NORMAL else 1
            else:
                value = sp_lis[0] // factor
        else:
            return
        return value

    def get_mdm_metrics(self, metric, mdm_data):
        pattern = Constants.MDM_PATTERN + getKeys(metric)
        mdm_lis = get_pattern(pattern, mdm_data)
        if len(mdm_lis) > 0 and metric == Constants.MDM_CLUSTER_STATE_METRIC:
            value = 0 if mdm_lis[0] == Constants.CLUSTER_NORMAL else 1
        else:
            return
        return value

    def get_sdc_metrics(self,metric, sdc_data):
        pattern = Constants.START_PATTERN + getKeys(metric)
        sdc_lis = get_pattern(pattern, sdc_data)
        logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(sdc_lis))
        if len(sdc_lis) > 0 and metric == Constants.SDC_STATE_METRIC:
            value = 0 if sdc_lis[0] == Constants.CONNECTED else 1
        else:
            return
        return value

    def get_pd_metrics(self,metric, pd_data):
        pattern = Constants.START_PATTERN + getKeys(metric)
        pd_lis = get_pattern(pattern, pd_data)
        logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(pd_lis))
        if len(pd_lis) > 0 and metric == Constants.PROTECTION_DOMAIN_STATE_METRIC:
            value = 0 if pd_lis[0] == Constants.ACTIVE else 1
        else:
            return
        return value

    def get_sds_metrics(self,metric, sds_data):
        pattern = Constants.START_PATTERN + getKeys(metric)
        sds_lis = get_pattern(pattern, sds_data)
        logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(sds_lis))
        if len(sds_lis) > 0 and metric == Constants.SDS_STATE_METRIC:
            value = 0 if sds_lis[0] == Constants.NORMAL else 1
        else:
            return
        return value

    def get_device_metrics(self,metric,device_data):
        pattern = Constants.START_PATTERN + getKeys(metric)
        device_lis = get_pattern(pattern, device_data)
        logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(device_lis))
        if len(device_lis) > 0 and metric == Constants.DEVICE_STATE_METRIC:
            value = 0 if device_lis[0] == Constants.NORMAL else 1
        else:
            return
        return value



