``w.clean_room_assets``: Assets
===============================
.. currentmodule:: databricks.sdk.service.cleanrooms

.. py:class:: CleanRoomAssetsAPI

    Clean room assets are data and code objects — Tables, volumes, and notebooks that are shared with the
    clean room.

    .. py:method:: create(clean_room_name: str [, asset: Optional[CleanRoomAsset]]) -> CleanRoomAsset

        Create an asset.
        
        Create a clean room asset —share an asset like a notebook or table into the clean room. For each UC
        asset that is added through this method, the clean room owner must also have enough privilege on the
        asset to consume it. The privilege must be maintained indefinitely for the clean room to be able to
        access the asset. Typically, you should use a group as the clean room owner.
        
        :param clean_room_name: str
          Name of the clean room.
        :param asset: :class:`CleanRoomAsset` (optional)
          Metadata of the clean room asset
        
        :returns: :class:`CleanRoomAsset`
        

    .. py:method:: delete(clean_room_name: str, asset_type: CleanRoomAssetAssetType, asset_full_name: str)

        Delete an asset.
        
        Delete a clean room asset - unshare/remove the asset from the clean room
        
        :param clean_room_name: str
          Name of the clean room.
        :param asset_type: :class:`CleanRoomAssetAssetType`
          The type of the asset.
        :param asset_full_name: str
          The fully qualified name of the asset, it is same as the name field in CleanRoomAsset.
        
        
        

    .. py:method:: get(clean_room_name: str, asset_type: CleanRoomAssetAssetType, asset_full_name: str) -> CleanRoomAsset

        Get an asset.
        
        Get the details of a clean room asset by its type and full name.
        
        :param clean_room_name: str
          Name of the clean room.
        :param asset_type: :class:`CleanRoomAssetAssetType`
          The type of the asset.
        :param asset_full_name: str
          The fully qualified name of the asset, it is same as the name field in CleanRoomAsset.
        
        :returns: :class:`CleanRoomAsset`
        

    .. py:method:: list(clean_room_name: str [, page_token: Optional[str]]) -> Iterator[CleanRoomAsset]

        List assets.
        
        :param clean_room_name: str
          Name of the clean room.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`CleanRoomAsset`
        

    .. py:method:: update(clean_room_name: str, asset_type: CleanRoomAssetAssetType, name: str [, asset: Optional[CleanRoomAsset]]) -> CleanRoomAsset

        Update an asset.
        
        Update a clean room asset. For example, updating the content of a notebook; changing the shared
        partitions of a table; etc.
        
        :param clean_room_name: str
          Name of the clean room.
        :param asset_type: :class:`CleanRoomAssetAssetType`
          The type of the asset.
        :param name: str
          A fully qualified name that uniquely identifies the asset within the clean room. This is also the
          name displayed in the clean room UI.
          
          For UC securable assets (tables, volumes, etc.), the format is
          *shared_catalog*.*shared_schema*.*asset_name*
          
          For notebooks, the name is the notebook file name.
        :param asset: :class:`CleanRoomAsset` (optional)
          Metadata of the clean room asset
        
        :returns: :class:`CleanRoomAsset`
        