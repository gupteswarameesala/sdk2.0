# @staticmethod
# def sample():
#     resources = {}
#     print("test")
#     print(datetime.datetime.now())
#
#     def host(i, j):
#         resources[f'vcenter{i + 1}']['hosts'][f'host{j + 1}'] = {
#             'vms': {},
#             'uuid': f'vcenter{i + 1}@host{j + 1}',
#             'name': f'host{j + 1}',
#             'host': f'host{j + 1}',
#             'ip': str(genIP()),
#             'model': 'x1',
#             'type': 'linux'
#         }
#
#     def vm(i, j, k):
#         resources[f'vcenter{i + 1}']['hosts'][f'host{j + 1}']['vms'][f'vm{k + 1}'] = {
#             'uuid': f'vcenter{i + 1}@host{j + 1}@vm{k + 1}',
#             'name': f'host{j + 1}@vm{k + 1}',
#             'host': f'host{j + 1}@vm{k + 1}',
#             'ip': str(genIP()),
#             'model': 'y1',
#             'type': 'linux'
#         }
#         print(i, j, k)
#
#     def vcenter(i):
#         resources[f'vcenter{i + 1}'] = {
#             'uuid': f'vcenter{i + 1}',
#             'hosts': {}
#         }
#
#     for i in range(vcenters):
#         threading.Thread(target=vcenter, args=[i]).start()
#
#         for j in range(hosts):
#             threading.Thread(target=host, args=[i, j]).start()
#
#             for k in range(vms):
#                 threading.Thread(target=vm, args=[i, j, k]).start()
#
#     print(datetime.datetime.now())
