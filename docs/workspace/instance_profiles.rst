Instance Profiles
=================
.. currentmodule:: databricks.sdk.service.compute

.. py:class:: InstanceProfilesAPI

    The Instance Profiles API allows admins to add, list, and remove instance profiles that users can launch
    clusters with. Regular users can list the instance profiles available to them. See [Secure access to S3
    buckets] using instance profiles for more information.
    
    [Secure access to S3 buckets]: https://docs.databricks.com/administration-guide/cloud-configurations/aws/instance-profiles.html

    .. py:method:: add(instance_profile_arn: str [, iam_role_arn: Optional[str], is_meta_instance_profile: Optional[bool], skip_validation: Optional[bool]])


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            arn = "arn:aws:iam::000000000000:instance-profile/abc"
            
            w.instance_profiles.add(instance_profile_arn=arn,
                                    skip_validation=True,
                                    iam_role_arn="arn:aws:iam::000000000000:role/bcd")

        Register an instance profile.
        
        In the UI, you can select the instance profile when launching clusters. This API is only available to
        admin users.
        
        :param instance_profile_arn: str
          The AWS ARN of the instance profile to register with Databricks. This field is required.
        :param iam_role_arn: str (optional)
          The AWS IAM role ARN of the role associated with the instance profile. This field is required if
          your role name and instance profile name do not match and you want to use the instance profile with
          [Databricks SQL Serverless].
          
          Otherwise, this field is optional.
          
          [Databricks SQL Serverless]: https://docs.databricks.com/sql/admin/serverless.html
        :param is_meta_instance_profile: bool (optional)
          Boolean flag indicating whether the instance profile should only be used in credential passthrough
          scenarios. If true, it means the instance profile contains an meta IAM role which could assume a
          wide range of roles. Therefore it should always be used with authorization. This field is optional,
          the default value is `false`.
        :param skip_validation: bool (optional)
          By default, Databricks validates that it has sufficient permissions to launch instances with the
          instance profile. This validation uses AWS dry-run mode for the RunInstances API. If validation
          fails with an error message that does not indicate an IAM related permission issue, (e.g. “Your
          requested instance type is not supported in your requested availability zone”), you can pass this
          flag to skip the validation and forcibly add the instance profile.
        
        
        

    .. py:method:: edit(instance_profile_arn: str [, iam_role_arn: Optional[str], is_meta_instance_profile: Optional[bool]])


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            arn = "arn:aws:iam::000000000000:instance-profile/abc"
            
            w.instance_profiles.edit(instance_profile_arn=arn, iam_role_arn="arn:aws:iam::000000000000:role/bcdf")

        Edit an instance profile.
        
        The only supported field to change is the optional IAM role ARN associated with the instance profile.
        It is required to specify the IAM role ARN if both of the following are true:
        
        * Your role name and instance profile name do not match. The name is the part after the last slash in
        each ARN. * You want to use the instance profile with [Databricks SQL Serverless].
        
        To understand where these fields are in the AWS console, see [Enable serverless SQL warehouses].
        
        This API is only available to admin users.
        
        [Databricks SQL Serverless]: https://docs.databricks.com/sql/admin/serverless.html
        [Enable serverless SQL warehouses]: https://docs.databricks.com/sql/admin/serverless.html
        
        :param instance_profile_arn: str
          The AWS ARN of the instance profile to register with Databricks. This field is required.
        :param iam_role_arn: str (optional)
          The AWS IAM role ARN of the role associated with the instance profile. This field is required if
          your role name and instance profile name do not match and you want to use the instance profile with
          [Databricks SQL Serverless].
          
          Otherwise, this field is optional.
          
          [Databricks SQL Serverless]: https://docs.databricks.com/sql/admin/serverless.html
        :param is_meta_instance_profile: bool (optional)
          Boolean flag indicating whether the instance profile should only be used in credential passthrough
          scenarios. If true, it means the instance profile contains an meta IAM role which could assume a
          wide range of roles. Therefore it should always be used with authorization. This field is optional,
          the default value is `false`.
        
        
        

    .. py:method:: list() -> Iterator[InstanceProfile]


        Usage:

        .. code-block::

            from databricks.sdk import WorkspaceClient
            
            w = WorkspaceClient()
            
            all = w.instance_profiles.list()

        List available instance profiles.
        
        List the instance profiles that the calling user can use to launch a cluster.
        
        This API is available to all users.
        
        :returns: Iterator over :class:`InstanceProfile`
        

    .. py:method:: remove(instance_profile_arn: str)

        Remove the instance profile.
        
        Remove the instance profile with the provided ARN. Existing clusters with this instance profile will
        continue to function.
        
        This API is only accessible to admin users.
        
        :param instance_profile_arn: str
          The ARN of the instance profile to remove. This field is required.
        
        
        