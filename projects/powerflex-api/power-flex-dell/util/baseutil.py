import json

from PyPowerFlex import PowerFlexClient

from httpclient import Url

from jsonpath_ng.ext import parse

import logging

from util.constants import Constants

logger = logging.getLogger(__name__)

import time
env = "production"

class Util:
    def get_cipher(self, requestContext):
        if env == "production" :
            for cred in requestContext.context.get(Constants.DATA).get(Constants.CREDENTIAL):
                credobj = cred.get(Constants.CREDENTIALVALUE)
                if credobj is not None:
                    if cred.get(Constants.FIELDNAME) == Constants.CREDENTIALS and cred.get(Constants.FIELDNAME) is not None:
                        if requestContext.context.get("action") == "Discovery":
                            ciphertext = credobj.get(Constants.PAYLOAD).get(Constants.DATA).get(Constants.CIPHER)
                            key = credobj.get(Constants.PAYLOAD).get(Constants.DATA).get("key1")
                        else:
                            ciphertext = credobj.get(Constants.DATA).get(Constants.CIPHER)
                            key = credobj.get(Constants.DATA).get("key1")
                        res = Url().get_credentials(ciphertext, key)
                        #logger.info("cred reponse" + str(res))
                        requestContext.context[Constants.USERNAME] = res.get(Constants.USERNAME)
                        requestContext.context[Constants.PASSWORD] = res.get(Constants.PASSWORD)
                        logger.info(
                            "username : " + str(requestContext.context[Constants.USERNAME]) + "     " + "password : " +
                            str(requestContext.context[Constants.PASSWORD]))
                else:
                    logger.info("Credential object not found")
        else:
            requestContext.context[Constants.USERNAME] = "cpmsmon"
            requestContext.context[Constants.PASSWORD] = "VMwar1234"
            logger.info(
                "username : " + str(requestContext.context[Constants.USERNAME]) + "     " + "password : " +
                str(requestContext.context[Constants.PASSWORD]))



    def getResponse(self, requestContext, nativeType, moId=None, relation=None):
        self.get_cipher(requestContext)
        _data = None
        ipAddress = requestContext.context.get(Constants.DATA).get(Constants.IPADDRESS)
        username = requestContext.context.get(Constants.USERNAME)
        password = requestContext.context.get(Constants.PASSWORD)
        try:
            if ipAddress != None and username != None and password != None:
                client = PowerFlexClient(gateway_address=ipAddress,
                                         username=username,
                                         password=password)
                client.initialize()
                logger.info(str(moId) + "  moid" + str(relation) + "   relation")
                if nativeType == Constants.SYSTEM or nativeType == Constants.MDM:

                    if moId is None and relation is None:
                        _data = client.system.get()
                    elif moId is not None and relation is None:
                        _data = client.system.get(moId)
                    elif moId is not None and relation is not None:
                        _data = client.system.get_related(moId, relation)

                elif nativeType == Constants.SDC:
                    if moId is None and relation is None:
                        _data = client.sdc.get()
                    elif moId is not None and relation is None:
                        _data = client.sdc.get(moId)
                    elif moId is not None and relation is not None:
                        _data = client.sdc.get_related(moId, relation)

                elif nativeType == Constants.SDS:
                    if moId is None and relation is None:
                        _data = client.sds.get()
                    elif moId is not None and relation is None:
                        _data = client.sds.get(moId)
                    elif moId is not None and relation is not None:
                        _data = client.sds.get_related(moId, relation)

                elif nativeType == Constants.PROTECTION_DOMAIN:
                    if moId is None and relation is None:
                        _data = client.protection_domain.get()
                    elif moId is not None and relation is None:
                        _data = client.protection_domain.get(moId)
                    elif moId is not None and relation is not None:
                        _data = client.protection_domain.get_related(moId, relation)

                elif nativeType == Constants.DEVICE:
                    if moId is None and relation is None:
                        _data = client.device.get()
                    elif moId is not None and relation is None:
                        _data = client.device.get(moId)
                    elif moId is not None and relation is not None:
                        _data = client.device.get_related(moId, relation)

                elif nativeType == Constants.STORAGE_POOL:
                    if moId is None and relation is None:
                        _data = client.storage_pool.get()
                    elif moId is not None and relation is None:
                        _data = client.storage_pool.get(moId)
                    elif moId is not None and relation is not None:
                        _data = client.storage_pool.get_related(moId, relation)


                elif nativeType == Constants.VOLUME:
                    if moId is None and relation is None:
                        _data = client.volume.get()
                _data = json.dumps(_data)
                _data = json.loads(_data)
        except Exception as e:
            logger.exception(e)
        return _data


