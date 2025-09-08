``w.clean_room_assets``: Assets
===============================
.. currentmodule:: databricks.sdk.service.cleanrooms

.. py:class:: CleanRoomAssetsAPI

    Clean room assets are data and code objects — Tables, volumes, and notebooks that are shared with the
    clean room.

    .. py:method:: create(clean_room_name: str, asset: CleanRoomAsset) -> CleanRoomAsset

        Create a clean room asset —share an asset like a notebook or table into the clean room. For each UC
        asset that is added through this method, the clean room owner must also have enough privilege on the
        asset to consume it. The privilege must be maintained indefinitely for the clean room to be able to
        access the asset. Typically, you should use a group as the clean room owner.
        
        :param clean_room_name: str
          The name of the clean room this asset belongs to. This field is required for create operations and
          populated by the server for responses.
        :param asset: :class:`CleanRoomAsset`
        
        :returns: :class:`CleanRoomAsset`
        

    .. py:method:: create_clean_room_asset_review(clean_room_name: str, asset_type: CleanRoomAssetAssetType, name: str [, notebook_review: Optional[NotebookVersionReview]]) -> CreateCleanRoomAssetReviewResponse

        Submit an asset review
        
        :param clean_room_name: str
          Name of the clean room
        :param asset_type: :class:`CleanRoomAssetAssetType`
          Asset type. Can either be NOTEBOOK_FILE or JAR_ANALYSIS.
        :param name: str
          Name of the asset
        :param notebook_review: :class:`NotebookVersionReview` (optional)
        
        :returns: :class:`CreateCleanRoomAssetReviewResponse`
        

    .. py:method:: delete(clean_room_name: str, asset_type: CleanRoomAssetAssetType, name: str)

        Delete a clean room asset - unshare/remove the asset from the clean room
        
        :param clean_room_name: str
          Name of the clean room.
        :param asset_type: :class:`CleanRoomAssetAssetType`
          The type of the asset.
        :param name: str
          The fully qualified name of the asset, it is same as the name field in CleanRoomAsset.
        
        
        

    .. py:method:: get(clean_room_name: str, asset_type: CleanRoomAssetAssetType, name: str) -> CleanRoomAsset

        Get the details of a clean room asset by its type and full name.
        
        :param clean_room_name: str
          Name of the clean room.
        :param asset_type: :class:`CleanRoomAssetAssetType`
          The type of the asset.
        :param name: str
          The fully qualified name of the asset, it is same as the name field in CleanRoomAsset.
        
        :returns: :class:`CleanRoomAsset`
        

    .. py:method:: list(clean_room_name: str [, page_token: Optional[str]]) -> Iterator[CleanRoomAsset]

        List assets.
        
        :param clean_room_name: str
          Name of the clean room.
        :param page_token: str (optional)
          Opaque pagination token to go to next page based on previous query.
        
        :returns: Iterator over :class:`CleanRoomAsset`
        

    .. py:method:: update(clean_room_name: str, asset_type: CleanRoomAssetAssetType, name: str, asset: CleanRoomAsset) -> CleanRoomAsset

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
          
          For notebooks, the name is the notebook file name. For jar analyses, the name is the jar analysis
          name.
        :param asset: :class:`CleanRoomAsset`
          The asset to update. The asset's `name` and `asset_type` fields are used to identify the asset to
          update.
        
        :returns: :class:`CleanRoomAsset`
        