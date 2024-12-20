``w.consumer_installations``: Consumer Installations
====================================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ConsumerInstallationsAPI

    Installations are entities that allow consumers to interact with Databricks Marketplace listings.

    .. py:method:: create(listing_id: str [, accepted_consumer_terms: Optional[ConsumerTerms], catalog_name: Optional[str], recipient_type: Optional[DeltaSharingRecipientType], repo_detail: Optional[RepoInstallation], share_name: Optional[str]]) -> Installation

        Install from a listing.
        
        Install payload associated with a Databricks Marketplace listing.
        
        :param listing_id: str
        :param accepted_consumer_terms: :class:`ConsumerTerms` (optional)
        :param catalog_name: str (optional)
        :param recipient_type: :class:`DeltaSharingRecipientType` (optional)
        :param repo_detail: :class:`RepoInstallation` (optional)
          for git repo installations
        :param share_name: str (optional)
        
        :returns: :class:`Installation`


    .. py:method:: delete(listing_id: str, installation_id: str)

        Uninstall from a listing.
        
        Uninstall an installation associated with a Databricks Marketplace listing.
        
        :param listing_id: str
        :param installation_id: str
        



    .. py:method:: list( [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[InstallationDetail]

        List all installations.
        
        List all installations across all listings.
        
        :param page_size: int (optional)
        :param page_token: str (optional)
        
        :returns: Iterator over :class:`InstallationDetail`


    .. py:method:: list_listing_installations(listing_id: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[InstallationDetail]

        List installations for a listing.
        
        List all installations for a particular listing.
        
        :param listing_id: str
        :param page_size: int (optional)
        :param page_token: str (optional)
        
        :returns: Iterator over :class:`InstallationDetail`


    .. py:method:: update(listing_id: str, installation_id: str, installation: InstallationDetail [, rotate_token: Optional[bool]]) -> UpdateInstallationResponse

        Update an installation.
        
        This is a update API that will update the part of the fields defined in the installation table as well
        as interact with external services according to the fields not included in the installation table 1.
        the token will be rotate if the rotateToken flag is true 2. the token will be forcibly rotate if the
        rotateToken flag is true and the tokenInfo field is empty
        
        :param listing_id: str
        :param installation_id: str
        :param installation: :class:`InstallationDetail`
        :param rotate_token: bool (optional)
        
        :returns: :class:`UpdateInstallationResponse`
