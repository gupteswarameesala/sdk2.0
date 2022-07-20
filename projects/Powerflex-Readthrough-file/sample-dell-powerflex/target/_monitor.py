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

logger = logging.getLogger(__name__)

class TargetMonitoring:
    
    def process_DellPowerflexManager_metrics(self, requestContext):
        return None

    
    def process_DellPowerflexManagerServer_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                # resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                # system_data = Util().getResponse(requestContext, Constants.SYSTEM, moId, Constants.STATISTICS)
                _data = open('response-new/ManagedDevice_Instance.json')
                server_data = json.load(_data)
                if server_data != None:
                    for metric in metrics:
                        value = self.get_server_metrics(metric, server_data)
                        if value != None:
                            metric_data = {Constants.METRIC_NAME: metric, Constants.INSTANCE_VALUE: str(value),
                                           Constants.TIME_STAMP: Time().get_current_time()}
                            metrics_list.append(metric_data)

                    metric_map['data'] = metrics_list
                metric_list.append(metric_map)
            return metric_list
        except Exception as e:
            logger.exception(e)

    
    def process_DellPowerflexManagerSwitch_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                # resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                # system_data = Util().getResponse(requestContext, Constants.SYSTEM, moId, Constants.STATISTICS)
                _data = open('response-new/switch_instance.json')
                switch_data = json.load(_data)
                if switch_data != None:
                    for metric in metrics:
                        value = self.get_switch_metrics(metric, switch_data)
                        if value != None:
                            metric_data = {Constants.METRIC_NAME: metric, Constants.INSTANCE_VALUE: str(value),
                                           Constants.TIME_STAMP: Time().get_current_time()}
                            metrics_list.append(metric_data)

                    metric_map['data'] = metrics_list
                metric_list.append(metric_map)
            return metric_list
        except Exception as e:
            logger.exception(e)

    
    def process_DellPowerflexManagerVcenter_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                # resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                # system_data = Util().getResponse(requestContext, Constants.SYSTEM, moId, Constants.STATISTICS)
                _data = open('response-new/vcenter_instance.json')
                vcenter_data = json.load(_data)
                if vcenter_data != None:
                    for metric in metrics:
                        value = self.get_vcenter_metrics(metric, vcenter_data)
                        if value != None:
                            metric_data = {Constants.METRIC_NAME: metric, Constants.INSTANCE_VALUE: str(value),
                                           Constants.TIME_STAMP: Time().get_current_time()}
                            metrics_list.append(metric_data)

                    metric_map['data'] = metrics_list
                metric_list.append(metric_map)
            return metric_list
        except Exception as e:
            logger.exception(e)

    
    def process_DellPowerflexGateway_metrics(self, requestContext):
        try:
            metric_list = []
            for resourcesObject in requestContext.context.get(Constants.RESOURCES):
                # resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                # system_data = Util().getResponse(requestContext, Constants.SYSTEM, moId, Constants.STATISTICS)
                _data = open('response-new/System_Statistics.json')
                system_data = json.load(_data)
                if system_data != None:
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
                # resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                # sp_data = Util().getResponse(requestContext, Constants.STORAGE_POOL_NATIVE_TYPE, moId,Constants.STATISTICS)
                # logger.info("sp_data" + str(sp_data))
                _data = open('response-new/StoragePool_Statistics.json')
                sp_data = json.load(_data)
                # sp_state_data = Util().getResponse(requestContext, Constants.STORAGE_POOL_NATIVE_TYPE, moId)
                # logger.info("sp_state_data" + str(sp_state_data))
                _data = open('response-new/storage_pool_mdata.json')
                sp_state_data = json.load(_data)
                if sp_data != None and sp_state_data != None:
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
                # resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                '''mdm_data = Util().getResponse(requestContext, Constants.MDM)
                mdm_data = mdm_data[0]'''
                _data = open('response-new/system_cluster_mdata.json')
                mdm_data = json.load(_data)
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
                # resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                '''sdc_data = Util().getResponse(requestContext, Constants.SDC, moId)
                logger.info("sdc_data" + str(sdc_data))'''
                _data = open('response-new/sdc_mdata.json')
                sdc_data = json.load(_data)
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
                # resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                '''pd_data = Util().getResponse(requestContext, Constants.PROTECTION_DOMAIN, moId)
                logger.info("pd_data" + str(pd_data))'''
                _data = open('response-new/pd_mdata.json')
                pd_data = json.load(_data)
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
                # resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                '''sds_data = Util().getResponse(requestContext, Constants.SDS, moId)
                logger.info("sds_data" + str(sds_data))'''
                _data = open('response-new/sds_mdata.json')
                sds_data = json.load(_data)
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
                # resourcesObject = resource.get(Constants.RESOURCES)
                resourceId = resourcesObject.get(Constants.RESOURCE_ID)
                moId = resourcesObject.get(Constants.MOID)
                metric_map = {Constants.RESOURCE_ID: resourceId,
                              Constants.RESOURCETYPE: requestContext.context.get(Constants.NATIVE_TYPE),
                              Constants.TEMPLATE_ID: requestContext.context.get(Constants.TEMPLATE_ID),
                              Constants.MONITOR_ID: requestContext.context.get(Constants.MONITOR_ID)}
                metrics = requestContext.context.get(Constants.METRICS)
                metrics_list = []
                # device_data = Util().getResponse(requestContext, Constants.SDS, moId)
                _data = open('response-new/device_mdata.json')
                device_data = json.load(_data)
                # logger.info("device_data"+str(device_data))
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
        if getKeys(metric) is Constants.EMPTY_STRING:
            return
        else:
            if metric == Constants.SYSTEM_CAPACITY_UTILIZATION:
                max_capacity = system_data.get(Constants.MAX_CAPACITY)
                unused_capacity = system_data.get(Constants.UNUSED_CAPACITY)
                value = (unused_capacity * 100) // max_capacity

            elif metric == Constants.SYSTEM_TOTAL_USED_CAPACITY:
                max_capacity = system_data.get(Constants.MAX_CAPACITY)
                unused_capacity = system_data.get(Constants.UNUSED_CAPACITY)
                #print(max_capacity,unused_capacity)
                value = (max_capacity - unused_capacity) // factor

            else:
                logger.info( "  metric  " + str(metric) )
                pattern = Constants.START_PATTERN + getKeys(metric)
                logger.info("pattern    " + str(pattern))
                system_lis = get_pattern(pattern, system_data)
                logger.info("  data " + str(system_lis))
                if len(system_lis) > 0:
                    value = system_lis[0] // factor
                else:
                    return

            return value

    def get_sp_metrics(self,metric, sp_data):

        if getKeys(metric) is Constants.EMPTY_STRING:
            return
        else:
            pattern = Constants.START_PATTERN + getKeys(metric)
            sp_lis = get_pattern(pattern, sp_data)
            #logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data " + str(sp_lis))
            if len(sp_lis) > 0 :
                if metric == Constants.STOREAGE_POOL_STATE:
                    value = 0 if sp_lis[0] == Constants.NORMAL else 1
                else:
                    value = sp_lis[0] // factor
            else:
                return
            return value

    def get_mdm_metrics(self, metric, mdm_data):
        if getKeys(metric) is Constants.EMPTY_STRING:
            return
        pattern = Constants.MDM_PATTERN + getKeys(metric)
        mdm_lis = get_pattern(pattern, mdm_data)
        #logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data " + str(mdm_lis))
        if len(mdm_lis) > 0 and metric == Constants.MDM_CLUSTER_STATE_METRIC:
            value = 0 if mdm_lis[0] == Constants.CLUSTER_NORMAL else 1
        else:
            return
        return value

    def get_sdc_metrics(self,metric, sdc_data):
        if getKeys(metric) is Constants.EMPTY_STRING:
            return
        pattern = Constants.START_PATTERN + getKeys(metric)
        sdc_lis = get_pattern(pattern, sdc_data)
        #logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(sdc_lis))
        if len(sdc_lis) > 0 and metric == Constants.SDC_STATE_METRIC:
            value = 0 if sdc_lis[0] == Constants.CONNECTED else 1
        else:
            return
        return value

    def get_pd_metrics(self,metric, pd_data):
        if getKeys(metric) is Constants.EMPTY_STRING:
            return
        pattern = Constants.START_PATTERN + getKeys(metric)
        pd_lis = get_pattern(pattern, pd_data)
        #logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(pd_lis))
        if len(pd_lis) > 0 and metric == Constants.PROTECTION_DOMAIN_STATE_METRIC:
            value = 0 if pd_lis[0] == Constants.ACTIVE else 1
        else:
            return
        return value

    def get_sds_metrics(self,metric, sds_data):
        if getKeys(metric) is Constants.EMPTY_STRING:
            return
        pattern = Constants.START_PATTERN + getKeys(metric)
        sds_lis = get_pattern(pattern, sds_data)
        #logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(sds_lis))
        if len(sds_lis) > 0 and metric == Constants.SDS_STATE_METRIC:
            value = 0 if sds_lis[0] == Constants.NORMAL else 1
        else:
            return
        return value

    def get_device_metrics(self,metric,device_data):
        if getKeys(metric) is Constants.EMPTY_STRING:
            return
        pattern = Constants.START_PATTERN + getKeys(metric)
        device_lis = get_pattern(pattern, device_data)
        #logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(device_lis))
        if len(device_lis) > 0 and metric == Constants.DEVICE_STATE_METRIC:
            value = 0 if device_lis[0] == Constants.NORMAL else 1
        else:
            return
        return value

    def get_server_metrics(self,metric, server_data):
        if getKeys(metric) is Constants.EMPTY_STRING:
            return
        pattern = Constants.START_PATTERN + getKeys(metric)
        service_lis = get_pattern(pattern, server_data)
        #logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(device_lis))
        if len(service_lis) > 0 and metric == Constants.SERVER_STATE_METRIC:
            value = 1 if service_lis[0] == Constants.READY else 0
        elif len(service_lis) > 0 and metric == Constants.SERVER_COMPLIANCE_METRIC:
            value = 1 if service_lis[0] == Constants.COMPLIANT else 0
        elif len(service_lis) > 0 and metric == Constants.SERVER_MANAGED_STATE_METRIC:
            value = 1 if service_lis[0] == Constants.MANAGED else 0
        else:
            return
        return value

    def get_switch_metrics(self, metric, switch_data):
        if getKeys(metric) is Constants.EMPTY_STRING:
            return
        pattern = Constants.START_PATTERN + getKeys(metric)
        service_lis = get_pattern(pattern, switch_data)
        # logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(device_lis))
        if len(service_lis) > 0 and metric == Constants.SWITCH_STATE_METRIC:
            value = 1 if service_lis[0] == Constants.READY else 0
        elif len(service_lis) > 0 and metric == Constants.SWITCH_COMPLIANCE_METRIC:
            value = 1 if service_lis[0] == Constants.COMPLIANT else 0
        elif len(service_lis) > 0 and metric == Constants.SWITCH_MANAGED_STATE_METRIC:
            value = 1 if service_lis[0] == Constants.MANAGED else 0
        else:
            return
        return value

    def get_vcenter_metrics(self,metric, vcenter_data):
        if getKeys(metric) is Constants.EMPTY_STRING:
            return
        pattern = Constants.START_PATTERN + getKeys(metric)
        service_lis = get_pattern(pattern, vcenter_data)
        # logger.info("pattern    " + str(pattern) + "  metric  " + str(metric) + "  data" + str(device_lis))
        if len(service_lis) > 0 and metric == Constants.VCENTER_STATE_METRIC:
            value = 1 if service_lis[0] == Constants.READY else 0
        elif len(service_lis) > 0 and metric == Constants.VCENTER_COMPLIANCE_METRIC:
            value = 1 if service_lis[0] == Constants.COMPLIANT else 0
        elif len(service_lis) > 0 and metric == Constants.VCENTER_MANAGED_STATE_METRIC:
            value = 1 if service_lis[0] == Constants.MANAGED else 0
        else:
            return
        return value





