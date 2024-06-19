import os
import time

from databricks.sdk import AccountClient

a = AccountClient()

created = a.vpc_endpoints.create(aws_vpc_endpoint_id=os.environ["TEST_RELAY_VPC_ENDPOINT"],
                                 region=os.environ["AWS_REGION"],
                                 vpc_endpoint_name=f'sdk-{time.time_ns()}')

by_id = a.vpc_endpoints.get(vpc_endpoint_id=created.vpc_endpoint_id)

# cleanup
a.vpc_endpoints.delete(vpc_endpoint_id=created.vpc_endpoint_id)
