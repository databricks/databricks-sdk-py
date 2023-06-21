Policy Families
===============
.. py:class:: PolicyFamiliesAPI

    View available policy families. A policy family contains a policy definition providing best practices for
    configuring clusters for a particular use case.
    
    Databricks manages and provides policy families for several common cluster use cases. You cannot create,
    edit, or delete policy families.
    
    Policy families cannot be used directly to create clusters. Instead, you create cluster policies using a
    policy family. Cluster policies created using a policy family inherit the policy family's policy
    definition.