``w.provider_files``: Provider Files
====================================
.. currentmodule:: databricks.sdk.service.marketplace

.. py:class:: ProviderFilesAPI

    Marketplace offers a set of file APIs for various purposes such as preview notebooks and provider icons.

    .. py:method:: create(file_parent: FileParent, marketplace_file_type: MarketplaceFileType, mime_type: str [, display_name: Optional[str]]) -> CreateFileResponse

        Creates a file and returns a short-lived URL for uploading its content with an HTTP PUT request. Only
        provider icons (PROVIDER_ICON files on a PROVIDER parent) and sample notebooks (EMBEDDED_NOTEBOOK
        files on a LISTING parent) are supported.

        :param file_parent: :class:`FileParent`
          Provider profile or listing to attach the file to.
        :param marketplace_file_type: :class:`MarketplaceFileType`
          Purpose of the file. PROVIDER_ICON requires a PROVIDER parent; EMBEDDED_NOTEBOOK requires a LISTING
          parent.
        :param mime_type: str
          MIME type of the file content: text/html for notebooks; image/png, image/jpeg or image/svg+xml for
          icons.
        :param display_name: str (optional)
          Name shown to consumers for the file, for example a notebook title. At most 255 characters.

        :returns: :class:`CreateFileResponse`
        

    .. py:method:: delete(file_id: str)

        Deletes a file. Fails if the file is still in use.

        :param file_id: str
          ID of the file to delete.


        

    .. py:method:: get(file_id: str) -> GetFileResponse

        Gets a file's metadata, including a short-lived download URL.

        :param file_id: str
          ID of the file.

        :returns: :class:`GetFileResponse`
        

    .. py:method:: list(file_parent: FileParent [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[FileInfo]

        Lists the files attached to a provider profile or a listing.

        :param file_parent: :class:`FileParent`
          Provider profile or listing whose files to list.
        :param page_size: int (optional)
          Maximum number of results to return per page.
        :param page_token: str (optional)
          Token from the next_page_token field of a previous response. Omit to get the first page.

        :returns: Iterator over :class:`FileInfo`
        