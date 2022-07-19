from flask import Flask
from flask import jsonify
from config.load import *

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/vcenters/<vcenter_id>/hosts', methods=['GET'])
def display_hosts(vcenter_id):
    data = Resources().get_all_hosts(vcenter_id)
    # print(len(data.__str__()))
    return jsonify(data)


@app.route('/api/v1/vcenters/<vcenter_id>/hosts/<host_id>/vms', methods=['GET'])
def display_vms(vcenter_id, host_id):
    host_data = Resources().get_all_hosts(vcenter_id)
    data = Resources().get_vms_by_host(vcenter_id, host_id, host_data)
    return jsonify(data)


@app.route('/api/v1/vcenters/<vcenter_id>/hosts/<host_id>/metrics', methods=['GET'])
def display_metrics(vcenter_id, host_id):
    host_data = Resources().get_all_hosts(vcenter_id)
    data = Resources().get_host_metrics(vcenter_id, host_id, host_data)
    return jsonify(data)


@app.route('/api/v1/vcenters/<vcenter_id>/hosts/<host_id>/vms/metrics', methods=['GET'])
def display_vm_metrics(vcenter_id, host_id):
    host_data = Resources().get_all_hosts(vcenter_id)
    data = Resources().get_vm_metrics(vcenter_id, host_id, host_data)
    return jsonify(data)

@app.route('/api/v1/vcenters/<vcenter_id>/hosts/<host_id>/vms/<vm_id>/metrics', methods=['GET'])
def display_single_vm_metrics(vcenter_id, host_id, vm_Id):
    host_data = Resources().get_all_hosts(vcenter_id)
    data = Resources().get_single_vm_metrics(vcenter_id, host_id, host_data, vm_Id)
    return jsonify(data)

@app.route('/api/v1/types/alert/instances', methods=['GET'])
def display_alerts():
    alert_data = Resources().get_all_alerts()
    return jsonify(alert_data)


def start_server():
    logger.info("server started")
    app.run(host='0.0.0.0', port=45000, use_reloader=False)
