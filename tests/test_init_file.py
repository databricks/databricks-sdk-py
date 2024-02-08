import hashlib


def test_init_file_contents():
    """
    Micro test to confirm the contents of `databricks/__init__.py` does not change.

    Also see https://github.com/databricks/databricks-sdk-py/issues/343#issuecomment-1866029118.
    """
    with open('databricks/__init__.py') as f:
        init_file_contents = f.read()

    # This hash is the expected hash of the contents of `src/databricks/__init__.py`.
    # It must not change, or else parallel package installation may lead to clobbered and invalid files.
    expected_sha1 = '2772edbf52e517542acf8c039479c4b57b6ca2cd'
    actual_sha1 = hashlib.sha1(init_file_contents.encode('utf-8')).hexdigest()
    assert expected_sha1 == actual_sha1
