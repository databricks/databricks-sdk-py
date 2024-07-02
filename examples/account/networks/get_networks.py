import time

from databricks.sdk import AccountClient

a = AccountClient()

netw = a.networks.create(network_name=f'sdk-{time.time_ns()}',
                         vpc_id=hex(time.time_ns())[2:],
                         subnet_ids=[hex(time.time_ns())[2:],
                                     hex(time.time_ns())[2:]],
                         security_group_ids=[hex(time.time_ns())[2:]])

by_id = a.networks.get(network_id=netw.network_id)
