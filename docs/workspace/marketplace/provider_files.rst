``w.provider_files``: Provider Files
====================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderFilesAPI

    Marketplace offers a set of file APIs for various purposes such as preview notebooks and provider icons.

    .. py:method:: create(file_parent: FileParent, marketplace_file_type: MarketplaceFileType, mime_type: str [, display_name: Optional[str]]) -> CreateFileResponse

        Create a file.
        
        Create a file. Currently, only provider icons and attached notebooks are supported.
        
        :param file_parent: :class:`FileParent`
        :param marketplace_file_type: :class:`MarketplaceFileType`
        :param mime_type: str
        :param display_name: str (optional)
        
        :returns: :class:`CreateFileResponse`


    .. py:method:: delete(file_id: str)

        Delete a file.
        
        Delete a file
        
        :param file_id: str
        



    .. py:method:: get(file_id: str) -> GetFileResponse

        Get a file.
        
        Get a file
        
        :param file_id: str
        
        :returns: :class:`GetFileResponse`


    .. py:method:: list(file_parent: FileParent [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[FileInfo]

        List files.
        
        List files attached to a parent entity.
        
        :param file_parent: :class:`FileParent`
        :param page_size: int (optional)
        :param page_token: str (optional)
        
        :returns: Iterator over :class:`FileInfo`
