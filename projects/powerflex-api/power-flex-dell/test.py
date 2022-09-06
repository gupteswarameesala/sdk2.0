
import json
from jsonpath_ng import jsonpath
from jsonpath_ng.ext import parse


dic = {
    "systemVersionName": "DellEMC PowerFlex Version: R3_6.300.107",
    "perfProfile": "HighPerformance",
    "authenticationMethod": "Native",
    "capacityAlertHighThresholdPercent": 80,
    "capacityAlertCriticalThresholdPercent": 90,
    "upgradeState": "NoUpgrade",
    "remoteReadOnlyLimitState": "false",
    "mdmManagementPort": 6611,
    "mdmExternalPort": 7611,
    "sdcMdmNetworkDisconnectionsCounterParameters": {
      "mediumWindow": {
        "threshold": 500,
        "windowSizeInSec": 3600
      },
      "longWindow": {
        "threshold": 700,
        "windowSizeInSec": 86400
      },
      "shortWindow": {
        "threshold": 300,
        "windowSizeInSec": 60
      }
    },
    "sdcSdsNetworkDisconnectionsCounterParameters": {
      "mediumWindow": {
        "threshold": 4000,
        "windowSizeInSec": 3600
      },
      "longWindow": {
        "threshold": 20000,
        "windowSizeInSec": 86400
      },
      "shortWindow": {
        "threshold": 800,
        "windowSizeInSec": 60
      }
    },
    "sdcMemoryAllocationFailuresCounterParameters": {
      "mediumWindow": {
        "threshold": 500,
        "windowSizeInSec": 3600
      },
      "longWindow": {
        "threshold": 700,
        "windowSizeInSec": 86400
      },
      "shortWindow": {
        "threshold": 300,
        "windowSizeInSec": 60
      }
    },
    "sdcSocketAllocationFailuresCounterParameters": {
      "mediumWindow": {
        "threshold": 500,
        "windowSizeInSec": 3600
      },
      "longWindow": {
        "threshold": 700,
        "windowSizeInSec": 86400
      },
      "shortWindow": {
        "threshold": 300,
        "windowSizeInSec": 60
      }
    },
    "sdcLongOperationsCounterParameters": {
      "mediumWindow": {
        "threshold": 100000,
        "windowSizeInSec": 3600
      },
      "longWindow": {
        "threshold": 1000000,
        "windowSizeInSec": 86400
      },
      "shortWindow": {
        "threshold": 10000,
        "windowSizeInSec": 60
      }
    },
    "cliPasswordAllowed": "true",
    "managementClientSecureCommunicationEnabled": "true",
    "tlsVersion": "TLSv1.2",
    "showGuid": "true",
    "defragmentationEnabled": "true",
    "mdmSecurityPolicy": "None",
    "mdmCluster": {
      "clusterState": "ClusteredNormal",
      "virtualIps": [
        "172.16.1.51",
        "172.16.2.51"
      ],
      "clusterMode": "ThreeNodes",
      "tieBreakers": [
        {
          "managementIPs": [
            "10.60.89.137"
          ],
          "ips": [
            "172.16.1.13",
            "172.16.2.13"
          ],
          "versionInfo": "R3_6.300.0",
          "opensslVersion": "N/A",
          "role": "TieBreaker",
          "status": "Normal",
          "name": "pflex-storage-03",
          "id": "5cfdf4117be02902",
          "port": 9011
        }
      ],
      "standbyMDMs": [
        {
          "managementIPs": [
            "10.60.89.138"
          ],
          "ips": [
            "172.16.1.14",
            "172.16.2.14"
          ],
          "opensslVersion": "N/A",
          "virtualInterfaces": [
            "bond0.151",
            "bond1.152"
          ],
          "role": "Manager",
          "name": "pflex-storage-04",
          "id": "5027e33f6eb06d03",
          "port": 9011
        }
      ],
      "goodNodesNum": 3,
      "goodReplicasNum": 2,
      "master": {
        "managementIPs": [
          "10.60.89.135"
        ],
        "ips": [
          "172.16.1.11",
          "172.16.2.11"
        ],
        "versionInfo": "R3_6.300.0",
        "opensslVersion": "OpenSSL 1.0.2k-fips  26 Jan 2017",
        "virtualInterfaces": [
          "bond0.151",
          "bond1.152"
        ],
        "role": "Manager",
        "status": "Normal",
        "name": "pflex-storage-01",
        "id": "000c21e16dcbce00",
        "port": 9011
      },
      "slaves": [
        {
          "managementIPs": [
            "10.60.89.136"
          ],
          "ips": [
            "172.16.1.12",
            "172.16.2.12"
          ],
          "versionInfo": "R3_6.300.0",
          "opensslVersion": "OpenSSL 1.0.2k-fips  26 Jan 2017",
          "virtualInterfaces": [
            "bond0.151",
            "bond1.152"
          ],
          "role": "Manager",
          "status": "Normal",
          "name": "pflex-storage-02",
          "id": "6d3b020535b65f01",
          "port": 9011
        }
      ],
      "name": "stage-pflex-gateway",
      "id": "624241968486428175"
    },
    "sdcSdsConnectivityInfo": {
      "clientServerConnectivityStatus": "AllConnected",
      "disconnectedClientId": "null",
      "disconnectedClientName": "null",
      "disconnectedServerId": "null",
      "disconnectedServerName": "null",
      "disconnectedServerIp": "null"
    },
    "addressSpaceUsage": "Normal",
    "lastUpgradeTime": 0,
    "sdcSdrConnectivityInfo": {
      "clientServerConnectivityStatus": "AllConnected",
      "disconnectedClientId": "null",
      "disconnectedClientName": "null",
      "disconnectedServerId": "null",
      "disconnectedServerName": "null",
      "disconnectedServerIp": "null"
    },
    "sdrSdsConnectivityInfo": {
      "clientServerConnectivityStatus": "AllConnected",
      "disconnectedClientId": "null",
      "disconnectedClientName": "null",
      "disconnectedServerId": "null",
      "disconnectedServerName": "null",
      "disconnectedServerIp": "null"
    },
    "isInitialLicense": "true",
    "enterpriseFeaturesEnabled": "true",
    "capacityTimeLeftInDays": "34",
    "swid": "",
    "daysInstalled": 56,
    "maxCapacityInGb": "Unlimited",
    "restrictedSdcMode": "None",
    "restrictedSdcModeEnabled": "false",
    "installId": "2997f5533560cd52",
    "name": "stage-pflex-gateway",
    "id": "08a9c0c351862e0f",
    "links": [
      {
        "rel": "self",
        "href": "/api/instances/System::08a9c0c351862e0f"
      },
      {
        "rel": "/api/System/relationship/Statistics",
        "href": "/api/instances/System::08a9c0c351862e0f/relationships/Statistics"
      },
      {
        "rel": "/api/System/relationship/Sdr",
        "href": "/api/instances/System::08a9c0c351862e0f/relationships/Sdr"
      },
      {
        "rel": "/api/System/relationship/ProtectionDomain",
        "href": "/api/instances/System::08a9c0c351862e0f/relationships/ProtectionDomain"
      },
      {
        "rel": "/api/System/relationship/Sdc",
        "href": "/api/instances/System::08a9c0c351862e0f/relationships/Sdc"
      },
      {
        "rel": "/api/System/relationship/User",
        "href": "/api/instances/System::08a9c0c351862e0f/relationships/User"
      },
      {
        "rel": "/api/System/relationship/SnapshotPolicy",
        "href": "/api/instances/System::08a9c0c351862e0f/relationships/SnapshotPolicy"
      },
      {
        "rel": "/api/System/relationship/PeerMdm",
        "href": "/api/instances/System::08a9c0c351862e0f/relationships/PeerMdm"
      }
    ]
  }






lis = []
jsonpath_expression = parse("$.mdmCluster.clusterStat")
for match in jsonpath_expression.find(dic):
	lis.append(match.value)
print(lis)