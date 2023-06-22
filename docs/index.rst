Databricks SDK for Python
-------------------------

The Databricks SDK for Python includes functionality to accelerate development with Python for the Databricks Lakehouse.
It covers all public `Databricks REST API <https://docs.databricks.com/api>`_ operations.
The SDK's internal HTTP client is robust and handles failures on different levels by
performing intelligent retries. Install it via

.. code-block::

  $ pip install databricks-sdk

.. note::

   The Databricks SDK for Python is in an Experimental state. To provide feedback, ask questions, and report issues, use the `Issues tab <https://github.com/databricks/databricks-sdk-py/issues>`_ in the `Databricks SDK for Python repository <https://github.com/databricks/databricks-sdk-py>`_ on GitHub.

   During the Experimental period, Databricks is actively working on stabilizing the Databricks SDK for Python’s interfaces. API clients for all services are generated from specification files that are synchronized from the main platform. You are highly encouraged to install a specific version of the Databricks SDK for Python package and read the changelog where Databricks documents the changes. Databricks may have minor documented backward-incompatible changes, such as renaming the functions or some class names to bring more consistency.

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


