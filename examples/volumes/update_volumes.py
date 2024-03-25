import os
import time

from databricks.sdk import WorkspaceClient
from databricks.sdk.service import catalog

w = WorkspaceClient()

storage_credential = w.storage_credentials.create(
    name=f'sdk-{time.time_ns()}',
    aws_iam_role=catalog.AwsIamRoleRequest(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
    comment="created via SDK")

external_location = w.external_locations.create(name=f'sdk-{time.time_ns()}',
                                                credential_name=storage_credential.name,
                                                comment="created via SDK",
                                                url="s3://" + os.environ["TEST_BUCKET"] + "/" +
                                                f'sdk-{time.time_ns()}')

created_catalog = w.catalogs.create(name=f'sdk-{time.time_ns()}')

created_schema = w.schemas.create(name=f'sdk-{time.time_ns()}', catalog_name=created_catalog.name)

created_volume = w.volumes.create(catalog_name=created_catalog.name,
                                  schema_name=created_schema.name,
                                  name=f'sdk-{time.time_ns()}',
                                  storage_location=external_location.url,
                                  volume_type=catalog.VolumeType.EXTERNAL)

loaded_volume = w.volumes.read(name=created_volume.full_name)

_ = w.volumes.update(name=loaded_volume.full_name, comment="Updated volume comment")

# cleanup
w.storage_credentials.delete(name=storage_credential.name)
w.external_locations.delete(name=external_location.name)
w.schemas.delete(full_name=created_schema.full_name)
w.catalogs.delete(name=created_catalog.name, force=True)
w.volumes.delete(name=created_volume.full_name)