def get_pattern(pattern, data):
    value = []
    jsonpath_expression = parse(pattern)
    for match in jsonpath_expression.find(data):
        value.append(match.value)
    return value


def getKeys(key):
    switcher = {
        # System
        "dell_powerflex_system_AvailableCapacity": "unusedCapacityInKb",
        "dell_powerflex_system_RebalanceCapacity": "rebalanceCapacityInKb",
        "dell_powerflex_system_SnapUsedCapacity": "snapCapacityInUseInKb",
        "dell_powerflex_system_SystemCapacity": "maxUserDataCapacityInKb",
        "dell_powerflex_system_ThickUsedCapacity": "thickCapacityInUseInKb",
        "dell_powerflex_system_ThinUsedCapacity": "thinCapacityInUseInKb",
        "dell_powerflex_system_UnusableCapacity": "unusedCapacityInKb",
        # cluster
        "dell_powerflex_mdm_CurrentState": "clusterState",
        # sdc
        "dell_powerflex_sdc_ConnectionState": "mdmConnectionState",
        # protection domain
        "dell_powerflex_protectionDomain_State": "protectionDomainState",
        # sds
        "dell_powerflex_sds_ConnectionState": "sdsState",
        # Device
        "dell_powerflex_device_State": "deviceState",

        # storagepool
        "dell_powerflex_storagePool_UsageState":"capacityUsageState",
        "dell_powerflex_storagePool_ActiveBckRebuildCapacity":"activeBckRebuildCapacityInKb",
        "dell_powerflex_storagePool_ActiveFwdRebuildCapacity":"activeFwdRebuildCapacityInKb",
        "dell_powerflex_storagePool_ActiveMovingCapacity":"activeMovingCapacityInKb",
        "dell_powerflex_storagePool_ActiveNormRebuildCapacity":"activeNormRebuildCapacityInKb",
        "dell_powerflex_storagePool_ActiveRebalanceCapacity":"activeRebalanceCapacityInKb",
        "dell_powerflex_storagePool_AtRestCapacity":"atRestCapacityInKb",
        "dell_powerflex_storagePool_BckRebuildCapacity":"bckRebuildCapacityInKb",
        "dell_powerflex_storagePool_CapacityAvailableForVolumeAllocation":"capacityAvailableForVolumeAllocationInKb",
        "dell_powerflex_storagePool_CapacityInUse":"capacityInUseInKb",
        "dell_powerflex_storagePool_CapacityLimit":"capacityLimitInKb",
        "dell_powerflex_storagePool_DegradedFailedCapacity":"degradedFailedCapacityInKb",
        "dell_powerflex_storagePool_DegradedHealthyCapacity":"degradedHealthyCapacityInKb",
        "dell_powerflex_storagePool_FailedCapacity":"failedCapacityInKb",
        "dell_powerflex_storagePool_FwdRebuildCapacity":"fwdRebuildCapacityInKb",
        "dell_powerflex_storagePool_InMaintenanceCapacity":"inMaintenanceCapacityInKb",
        "dell_powerflex_storagePool_MaxCapacity":"maxCapacityInKb",
        "dell_powerflex_storagePool_MovingCapacity":"movingCapacityInKb",
        "dell_powerflex_storagePool_NormRebuildCapacity":"normRebuildCapacityInKb",
        "dell_powerflex_storagePool_NumOfDevices":"numOfDevices",
        "dell_powerflex_storagePool_NumOfVolumes":"numOfVolumes",
        "dell_powerflex_storagePool_NumOfVtrees":"numOfVtrees",
        "dell_powerflex_storagePool_PendingBckRebuildCapacity":"pendingBckRebuildCapacityInKb",
        "dell_powerflex_storagePool_PendingFwdRebuildCapacity":"pendingFwdRebuildCapacityInKb",
        "dell_powerflex_storagePool_PendingMovingCapacity":"pendingMovingCapacityInKb",
        "dell_powerflex_storagePool_PendingNormRebuildCapacity":"pendingNormRebuildCapacityInKb",
        "dell_powerflex_storagePool_PendingRebalanceCapacity":"pendingRebalanceCapacityInKb",
        "dell_powerflex_storagePool_ProtectedCapacity":"protectedCapacityInKb",
        "dell_powerflex_storagePool_RebalanceCapacity":"rebalanceCapacityInKb",
        "dell_powerflex_storagePool_SemiProtectedCapacity":"semiProtectedCapacityInKb",
        "dell_powerflex_storagePool_SnapCapacityInUse":"snapCapacityInUseInKb",
        "dell_powerflex_storagePool_SnapCapacityInUseOccupied":"snapCapacityInUseOccupiedInKb",
        "dell_powerflex_storagePool_SpareCapacity":"spareCapacityInKb",
        "dell_powerflex_storagePool_ThickCapacityInUse":"thickCapacityInUseInKb",
        "dell_powerflex_storagePool_ThinCapacityAllocated":"thinCapacityAllocatedInKb",
        "dell_powerflex_storagePool_ThinCapacityAllocatedInKm":"thinCapacityAllocatedInKm",
        "dell_powerflex_storagePool_ThinCapacityInUse":"thinCapacityInUseInKb",
        "dell_powerflex_storagePool_UnreachableUnusedCapacity":"unreachableUnusedCapacityInKb",
        "dell_powerflex_storagePool_UnusedCapacity":"unusedCapacityInKb",
        "dell_powerflex_storagePool_RfacheReadHit":"rfacheReadHit",
        "dell_powerflex_storagePool_RfacheWriteHit":"rfacheWriteHit",
        "dell_powerflex_storagePool_RfcacheAvgReadTime":"rfcacheAvgReadTime",
        "dell_powerflex_storagePool_RfcacheAvgWriteTime":"rfcacheAvgWriteTime",
        "dell_powerflex_storagePool_RfcacheReadMiss":"rfcacheReadMiss",
        "dell_powerflex_storagePool_RfcacheReadsFromCache":"rfcacheReadsFromCache",
        "dell_powerflex_storagePool_RfcacheReadsPending":"rfcacheReadsPending",
        "dell_powerflex_storagePool_RfcacheReadsReceived":"rfcacheReadsReceived",
        "dell_powerflex_storagePool_RfcacheReadsSkipped":"rfcacheReadsSkipped",
        "dell_powerflex_storagePool_RfcacheReadsSkippedAlignedSizeTooLarge":"rfcacheReadsSkippedAlignedSizeTooLarge",
        "dell_powerflex_storagePool_RfcacheReadsSkippedHeavyLoad":"rfcacheReadsSkippedHeavyLoad",
        "dell_powerflex_storagePool_RfcacheReadsSkippedInternalError":"rfcacheReadsSkippedInternalError",
        "dell_powerflex_storagePool_RfcacheReadsSkippedLockIos":"rfcacheReadsSkippedLockIos",
        "dell_powerflex_storagePool_RfcacheReadsSkippedLowResources":"rfcacheReadsSkippedLowResources",
        "dell_powerflex_storagePool_RfcacheReadsSkippedMaxIoSize":"rfcacheReadsSkippedMaxIoSize",
        "dell_powerflex_storagePool_RfcacheReadsSkippedStuckIo":"rfcacheReadsSkippedStuckIo",
        "dell_powerflex_storagePool_RfcacheSkippedUnlinedWrite":"rfcacheSkippedUnlinedWrite",
        "dell_powerflex_storagePool_RfcacheSourceDeviceReads":"rfcacheSourceDeviceReads",
        "dell_powerflex_storagePool_RfcacheSourceDeviceWrites":"rfcacheSourceDeviceWrites",
        "dell_powerflex_storagePool_RfcacheWriteMiss":"rfcacheWriteMiss",
        "dell_powerflex_storagePool_RfcacheWritePending":"rfcacheWritePending",
        "dell_powerflex_storagePool_RfcacheWritesReceived":"rfcacheWritesReceived",
        "dell_powerflex_storagePool_RfcacheWritesSkippedCacheMiss":"rfcacheWritesSkippedCacheMiss",
        "dell_powerflex_storagePool_RfcacheWritesSkippedHeavyLoad":"rfcacheWritesSkippedHeavyLoad",
        "dell_powerflex_storagePool_RfcacheWritesSkippedInternalError":"rfcacheWritesSkippedInternalError",
        "dell_powerflex_storagePool_RfcacheWritesSkippedLowResources":"rfcacheWritesSkippedLowResources",
        "dell_powerflex_storagePool_RfcacheWritesSkippedMaxIoSize":"rfcacheWritesSkippedMaxIoSize",
        "dell_powerflex_storagePool_RfcacheWritesSkippedStuckIo":"rfcacheReadsSkippedStuckIo"
    }
    return switcher.get(key, "")
