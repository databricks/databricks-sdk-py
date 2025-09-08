``w.clean_room_asset_revisions``: Asset Revisions
=================================================
.. currentmodule:: databricks.sdk.service.cleanrooms

.. py:class:: CleanRoomAssetRevisionsAPI

    Clean Room Asset Revisions denote new versions of uploaded assets (e.g. notebooks) in the clean room.

    .. py:method:: get(clean_room_name: str, asset_type: CleanRoomAssetAssetType, name: str, etag: str) -> CleanRoomAsset

        Get a specific revision of an asset
        
        :param clean_room_name: str
          Name of the clean room.
        :param asset_type: :class:`CleanRoomAssetAssetType`
          Asset type. Only NOTEBOOK_FILE is supported.
        :param name: str
          Name of the asset.
        :param etag: str
          Revision etag to fetch. If not provided, the latest revision will be returned.
        
        :returns: :class:`CleanRoomAsset`
        

    .. py:method:: list(clean_room_name: str, asset_type: CleanRoomAssetAssetType, name: str [, page_size: Optional[int], page_token: Optional[str]]) -> Iterator[CleanRoomAsset]

        List revisions for an asset
        
        :param clean_room_name: str
          Name of the clean room.
        :param asset_type: :class:`CleanRoomAssetAssetType`
          Asset type. Only NOTEBOOK_FILE is supported.
        :param name: str
          Name of the asset.
        :param page_size: int (optional)
          Maximum number of asset revisions to return. Defaults to 10.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on the previous query.
        
        :returns: Iterator over :class:`CleanRoomAsset`
        