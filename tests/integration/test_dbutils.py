import base64
import logging

import pytest

from databricks.sdk.core import DatabricksError


def test_rest_dbfs_ls(w, env_or_skip):
    from databricks.sdk.runtime import dbutils

    x = dbutils.fs.ls('/')

    assert len(x) > 1


def test_proxy_dbfs_mounts(w, env_or_skip):
    w.config.cluster_id = env_or_skip("TEST_DEFAULT_CLUSTER_ID")

    x = w.dbutils.fs.mounts()

    assert len(x) > 1


def test_secrets(w, random):
    random_scope = f'scope-{random()}'
    key_for_string = f'string-{random()}'
    key_for_bytes = f'bytes-{random()}'
    random_value = f'SECRET-{random()}'

    logger = logging.getLogger('foo')
    logger.info(f'Before loading secret: {random_value}')

    w.secrets.create_scope(random_scope)
    w.secrets.put_secret(random_scope, key_for_string, string_value=random_value)
    w.secrets.put_secret(random_scope,
                         key_for_bytes,
                         bytes_value=base64.b64encode(random_value.encode()).decode())

    from databricks.sdk.runtime import dbutils

    all_secrets = {}
    for secret_scope in dbutils.secrets.listScopes():
        scope = secret_scope.name
        for secret_metadata in dbutils.secrets.list(scope):
            key = secret_metadata.key
            try:
                all_secrets[f'{scope}.{key}'] = dbutils.secrets.get(scope, key)
            except DatabricksError as e:
                if e.error_code == 'BAD_REQUEST':
                    pytest.skip('dbconnect is not enabled on this workspace')
                raise e

    logger.info(f'After loading secret: {random_value}')
    logging.getLogger('databricks.sdk').info(f'After loading secret: {random_value}')

    assert all_secrets[f'{random_scope}.{key_for_string}'] == random_value
    assert all_secrets[f'{random_scope}.{key_for_bytes}'] == random_value
