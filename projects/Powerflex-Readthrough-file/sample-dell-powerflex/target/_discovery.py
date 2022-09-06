import json

from core import AbstractDiscovery
from httpclient import Url

import logging

from util import Util
from util.constants import Constants

logger = logging.getLogger(__name__)


class TargetDiscovery:
    

    def get_DellPowerflexManager_data(self, requestContext,resource_type):
        try:
            md_list = []
            relation_list = []
            # system_data = Util().getResponse(requestContext, Constants.SYSTEM)
            md_map = {Constants.RESOURCETYPE: resource_type,
                      Constants.NATIVE_TYPE: Constants.MANAGER_NATIVE_TYPE,
                      Constants.MOID: requestContext.context.get(Constants.DATA).get(
                                      Constants.MANAGER_IP_ADDRESS),
                      Constants.HOST_NAME: Constants.MANAGER_NATIVE_TYPE,
                      Constants.RESOURCE_NAME: Constants.MANAGER_NATIVE_TYPE ,
                      Constants.HAS_RELATION: Constants.TRUE,
                      Constants.IPADDRESS: requestContext.context.get(Constants.DATA).get(
                                      Constants.MANAGER_IP_ADDRESS)
                      }
            requestContext.context[Constants.ROOT_MOID] = requestContext.context.get(Constants.DATA).get(
                                      Constants.MANAGER_IP_ADDRESS)
            tags = {}
            md_map.update({Constants.TAGS: tags})

            md_list.append(md_map)
            return md_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexManagerServer_data(self, requestContext,resource_type):
        try:
            server_list,relation_list = self.get_managedDeviceResources(requestContext,resource_type,Constants.SERVER_NATIVE_TYPE)
            return server_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexManagerSwitch_data(self, requestContext,resource_type):
        try:
            switch_list,relation_list = self.get_managedDeviceResources(requestContext,resource_type,Constants.SWITCH_NATIVE_TYPE)
            return switch_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexManagerVcenter_data(self, requestContext,resource_type):
        try:
            vcenter_list,relation_list = self.get_managedDeviceResources(requestContext,resource_type,Constants.VCENTER_NATIVE_TYPE)

            return vcenter_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexGateway_data(self, requestContext,resource_type):
        try:
            system_list = []
            relation_list = []
            # system_data = Util().getResponse(requestContext, Constants.SYSTEM)
            _data = open('response-new/mdm.json')
            system_data = json.load(_data)

            if system_data != None:
                requestContext.context[Constants.SYSTEM] = system_data
                for system_member in system_data:
                    system_map = {Constants.RESOURCETYPE: resource_type,
                                  Constants.NATIVE_TYPE: Constants.SYSTEM_NATIVE_TYPE,
                                  Constants.MOID: system_member.get(Constants.ID),
                                  Constants.HOST_NAME: system_member.get(Constants.NAME),
                                  Constants.RESOURCE_NAME: system_member.get(
                                      Constants.NAME) + Constants.HYPHEN + Constants.SYSTEM,
                                  Constants.SERIAL_NUMBER: system_member.get(Constants.SW_ID),
                                  Constants.MODEL: system_member.get(Constants.SYSTEM_VERSION_NAME),
                                  Constants.HAS_RELATION: Constants.TRUE,
                                  Constants.IPADDRESS: requestContext.context.get(Constants.DATA).get(
                                      Constants.IPADDRESS)}

                    system_list.append(system_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(
                        Constants.MANAGER_NATIVE_TYPE)
                    if parent_resource_type != None:
                        relation_map = {Constants.TYPE: Constants.MEMBER_OF,
                                        Constants.SOURCE_MOID: requestContext.context.get(Constants.ROOT_MOID),
                                        Constants.TARGET_MOID: system_member.get(Constants.ID)}
                        relation_list.append(relation_map)
                return system_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None
    

    def get_DellPowerflexStoragePool_data(self, requestContext, resource_type):
        try:
            sp_list = []
            relation_list = []
            # sp_data = Util().getResponse(requestContext, Constants.STORAGE_POOL)
            _data = open('response-new/storage_pool.json')
            sp_data = json.load(_data)
            if sp_data != None:
                requestContext.context[Constants.STORAGE_POOL] = sp_data
                for sp_member in sp_data:
                    sp_map = {Constants.RESOURCETYPE: resource_type,
                              Constants.NATIVE_TYPE: Constants.STORAGE_POOL_NATIVE_TYPE,
                              Constants.MOID: sp_member.get(Constants.ID),
                              Constants.HOST_NAME: sp_member.get(Constants.NAME),
                              Constants.RESOURCE_NAME: sp_member.get(Constants.NAME),
                              Constants.HAS_RELATION: Constants.TRUE,
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

    def get_DellPowerflexMdmCluster_data(self, requestContext, resource_type):
        try:
            cluster_list = []
            relation_list = []
            # cluster_data = Util().getResponse(requestContext, Constants.MDM)
            _data = open('response-new/mdm.json')
            cluster_data = json.load(_data)
            if cluster_data != None:
                requestContext.context[Constants.MDM] = cluster_data
                for cluster_member in cluster_data:
                    cluster_map = {Constants.RESOURCETYPE: resource_type,
                                   Constants.NATIVE_TYPE: Constants.MDM_NATIVE_TYPE,
                                   Constants.MOID: cluster_member.get(Constants.MDM_CLUSTER).get(Constants.ID),
                                   Constants.HOST_NAME: cluster_member.get(Constants.MDM_CLUSTER).get(
                                       Constants.NAME),
                                   Constants.RESOURCE_NAME: cluster_member.get(Constants.MDM_CLUSTER).get(
                                       Constants.NAME) + Constants.HYPHEN + Constants.MDM,
                                   Constants.HAS_RELATION: Constants.TRUE,
                                   Constants.MODEL: cluster_member.get(Constants.MDM_CLUSTER).get(
                                       Constants.MASTER).get(Constants.VERSION_INFO),
                                   Constants.IPADDRESS:
                                       cluster_member.get(Constants.MDM_CLUSTER).get(Constants.MASTER).get(
                                           Constants.MANAGEMENT_IP)[0]}

                    cluster_list.append(cluster_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(
                        Constants.SYSTEM_NATIVE_TYPE)
                    if parent_resource_type != None:
                        relation_map = {Constants.TYPE: Constants.MEMBER_OF,
                                        Constants.SOURCE_MOID: cluster_member.get(Constants.ID),
                                        Constants.TARGET_MOID: cluster_member.get(Constants.MDM_CLUSTER).get(
                                            Constants.ID)}
                        relation_list.append(relation_map)
                return cluster_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None

    def get_DellPowerflexSdc_data(self, requestContext, resource_type):
        try:
            sdc_list = []
            relation_list = []
            # sdc_data = Util().getResponse(requestContext, Constants.SDC)
            _data = open('response-new/sdc.json')
            sdc_data = json.load(_data)
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
                               Constants.HAS_RELATION: Constants.TRUE,
                               Constants.OS: sdc_member.get(Constants.OS_TYPE),
                               Constants.TAGS: {
                                   Constants.SDC_TYPE: sdc_member.get(Constants.SDC_TYPE)}}

                    sdc_list.append(sdc_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(
                        Constants.SYSTEM_NATIVE_TYPE)
                    if parent_resource_type != None:
                        relation_map = {Constants.TYPE: Constants.COMPONENT_OF,
                                        Constants.SOURCE_MOID: sdc_member.get(Constants.SYSTEM_ID),
                                        Constants.TARGET_MOID: sdc_member.get(Constants.ID)}
                        relation_list.append(relation_map)
                return sdc_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None


    def get_DellPowerflexProtectionDomain_data(self, requestContext, resource_type):
            try:
                pd_list = []
                relation_list = []
                # pd_data = Util().getResponse(requestContext, Constants.PROTECTION_DOMAIN)
                _data = open('response-new/pd.json')
                pd_data = json.load(_data)
                if pd_data != None:
                    requestContext.context[Constants.PROTECTION_DOMAIN] = pd_data
                    for pd_member in pd_data:
                        pd_map = {Constants.RESOURCETYPE: resource_type,
                                  Constants.NATIVE_TYPE: Constants.PROTECTION_DOMAIN_NATIVE_TYPE,
                                  Constants.MOID: pd_member.get(Constants.ID),
                                  Constants.HOST_NAME: pd_member.get(Constants.NAME),
                                  Constants.RESOURCE_NAME: pd_member.get(Constants.NAME),
                                  Constants.HAS_RELATION: Constants.TRUE,
                                  }

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


    def get_DellPowerflexSds_data(self, requestContext, resource_type):
            try:
                sds_list = []
                relation_list = []
                # sds_data = Util().getResponse(requestContext, Constants.SDS)
                _data = open('response-new/sds.json')
                sds_data = json.load(_data)
                if sds_data != None:
                    requestContext.context[Constants.SDS] = sds_data
                    for sds_member in sds_data:
                        sds_map = {Constants.RESOURCETYPE: resource_type,
                                   Constants.NATIVE_TYPE: Constants.SDS_NATIVE_TYPE,
                                   Constants.MOID: sds_member.get(Constants.ID),
                                   Constants.HOST_NAME: sds_member.get(Constants.NAME),
                                   Constants.RESOURCE_NAME: sds_member.get(Constants.NAME),
                                   Constants.HAS_RELATION: Constants.TRUE,
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

    def get_DellPowerflexDevice_data(self, requestContext, resource_type):
        try:
            device_list = []
            relation_list = []
            # device_data = Util().getResponse(requestContext, Constants.DEVICE)
            _data = open("response-new/device.json")
            device_data = json.load(_data)

            if device_data != None:
                requestContext.context[Constants.DEVICE] = device_data
                for device_member in device_data:

                    device_map = {Constants.RESOURCETYPE: resource_type,
                                  Constants.NATIVE_TYPE: Constants.DEVICE_NATIVE_TYPE,
                                  Constants.MOID: device_member.get(Constants.ID),
                                  Constants.HOST_NAME: device_member.get(Constants.NAME),
                                  Constants.HAS_RELATION: Constants.TRUE,
                                  Constants.RESOURCE_NAME: device_member.get(Constants.NAME),
                                  Constants.MODEL: device_member.get(Constants.MODEL_NAME),
                                  Constants.SERIAL_NUMBER: device_member.get(Constants.SERIAL_NUMBER),
                                  Constants.TAGS: {
                                      Constants.MEDIA_TYPE: device_member.get(Constants.MEDIATYPE),
                                      Constants.DEVICE_TYPE: device_member.get(Constants.DEVICETYPE),
                                      Constants.VENDOR_NAME: device_member.get(Constants.VENDORNAME)
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


    def get_DellPowerflexVolume_data(self, requestContext, resource_type):
        try:
            volume_list = []
            relation_list = []
            # volume_data = Util().getResponse(requestContext, Constants.VOLUME)
            _data = open('response-new/volume.json')
            volume_data = json.load(_data)
            if volume_data != None:
                requestContext.context[Constants.VOLUME] = volume_data
                for volume_member in volume_data:
                    volume_map = {Constants.RESOURCETYPE: resource_type,
                                  Constants.NATIVE_TYPE: Constants.VOLUME_NATIVE_TYPE,
                                  Constants.MOID: volume_member.get(Constants.ID),
                                  Constants.HAS_RELATION: Constants.TRUE,
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

    def get_DellPowerflexVtree_data(self, requestContext, resource_type):
        try:
            vtree_list = []
            relation_list = []
            # volume_data = Util().getResponse(requestContext, Constants.VOLUME)
            _data = open('response-new/VTree.json')
            vtree_data = json.load(_data)
            if vtree_data != None:
                requestContext.context[Constants.VOLUME] = vtree_data
                for vtree_member in vtree_data:
                    vtree_map = {Constants.RESOURCETYPE: resource_type,
                                 Constants.NATIVE_TYPE: Constants.VTREE_NATIVE_TYPE,
                                 Constants.MOID: vtree_member.get(Constants.ID),
                                 Constants.HOST_NAME: vtree_member.get(Constants.NAME),
                                 Constants.HAS_RELATION: Constants.TRUE,
                                 Constants.RESOURCE_NAME: vtree_member.get(Constants.NAME),
                                 Constants.TAGS: {

                                 }}

                    vtree_list.append(vtree_map)
                    parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(
                        Constants.STORAGE_POOL_NATIVE_TYPE)
                    if parent_resource_type != None:
                        relation_map = {Constants.TYPE: Constants.MEMBER_OF,
                                        Constants.SOURCE_MOID: vtree_member.get(Constants.STORAGEPOOL_ID),
                                        Constants.TARGET_MOID: vtree_member.get(Constants.ID)}
                        relation_list.append(relation_map)
                return vtree_list, relation_list
        except Exception as e:
            logger.exception(e)
        return None, None

    def get_managedDeviceResources(self,requestContext,resource_type,native_type):
        md_list = []
        relation_list = []
        # system_data = Util().getResponse(requestContext, Constants.SYSTEM)
        _data = open('response-new/ManagedDevice.json')
        md_data = json.load(_data)
        if md_data != None:
            requestContext.context[Constants.MANAGED_SWITCH] = md_data
            for md_member in md_data:
                if md_member.get(Constants.DEVICETYPE) is None or md_member.get(Constants.REF_ID) is None:
                    continue
                if Constants.SERVER in md_member.get(Constants.DEVICETYPE).lower() and native_type == Constants.SERVER_NATIVE_TYPE:
                    NATIVE_TYPE  = Constants.SERVER_NATIVE_TYPE
                elif Constants.SWITCH in md_member.get(Constants.DEVICETYPE).lower() and native_type == Constants.SWITCH_NATIVE_TYPE:
                    NATIVE_TYPE = Constants.SWITCH_NATIVE_TYPE
                elif Constants.VCENTER in md_member.get(
                        Constants.DEVICETYPE).lower() and native_type == Constants.VCENTER_NATIVE_TYPE:
                    NATIVE_TYPE = Constants.VCENTER_NATIVE_TYPE
                else:
                    continue

                md_map = {Constants.RESOURCETYPE: resource_type,
                          Constants.NATIVE_TYPE: NATIVE_TYPE,
                          Constants.MOID: md_member.get(Constants.REF_ID),
                          Constants.HOST_NAME: md_member.get(Constants.HOST_NAME) if md_member.get(
                              Constants.HOST_NAME) is not None else Constants.EMPTY_STRING,
                          Constants.RESOURCE_NAME: md_member.get(Constants.DISPLAY_NAME) if md_member.get(
                              Constants.DISPLAY_NAME) is not None else Constants.EMPTY_STRING,
                          Constants.OS: md_member.get(Constants.MANAGED_DEVICE_OS) if md_member.get(
                              Constants.MANAGED_DEVICE_OS) is not None else Constants.EMPTY_STRING,
                          Constants.MAKE: md_member.get(Constants.MANUFACTURER) if md_member.get(
                              Constants.MANUFACTURER) is not None else Constants.EMPTY_STRING,
                          Constants.MODEL: md_member.get(Constants.MODEL) if md_member.get(
                              Constants.MODEL) is not None else Constants.EMPTY_STRING,
                          # Constants.HAS_RELATION: Constants.FALSE,
                          Constants.IPADDRESS: md_member.get(Constants.IPADDRESS) if md_member.get(
                              Constants.IPADDRESS) is not None else Constants.EMPTY_STRING,
                          Constants.HAS_RELATION: Constants.TRUE,
                          }
                tags = {}
                if md_member.get(Constants.DEVICETYPE) is not None:
                    tags.update({Constants.DEVICE_TYPE: md_member.get(Constants.DEVICETYPE)})
                if md_member.get(Constants.SERVICETAG) != None:
                    tags.update({Constants.SERVICE_TAG: md_member.get(Constants.SERVICETAG)})

                md_map.update({Constants.TYPE: tags})

                md_list.append(md_map)
                parent_resource_type = requestContext.context.get(Constants.RESOURCETYPES).get(
                    Constants.MANAGER_NATIVE_TYPE)
                if parent_resource_type != None:
                    relation_map = {Constants.TYPE: Constants.MEMBER_OF,
                                    Constants.SOURCE_MOID: requestContext.context.get(Constants.ROOT_MOID),
                                    Constants.TARGET_MOID: md_member.get(Constants.REF_ID)}
                    relation_list.append(relation_map)

        return  md_list,relation_list















