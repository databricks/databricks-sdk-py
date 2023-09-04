Databricks SDK for Python (Beta)
--------------------------------

The Databricks SDK for Python includes functionality to accelerate development with Python for the Databricks Lakehouse.
It covers all public `Databricks REST API <https://docs.databricks.com/api>`_ operations.
The SDK's internal HTTP client is robust and handles failures on different levels by
performing intelligent retries. Install it via

.. code-block::

  $ pip install databricks-sdk

To install the Databricks SDK for Python from a Databricks Notebook as a `notebook-scoped library <https://docs.databricks.com/en/libraries/notebooks-python-libraries.html>`_, please run:

.. code-block::

  %pip install databricks-sdk
  dbutils.library.restartPython()

This SDK is supported for production use cases, but we do expect future releases to have `some interface changes <https://github.com/databricks/databricks-sdk-py#interface-stability>`_.
We are keen to hear feedback from you on these SDKs. Please `file GitHub issues <https://github.com/databricks/databricks-sdk-py/issues>`_, and we will address them.

.. toctree::
   :maxdepth: 2

   authentication
   oauth
   wait
   pagination
   logging
   dbutils
   workspace/index
   account/index


