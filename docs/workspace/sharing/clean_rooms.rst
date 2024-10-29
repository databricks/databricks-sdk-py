``w.clean_rooms``: Clean Rooms
==============================
.. currentmodule:: databricks.sdk.service.sharing

.. py:class:: CleanRoomsAPI

    A clean room is a secure, privacy-protecting environment where two or more parties can share sensitive
enterprise data, including customer data, for measurements, insights, activation and other use cases.

To create clean rooms, you must be a metastore admin or a user with the **CREATE_CLEAN_ROOM** privilege.

    .. py:method:: create(name: str, remote_detailed_info: CentralCleanRoomInfo [, comment: Optional[str]]) -> CleanRoomInfo

        Create a clean room.

Creates a new clean room with specified colaborators. The caller must be a metastore admin or have the
**CREATE_CLEAN_ROOM** privilege on the metastore.

:param name: str
  Name of the clean room.
:param remote_detailed_info: :class:`CentralCleanRoomInfo`
  Central clean room details.
:param comment: str (optional)
  User-provided free-form text description.

:returns: :class:`CleanRoomInfo`


    .. py:method:: delete(name: str)

        Delete a clean room.

Deletes a data object clean room from the metastore. The caller must be an owner of the clean room.

:param name: str
  The name of the clean room.




    .. py:method:: get(name: str [, include_remote_details: Optional[bool]]) -> CleanRoomInfo

        Get a clean room.

Gets a data object clean room from the metastore. The caller must be a metastore admin or the owner of
the clean room.

:param name: str
  The name of the clean room.
:param include_remote_details: bool (optional)
  Whether to include remote details (central) on the clean room.

:returns: :class:`CleanRoomInfo`


    .. py:method:: list( [, max_results: Optional[int], page_token: Optional[str]]) -> Iterator[CleanRoomInfo]

        List clean rooms.

Gets an array of data object clean rooms from the metastore. The caller must be a metastore admin or
the owner of the clean room. There is no guarantee of a specific ordering of the elements in the
array.

:param max_results: int (optional)
  Maximum number of clean rooms to return. If not set, all the clean rooms are returned (not
  recommended). - when set to a value greater than 0, the page length is the minimum of this value and
  a server configured value; - when set to 0, the page length is set to a server configured value
  (recommended); - when set to a value less than 0, an invalid parameter error is returned;
:param page_token: str (optional)
  Opaque pagination token to go to next page based on previous query.

:returns: Iterator over :class:`CleanRoomInfo`


    .. py:method:: update(name: str [, catalog_updates: Optional[List[CleanRoomCatalogUpdate]], comment: Optional[str], owner: Optional[str]]) -> CleanRoomInfo

        Update a clean room.

Updates the clean room with the changes and data objects in the request. The caller must be the owner
of the clean room or a metastore admin.

When the caller is a metastore admin, only the __owner__ field can be updated.

In the case that the clean room name is changed **updateCleanRoom** requires that the caller is both
the clean room owner and a metastore admin.

For each table that is added through this method, the clean room owner must also have **SELECT**
privilege on the table. The privilege must be maintained indefinitely for recipients to be able to
access the table. Typically, you should use a group as the clean room owner.

Table removals through **update** do not require additional privileges.

:param name: str
  The name of the clean room.
:param catalog_updates: List[:class:`CleanRoomCatalogUpdate`] (optional)
  Array of shared data object updates.
:param comment: str (optional)
  User-provided free-form text description.
:param owner: str (optional)
  Username of current owner of clean room.

:returns: :class:`CleanRoomInfo`
