# This is a sample Python script.
import json

from target import TargetDiscovery
from _requestcontext import RequestContext

def get_json_data():
    json = {
        "action": "Update",
        "app": "demo-sample-app-python",
        "appIntegrationId": "INTG-13ef297f-4070-4e1d-a60f-9409ca56dd05",
        "appVersion": "1.0.0",
        "configurationId": "ADAPTER-MANIFEST-2e81f915-6f45-470c-9723-d7bf696f07c6",
        "configurationName": "demo",
        "deployment": "Image",
        "frequency": "0 13,28,43,58 * * * ? *",
        "gateway": "7827d75f-2466-4c4b-b457-acbc2a8d1954",
        "managementProfileId": "7827d75f-2466-4c4b-b457-acbc2a8d1954",
        "messageId": "1780bc40-a8ef-4103-8e96-c8f9adb963af",
        "messageVersion": "2.0.0",
        "module": "Discovery",
        "payload": {
            "data": {
                "alertConfiguration": "true",
                "alertOnRootResource": "true",
                "credential": [
                    {
                        "credentialId": "UMrqFmUYu8aqxgNdNEYTP9rp",
                        "credentialValue": {
                            "data": {
                                "cipher": "ydBmr3Y/Obl1qbSxljFj0U24yjIAAEXS1xhguqn68LR/Keu0TBQt0Zl5BWRdAMZtEGgefETh8y3sR+ckUNZ+uAqWsiYTsmsYKdxIPGfwa6GpPZlq8Dn8mlV7DhBNO774c992Zqx8P6xrdj1a4d0meQJvEweIAvfZstxqVyugPoNa17EYV45eJ0V8OSYjJNZAEvbSG2wiHde7d0vVSzk9k6aae+n5jhfUizy2nKQrhLB+mlvd1G2veHuasViDkmwoO1IHADcGZj6LDUAyU+l1QFPJr6Wr5T0u9vPRc33HqIfaq4M=",
                                "classId": "credential.cipher",
                                "key1": "181dbf63bf5",
                                "type": "APPLICATION",
                                "uuid": "UMrqFmUYu8aqxgNdNEYTP9rp",
                                "ver": 2
                            }
                        },
                        "fieldName": "credentials"
                    }
                ],
                "ipAddress": "192.168.111.236",
                "notificationAlert": "true",
                "port": "45000",
                "protocol": "http",
                "vcenterName": "vcenter1"
            },
            "nativeTypes": {
                "host": {
                    "resourceType": "server"
                },
                "vcenter": {
                    "resourceType": "server"
                },
                "vm": {
                    "resourceType": "server"
                }
            }
        },
        "requireAck": "false",
        "sha": "ee39a21e3ff5a5a3c1aa54a100e1e929e28e2657b1ee2232314a24b56515d2be",
        "subtype": "Configuration"
    }
    return json

def print_hi(name):
    requestContext = RequestContext("1", get_json_data())
    requestContext.context = {"app_data": get_json_data()}
    print("Discovery")
    print("Vcenter Data")
    print("-----------------------------------------------------")
    print(TargetDiscovery().get_Vcenter_data( requestContext, "Server"))
    print("-----------------------------------------------------")
    print("Host Data")
    print("-----------------------------------------------------")
    print(TargetDiscovery().get_Host_data(requestContext, "Server"))
    print("-----------------------------------------------------")
    print("Vm Data")
    print("-----------------------------------------------------")
    print(TargetDiscovery().get_Vm_data(requestContext, "Server"))
    print("-----------------------------------------------------")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')




