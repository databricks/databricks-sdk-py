
Statement Execution (Lakehouse//RT) V2
======================================

The Statement Execution API v2 can be used to execute SQL statements on a SQL warehouse and fetch the
result. It works the same as the Statement Execution API (v1), except that `warehouse_id` is a path parameter
on every call, including polling, fetching result chunks, and canceling. Routing on the warehouse ID gives
lower latency and higher concurrency.

Version 2 currently supports [Lakehouse//RT](https://docs.databricks.com/compute/sql-warehouse/real-time.html) warehouses only. For other
warehouse types, use the Statement Execution API (v1). You can also run statements on Lakehouse//RT warehouses
with version 1, but version 2 is optimized for them.

.. toctree::
   :maxdepth: 1

   statement_execution_v2