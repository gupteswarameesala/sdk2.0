import json

from core import  AbstractDiscovery
from httpclient import Url

import logging

from util import Util
from util.constants import Constants

logger = logging.getLogger(__name__)


class TargetDiscovery:
    

    def get_DellPowerflexSystem_data(self, requestContext,resource_type):
        try:
            system_list = []
            relation_list = []
            system_data = Util().getResponse(requestContext, Constants.SYSTEM)
            '''_data = open('response-new/mdm.json')
            system_data = json.load(_data)'''

            if system_data != None:
                requestContext.context[Constants.SYSTEM] = system_data
                for system_member in system_data:

                    system_map = {Constants.RESOURCETYPE: resource_type,
                                   Constants.NATIVE_TYPE: Constants.SYSTEM_NATIVE_TYPE,
                                   Constants.MOID: system_member.get(Constants.ID),
                                   Constants.HOST_NAME: system_member.get(Constants.NAME),
                                   Constants.RESOURCE_NAME: system_member.get(Constants.NAME)+Constants.HYPHEN+Constants.SYSTEM,
                                   Constants.SERIAL_NUMBER: system_member.get(Constants.SW_ID),
                                   Constants.MODEL: system_member.get(Constants.SYSTEM_VERSION_NAME),
                                   Constants.IPADDRESS: requestContext.context.get(Constants.DATA).get(Constants.IPADDRESS)}

                    system_list.append(system_map)
                return system_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None

    def get_DellPowerflexStoragePool_data(self, requestContext,resource_type):
        try:
            sp_list = []
            relation_list = []
            sp_data = Util().getResponse(requestContext, Constants.STORAGE_POOL)
            '''_data = open('response-new/storage_pool.json')
            sp_data = json.load(_data)'''
            if sp_data != None:
                requestContext.context[Constants.STORAGE_POOL] = sp_data
                for sp_member in sp_data:
                    sp_map = {Constants.RESOURCETYPE: resource_type,
                                  Constants.NATIVE_TYPE: Constants.STORAGE_POOL_NATIVE_TYPE,
                                  Constants.MOID: sp_member.get(Constants.ID),
                                  Constants.HOST_NAME: sp_member.get(Constants.NAME),
                                  Constants.RESOURCE_NAME: sp_member.get(Constants.NAME),
                                  Constants.MODEL: sp_member.get(Constants.MEDIATYPE)}

                    sp_list.append(sp_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(
                        Constants.PROTECTION_DOMAIN_NATIVE_TYPE)
                    if parent_resource_type != None:
                        relation_map = {Constants.TYPE: Constants.MEMBER_OF,
                                        Constants.SOURCE_MOID: sp_member.get(Constants.PROTECTION_DOMAIN_ID),
                                        Constants.TARGET_MOID: sp_member.get(Constants.ID)}
                        relation_list.append(relation_map)
                return sp_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexMdmCluster_data(self, requestContext,resource_type):
        try:
            cluster_list = []
            relation_list = []
            cluster_data = Util().getResponse(requestContext, Constants.MDM)
            '''_data = open('response-new/mdm.json')
            cluster_data = json.load(_data)'''
            if cluster_data != None:
                requestContext.context[Constants.MDM] = cluster_data
                for cluster_member in cluster_data:
                    cluster_map = {Constants.RESOURCETYPE: resource_type,
                                   Constants.NATIVE_TYPE: Constants.MDM_NATIVE_TYPE,
                                   Constants.MOID: cluster_member.get(Constants.MDM_CLUSTER).get(Constants.ID),
                                   Constants.HOST_NAME: cluster_member.get(Constants.MDM_CLUSTER).get(Constants.NAME),
                                   Constants.RESOURCE_NAME: cluster_member.get(Constants.MDM_CLUSTER).get(Constants.NAME)+Constants.HYPHEN+Constants.MDM,
                                   Constants.MODEL: cluster_member.get(Constants.MDM_CLUSTER).get(Constants.MASTER).get(Constants.VERSION_INFO),
                                   Constants.IPADDRESS: cluster_member.get(Constants.MDM_CLUSTER).get(Constants.MASTER).get(Constants.MANAGEMENT_IP)[0]}

                    cluster_list.append(cluster_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(Constants.SYSTEM_NATIVE_TYPE)
                    if parent_resource_type != None:

                        relation_map = {Constants.TYPE: Constants.MEMBER_OF, Constants.SOURCE_MOID: cluster_member.get(Constants.ID),
                                        Constants.TARGET_MOID: cluster_member.get(Constants.MDM_CLUSTER).get(Constants.ID)}
                        relation_list.append(relation_map)
                return cluster_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexSdc_data(self, requestContext,resource_type):
        try:
            sdc_list = []
            relation_list = []
            sdc_data = Util().getResponse(requestContext, Constants.SDC)
            '''_data = open('response-new/sdc.json')
            sdc_data = json.load(_data)'''
            if sdc_data != None:
                requestContext.context[Constants.SDC] = sdc_data
                for sdc_member in sdc_data:
                    sdc_map = {Constants.RESOURCETYPE: resource_type,
                                   Constants.NATIVE_TYPE: Constants.SDC_NATIVE_TYPE,
                                   Constants.MOID: sdc_member.get(Constants.ID),
                                   Constants.HOST_NAME: sdc_member.get(Constants.NAME),
                                   Constants.RESOURCE_NAME: sdc_member.get(Constants.NAME),
                                   Constants.IPADDRESS: sdc_member.get(Constants.SDC_IP),
                                   Constants.MODEL: sdc_member.get(Constants.VERSION_INFO),
                                   Constants.OS : sdc_member.get(Constants.OS_TYPE),
                                   Constants.TAGS: {
                                       Constants.SDC_TYPE : sdc_member.get(Constants.SDC_TYPE)}}

                    sdc_list.append(sdc_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(Constants.SYSTEM_NATIVE_TYPE)
                    if parent_resource_type != None:

                        relation_map = {Constants.TYPE: Constants.COMPONENT_OF, Constants.SOURCE_MOID: sdc_member.get(Constants.SYSTEM_ID),
                                        Constants.TARGET_MOID: sdc_member.get(Constants.ID)}
                        relation_list.append(relation_map)
                return sdc_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexProtectionDomain_data(self, requestContext,resource_type):
        try:
            pd_list = []
            relation_list = []
            pd_data = Util().getResponse(requestContext, Constants.PROTECTION_DOMAIN)
            '''_data = open('response-new/pd.json')
            pd_data = json.load(_data)'''
            if pd_data != None:
                requestContext.context[Constants.PROTECTION_DOMAIN] = pd_data
                for pd_member in pd_data:
                    pd_map = {Constants.RESOURCETYPE: resource_type,
                               Constants.NATIVE_TYPE: Constants.PROTECTION_DOMAIN_NATIVE_TYPE,
                               Constants.MOID: pd_member.get(Constants.ID),
                               Constants.HOST_NAME: pd_member.get(Constants.NAME),
                               Constants.RESOURCE_NAME: pd_member.get(Constants.NAME)}


                    pd_list.append(pd_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(
                        Constants.SYSTEM_NATIVE_TYPE)
                    if parent_resource_type != None:
                        relation_map = {Constants.TYPE: Constants.COMPONENT_OF,
                                        Constants.SOURCE_MOID: pd_member.get(Constants.SYSTEM_ID),
                                        Constants.TARGET_MOID: pd_member.get(Constants.ID)}
                        relation_list.append(relation_map)
                return pd_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexSds_data(self, requestContext,resource_type):
        try:
            sds_list = []
            relation_list = []
            sds_data = Util().getResponse(requestContext, Constants.SDS)
            '''_data = open('response-new/sds.json')
            sds_data = json.load(_data)'''
            if sds_data != None:
                requestContext.context[Constants.SDS] = sds_data
                for sds_member in sds_data:
                    sds_map = {Constants.RESOURCETYPE: resource_type,
                              Constants.NATIVE_TYPE: Constants.SDS_NATIVE_TYPE,
                              Constants.MOID: sds_member.get(Constants.ID),
                              Constants.HOST_NAME: sds_member.get(Constants.NAME),
                              Constants.RESOURCE_NAME: sds_member.get(Constants.NAME),
                              Constants.MODEL: sds_member.get(Constants.SOFT_VERSION_INFO),
                              Constants.TAGS: {
                                   Constants.PORT: sds_member.get(Constants.PORT)}}

                    sds_list.append(sds_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(
                        Constants.PROTECTION_DOMAIN_NATIVE_TYPE)
                    if parent_resource_type != None:
                        relation_map = {Constants.TYPE: Constants.MEMBER_OF,
                                        Constants.SOURCE_MOID: sds_member.get(Constants.PROTECTION_DOMAIN_ID),
                                        Constants.TARGET_MOID: sds_member.get(Constants.ID)}
                        relation_list.append(relation_map)
                return sds_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexDevice_data(self, requestContext,resource_type):
        try:
            device_list = []
            relation_list = []
            device_data = Util().getResponse(requestContext, Constants.DEVICE)
            '''_data = open("response-new/device.json")
            device_data = json.load(_data)'''

            if device_data != None:
                requestContext.context[Constants.DEVICE] = device_data
                for device_member in device_data:

                    device_map = {Constants.RESOURCETYPE: resource_type,
                               Constants.NATIVE_TYPE: Constants.DEVICE_NATIVE_TYPE,
                               Constants.MOID: device_member.get(Constants.ID),
                               Constants.HOST_NAME: device_member.get(Constants.NAME),
                               Constants.RESOURCE_NAME: device_member.get(Constants.NAME),
                               Constants.MODEL: device_member.get(Constants.MODEL_NAME),
                               Constants.SERIAL_NUMBER: device_member.get(Constants.SERIAL_NUMBER),
                               Constants.TAGS: {
                                   Constants.MEDIA_TYPE: device_member.get(Constants.MEDIATYPE),
                                   Constants.DEVICE_TYPE: device_member.get(Constants.DEVICETYPE),
                                   Constants.VENDOR_NAME:device_member.get(Constants.VENDORNAME)
                              }}

                    device_list.append(device_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(
                        Constants.STORAGE_POOL_NATIVE_TYPE)
                    if parent_resource_type != None:
                        relation_map = {Constants.TYPE: Constants.MEMBER_OF,
                                        Constants.SOURCE_MOID: device_member.get(Constants.STORAGEPOOL_ID),
                                        Constants.TARGET_MOID: device_member.get(Constants.ID)}
                        relation_list.append(relation_map)
                return device_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexVolume_data(self, requestContext,resource_type):
        try:
            volume_list = []
            relation_list = []
            volume_data = Util().getResponse(requestContext, Constants.VOLUME)
            '''_data = open('response-new/volume.json')
            volume_data = json.load(_data)'''
            if volume_data != None:
                requestContext.context[Constants.VOLUME] = volume_data
                for volume_member in volume_data:
                    volume_map = {Constants.RESOURCETYPE: resource_type,
                                  Constants.NATIVE_TYPE: Constants.VOLUME_NATIVE_TYPE,
                                  Constants.MOID: volume_member.get(Constants.ID),
                                  Constants.HOST_NAME: volume_member.get(Constants.NAME),
                                  Constants.RESOURCE_NAME: volume_member.get(Constants.NAME),
                                  Constants.TAGS: {
                                      Constants.SIZE_IN_KB: volume_member.get(Constants.SIZE),
                                      Constants.VOLUME_TYPE: volume_member.get(Constants.VOLUMETYPE)

                                  }}

                    volume_list.append(volume_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(
                        Constants.STORAGE_POOL_NATIVE_TYPE)
                    if parent_resource_type != None:
                        relation_map = {Constants.TYPE: Constants.MEMBER_OF,
                                        Constants.SOURCE_MOID: volume_member.get(Constants.STORAGEPOOL_ID),
                                        Constants.TARGET_MOID: volume_member.get(Constants.ID)}
                        relation_list.append(relation_map)
                return volume_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexVtree_data(self, requestContext,resource_type):
        return None,None
    
