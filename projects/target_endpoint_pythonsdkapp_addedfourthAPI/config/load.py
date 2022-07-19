import datetime
import random, os, logging
import time

from faker import Faker
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)
hosts = int(os.getenv("HOSTS"))  # number of hosts
vms = int(os.getenv("VMS"))  # number of VMs
vcenters = int(os.getenv("VCENTERS"))  # number of Vcenters
vcenters_list = []


class Resources:
    def load_vcenters(self):
        logger.info("started loading the resources")
        for v in range(1, vcenters + 1):
            v = str(v)
            vcenter = {}
            vcenter.clear()
            vcenter["uuid"] = "vcenter" + v
            vcenter["hosts"] = []
            for i in range(1, hosts + 1):
                i= str(i)
                host = {}
                host.clear()
                host["uuid"] = "vcenter" + v + "@" + "host" + i
                host["name"] = "vcenter" + v + "host" + i
                host["host"] = "vcenter" + v + "host" + i
                host["ip"] = str(genIP())
                host['model'] = 'x1'
                host['type'] = 'linux'
                host["vms"] = []

                for j in range(1, vms + 1):
                    j = str (j)
                    vm = {}
                    vm.clear()
                    vm["uuid"] = "vcenter" + v + "@" + "host" + i + "@" + "vm" + j
                    vm["name"] = "vcenter" + v + "host" + i + "vm" + j
                    vm["host"] = "vcenter" + v + "host" + i + "vm" + j
                    vm["ip"] = str(genIP())
                    vm['model'] = 'v1'
                    vm['type'] = 'linux'
                    host["vms"].append(vm)
                vcenter["hosts"].append(host)

            vcenters_list.append(vcenter)
        logger.info("completed loading the resources")

    # Getting all hosts in a vcenter
    def get_all_hosts(self, vcenter_id):
        for vcenter in vcenters_list:
            if vcenter_id == vcenter["uuid"]:
                return (vcenter["hosts"])

    # Getting all the vms of a particular host
    def get_vms_by_host(self, vcenter_id, host_Id, host_data):
        for vcenter in vcenters_list:
            if vcenter_id == vcenter["uuid"]:
                for host in host_data:
                    host_id = host["uuid"].split("@", 1)[1]
                    if host_Id == host_id:
                        return host["vms"]


    def get_host_metrics(self, vcenter_id, host_Id, host_data):
        for vcenter in vcenters_list:
            if vcenter_id == vcenter["uuid"]:
                for host in host_data:
                    host_id = host["uuid"].split("@", 1)[1]
                    if host_Id == host_id:
                        metric_list = self.get_metrics()
                        return metric_list

    def get_vm_metrics(self, vcenter_id, host_Id, host_data):
        for vcenter in vcenters_list:
            if vcenter_id == vcenter["uuid"]:
                for host in host_data:
                    host_id = host["uuid"].split("@", 1)[1]
                    if host_Id == host_id:
                        metric_list = []
                        metric_dict = {}
                        for vm in host["vms"]:
                            ml = self.get_metrics()
                            metric_dict[vm['name']] = ml
                        metric_list.append(metric_dict)
                        return metric_list

    def get_single_vm_metrics(self, vcenter_id, host_Id, host_data, vm_Id):
        for vcenter in vcenters_list:
            if vcenter_id == vcenter["uuid"]:
                for host in host_data:
                    host_id = host["uuid"].split("@", 1)[1]
                    if host_Id == host_id:
                        metric_list = []
                        metric_dict = {}
                        for vm in host["vms"]:
                            if vm["uuid"].split("@",2)[2] == vm_Id:
                                ml = self.get_metrics()
                                metric_dict[vm['name']] = ml
                                break
                        metric_list.append(metric_dict)
                        return metric_list

    def get_all_alerts(self):
        vcenter = ["vcenter1","vcenter2","vcenter3","vcenter4","vcenters"]
        host = ["host1","host2","host3","host4","host5"]
        vm = ["vm1","vm2","vm3","vm4","vm5"]
        return [
            {
                "eventName": "license key expirey",
                "eventDescription":"A license key expires",
                "eventOn":random.choice(vcenter),
                "eventType": "Error",
                "eventTime": time.time()
            },
            {
                "eventName": "virtual machine powered on",
                "eventDescription": "A virtual machine is powered on",
                "eventOn":random.choice(vcenter)+random.choice(host)+random.choice(vm) ,
                "eventType": "Information",
                "eventTime": time.time()
            },
            {
                "eventName": "user logged in",
                "eventDescription": "A user logs in to a virtual machine",
                "eventOn": random.choice(vcenter)+random.choice(host)+random.choice(vm),
                "eventType": "Audit",
                "eventTime": time.time()
            },
            {
                "eventName": "host connection lost",
                "eventDescription": "A host connection is lost",
                "eventOn": random.choice(host)+random.choice(vm),
                "eventType": "Error",
                "eventTime": time.time()
            }
        ]



    def get_metrics(self):
        metric_list = []
        metric1 = {'name': 'system.cpu.usage.utilization'}
        metric1['value'] = random.uniform(0, 100)
        metric_list.append(metric1)

        metric2 = {'name': 'system.memory.usage.utilization'}
        metric2['value'] = random.uniform(0, 100)
        metric_list.append(metric2)

        metric3= {'name': 'system.cpu.load'}
        metric3['value'] = random.uniform(0, 100)
        metric_list.append(metric3)

        metric4= {'name': 'system.disk.usage.freespace'}
        metric4['value'] = random.uniform(0, 100)
        metric_list.append(metric4)

        metric5= {'name': 'system.disk.usage.usedspace'}
        metric5['value'] = random.uniform(0, 10)
        metric_list.append(metric5)

        metric6 = {'name': 'system.memory.usage.usedspace'}
        metric6['value'] = random.uniform(0, 100)
        metric_list.append(metric6)

        metric7 = {'name': 'system.os.uptime'}
        metric7['value'] = random.uniform(0, 100)
        metric_list.append(metric7)

        metric8 = {'name': 'system.network.interface.utilization'}
        metric8['value'] = random.uniform(0, 100)
        metric_list.append(metric8)

        metric9 = {'name': 'system.cpu.usage.stats'}
        metric9['value'] = random.uniform(0, 100)
        metric_list.append(metric9)

        metric10 = {'name': 'system.process.stats.count'}
        metric10['value'] = random.uniform(0, 100)
        metric_list.append(metric10)

        return metric_list

# Generate random IP
def genIP():
    ex = Faker()
    ip = ex.ipv4()
    return ip
