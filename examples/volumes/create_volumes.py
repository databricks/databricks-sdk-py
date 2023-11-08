from databricks.sdk import WorkspaceClient
from databricks.sdk.service import _internal, iam, iam, sql, serving, catalog, billing, billing, catalog, sharing, compute, compute, compute, catalog, provisioning, settings, iam, oauth2, sql, sql, sql, files, sql, provisioning, ml, catalog, files, catalog, workspace, compute, catalog, iam, compute, compute, settings, jobs, compute, billing, catalog, catalog, ml, catalog, settings, settings, provisioning, oauth2, iam, pipelines, compute, provisioning, sharing, oauth2, sql, sql, sql, sharing, sharing, catalog, workspace, catalog, workspace, oauth2, iam, serving, settings, sharing, sql, provisioning, catalog, catalog, catalog, catalog, settings, settings, iam, catalog, provisioning, sql, workspace, iam, catalog, settings, provisioning
import time, base64, os

w = WorkspaceClient()

storage_credential = w.storage_credentials.create(
    name=f'sdk-{time.time_ns()}',
    aws_iam_role=catalog.AwsIamRole(role_arn=os.environ["TEST_METASTORE_DATA_ACCESS_ARN"]),
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

# cleanup
w.schemas.delete(full_name=created_schema.full_name)
w.catalogs.delete(name=created_catalog.name, force=True)
w.volumes.delete(full_name_arg=created_volume.full_name)
