Marketplace
===========

These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.marketplace`` module.

.. py:currentmodule:: databricks.sdk.service.marketplace
.. autoclass:: AddExchangeForListingRequest
   :members:
   :undoc-members:

.. autoclass:: AddExchangeForListingResponse
   :members:
   :undoc-members:

.. py:class:: AssetType

   .. py:attribute:: ASSET_TYPE_DATA_TABLE
      :value: "ASSET_TYPE_DATA_TABLE"

   .. py:attribute:: ASSET_TYPE_GIT_REPO
      :value: "ASSET_TYPE_GIT_REPO"

   .. py:attribute:: ASSET_TYPE_MEDIA
      :value: "ASSET_TYPE_MEDIA"

   .. py:attribute:: ASSET_TYPE_MODEL
      :value: "ASSET_TYPE_MODEL"

   .. py:attribute:: ASSET_TYPE_NOTEBOOK
      :value: "ASSET_TYPE_NOTEBOOK"

   .. py:attribute:: ASSET_TYPE_UNSPECIFIED
      :value: "ASSET_TYPE_UNSPECIFIED"

.. autoclass:: BatchGetListingsResponse
   :members:
   :undoc-members:

.. autoclass:: BatchGetProvidersResponse
   :members:
   :undoc-members:

.. py:class:: Category

   .. py:attribute:: ADVERTISING_AND_MARKETING
      :value: "ADVERTISING_AND_MARKETING"

   .. py:attribute:: CLIMATE_AND_ENVIRONMENT
      :value: "CLIMATE_AND_ENVIRONMENT"

   .. py:attribute:: COMMERCE
      :value: "COMMERCE"

   .. py:attribute:: DEMOGRAPHICS
      :value: "DEMOGRAPHICS"

   .. py:attribute:: ECONOMICS
      :value: "ECONOMICS"

   .. py:attribute:: EDUCATION
      :value: "EDUCATION"

   .. py:attribute:: ENERGY
      :value: "ENERGY"

   .. py:attribute:: FINANCIAL
      :value: "FINANCIAL"

   .. py:attribute:: GAMING
      :value: "GAMING"

   .. py:attribute:: GEOSPATIAL
      :value: "GEOSPATIAL"

   .. py:attribute:: HEALTH
      :value: "HEALTH"

   .. py:attribute:: LOOKUP_TABLES
      :value: "LOOKUP_TABLES"

   .. py:attribute:: MANUFACTURING
      :value: "MANUFACTURING"

   .. py:attribute:: MEDIA
      :value: "MEDIA"

   .. py:attribute:: OTHER
      :value: "OTHER"

   .. py:attribute:: PUBLIC_SECTOR
      :value: "PUBLIC_SECTOR"

   .. py:attribute:: RETAIL
      :value: "RETAIL"

   .. py:attribute:: SCIENCE_AND_RESEARCH
      :value: "SCIENCE_AND_RESEARCH"

   .. py:attribute:: SECURITY
      :value: "SECURITY"

   .. py:attribute:: SPORTS
      :value: "SPORTS"

   .. py:attribute:: TRANSPORTATION_AND_LOGISTICS
      :value: "TRANSPORTATION_AND_LOGISTICS"

   .. py:attribute:: TRAVEL_AND_TOURISM
      :value: "TRAVEL_AND_TOURISM"

.. autoclass:: ConsumerTerms
   :members:
   :undoc-members:

.. autoclass:: ContactInfo
   :members:
   :undoc-members:

.. py:class:: Cost

   .. py:attribute:: FREE
      :value: "FREE"

   .. py:attribute:: PAID
      :value: "PAID"

.. autoclass:: CreateExchangeFilterRequest
   :members:
   :undoc-members:

.. autoclass:: CreateExchangeFilterResponse
   :members:
   :undoc-members:

.. autoclass:: CreateExchangeRequest
   :members:
   :undoc-members:

.. autoclass:: CreateExchangeResponse
   :members:
   :undoc-members:

.. autoclass:: CreateFileRequest
   :members:
   :undoc-members:

.. autoclass:: CreateFileResponse
   :members:
   :undoc-members:

.. autoclass:: CreateInstallationRequest
   :members:
   :undoc-members:

.. autoclass:: CreateListingRequest
   :members:
   :undoc-members:

.. autoclass:: CreateListingResponse
   :members:
   :undoc-members:

.. autoclass:: CreatePersonalizationRequest
   :members:
   :undoc-members:

.. autoclass:: CreatePersonalizationRequestResponse
   :members:
   :undoc-members:

.. autoclass:: CreateProviderRequest
   :members:
   :undoc-members:

.. autoclass:: CreateProviderResponse
   :members:
   :undoc-members:

.. py:class:: DataRefresh

   .. py:attribute:: DAILY
      :value: "DAILY"

   .. py:attribute:: HOURLY
      :value: "HOURLY"

   .. py:attribute:: MINUTE
      :value: "MINUTE"

   .. py:attribute:: MONTHLY
      :value: "MONTHLY"

   .. py:attribute:: NONE
      :value: "NONE"

   .. py:attribute:: QUARTERLY
      :value: "QUARTERLY"

   .. py:attribute:: SECOND
      :value: "SECOND"

   .. py:attribute:: WEEKLY
      :value: "WEEKLY"

   .. py:attribute:: YEARLY
      :value: "YEARLY"

.. autoclass:: DataRefreshInfo
   :members:
   :undoc-members:

.. autoclass:: DeleteExchangeFilterResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteExchangeResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteFileResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteInstallationResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteListingResponse
   :members:
   :undoc-members:

.. autoclass:: DeleteProviderResponse
   :members:
   :undoc-members:

.. py:class:: DeltaSharingRecipientType

   .. py:attribute:: DELTA_SHARING_RECIPIENT_TYPE_DATABRICKS
      :value: "DELTA_SHARING_RECIPIENT_TYPE_DATABRICKS"

   .. py:attribute:: DELTA_SHARING_RECIPIENT_TYPE_OPEN
      :value: "DELTA_SHARING_RECIPIENT_TYPE_OPEN"

.. autoclass:: Exchange
   :members:
   :undoc-members:

.. autoclass:: ExchangeFilter
   :members:
   :undoc-members:

.. py:class:: ExchangeFilterType

   .. py:attribute:: GLOBAL_METASTORE_ID
      :value: "GLOBAL_METASTORE_ID"

.. autoclass:: ExchangeListing
   :members:
   :undoc-members:

.. autoclass:: FileInfo
   :members:
   :undoc-members:

.. autoclass:: FileParent
   :members:
   :undoc-members:

.. py:class:: FileParentType

   .. py:attribute:: LISTING
      :value: "LISTING"

   .. py:attribute:: PROVIDER
      :value: "PROVIDER"

.. py:class:: FileStatus

   .. py:attribute:: FILE_STATUS_PUBLISHED
      :value: "FILE_STATUS_PUBLISHED"

   .. py:attribute:: FILE_STATUS_SANITIZATION_FAILED
      :value: "FILE_STATUS_SANITIZATION_FAILED"

   .. py:attribute:: FILE_STATUS_SANITIZING
      :value: "FILE_STATUS_SANITIZING"

   .. py:attribute:: FILE_STATUS_STAGING
      :value: "FILE_STATUS_STAGING"

.. py:class:: FilterType

   .. py:attribute:: METASTORE
      :value: "METASTORE"

.. py:class:: FulfillmentType

   .. py:attribute:: INSTALL
      :value: "INSTALL"

   .. py:attribute:: REQUEST_ACCESS
      :value: "REQUEST_ACCESS"

.. autoclass:: GetExchangeResponse
   :members:
   :undoc-members:

.. autoclass:: GetFileResponse
   :members:
   :undoc-members:

.. autoclass:: GetLatestVersionProviderAnalyticsDashboardResponse
   :members:
   :undoc-members:

.. autoclass:: GetListingContentMetadataResponse
   :members:
   :undoc-members:

.. autoclass:: GetListingResponse
   :members:
   :undoc-members:

.. autoclass:: GetListingsResponse
   :members:
   :undoc-members:

.. autoclass:: GetPersonalizationRequestResponse
   :members:
   :undoc-members:

.. autoclass:: GetProviderResponse
   :members:
   :undoc-members:

.. autoclass:: Installation
   :members:
   :undoc-members:

.. autoclass:: InstallationDetail
   :members:
   :undoc-members:

.. py:class:: InstallationStatus

   .. py:attribute:: FAILED
      :value: "FAILED"

   .. py:attribute:: INSTALLED
      :value: "INSTALLED"

.. autoclass:: ListAllInstallationsResponse
   :members:
   :undoc-members:

.. autoclass:: ListAllPersonalizationRequestsResponse
   :members:
   :undoc-members:

.. autoclass:: ListExchangeFiltersResponse
   :members:
   :undoc-members:

.. autoclass:: ListExchangesForListingResponse
   :members:
   :undoc-members:

.. autoclass:: ListExchangesResponse
   :members:
   :undoc-members:

.. autoclass:: ListFilesResponse
   :members:
   :undoc-members:

.. autoclass:: ListFulfillmentsResponse
   :members:
   :undoc-members:

.. autoclass:: ListInstallationsResponse
   :members:
   :undoc-members:

.. autoclass:: ListListingsForExchangeResponse
   :members:
   :undoc-members:

.. autoclass:: ListListingsResponse
   :members:
   :undoc-members:

.. autoclass:: ListProviderAnalyticsDashboardResponse
   :members:
   :undoc-members:

.. autoclass:: ListProvidersResponse
   :members:
   :undoc-members:

.. autoclass:: Listing
   :members:
   :undoc-members:

.. autoclass:: ListingDetail
   :members:
   :undoc-members:

.. autoclass:: ListingFulfillment
   :members:
   :undoc-members:

.. autoclass:: ListingSetting
   :members:
   :undoc-members:

.. py:class:: ListingShareType

   .. py:attribute:: FULL
      :value: "FULL"

   .. py:attribute:: SAMPLE
      :value: "SAMPLE"

.. py:class:: ListingStatus

   Enums

   .. py:attribute:: DRAFT
      :value: "DRAFT"

   .. py:attribute:: PENDING
      :value: "PENDING"

   .. py:attribute:: PUBLISHED
      :value: "PUBLISHED"

   .. py:attribute:: SUSPENDED
      :value: "SUSPENDED"

.. autoclass:: ListingSummary
   :members:
   :undoc-members:

.. autoclass:: ListingTag
   :members:
   :undoc-members:

.. py:class:: ListingTagType

   .. py:attribute:: LISTING_TAG_TYPE_LANGUAGE
      :value: "LISTING_TAG_TYPE_LANGUAGE"

   .. py:attribute:: LISTING_TAG_TYPE_TASK
      :value: "LISTING_TAG_TYPE_TASK"

   .. py:attribute:: LISTING_TAG_TYPE_UNSPECIFIED
      :value: "LISTING_TAG_TYPE_UNSPECIFIED"

.. py:class:: ListingType

   .. py:attribute:: PERSONALIZED
      :value: "PERSONALIZED"

   .. py:attribute:: STANDARD
      :value: "STANDARD"

.. py:class:: MarketplaceFileType

   .. py:attribute:: EMBEDDED_NOTEBOOK
      :value: "EMBEDDED_NOTEBOOK"

   .. py:attribute:: PROVIDER_ICON
      :value: "PROVIDER_ICON"

.. autoclass:: PersonalizationRequest
   :members:
   :undoc-members:

.. py:class:: PersonalizationRequestStatus

   .. py:attribute:: DENIED
      :value: "DENIED"

   .. py:attribute:: FULFILLED
      :value: "FULFILLED"

   .. py:attribute:: NEW
      :value: "NEW"

   .. py:attribute:: REQUEST_PENDING
      :value: "REQUEST_PENDING"

.. autoclass:: ProviderAnalyticsDashboard
   :members:
   :undoc-members:

.. autoclass:: ProviderIconFile
   :members:
   :undoc-members:

.. py:class:: ProviderIconType

   .. py:attribute:: DARK
      :value: "DARK"

   .. py:attribute:: PRIMARY
      :value: "PRIMARY"

   .. py:attribute:: PROVIDER_ICON_TYPE_UNSPECIFIED
      :value: "PROVIDER_ICON_TYPE_UNSPECIFIED"

.. autoclass:: ProviderInfo
   :members:
   :undoc-members:

.. autoclass:: ProviderListingSummaryInfo
   :members:
   :undoc-members:

.. autoclass:: RegionInfo
   :members:
   :undoc-members:

.. autoclass:: RemoveExchangeForListingResponse
   :members:
   :undoc-members:

.. autoclass:: RepoInfo
   :members:
   :undoc-members:

.. autoclass:: RepoInstallation
   :members:
   :undoc-members:

.. autoclass:: SearchListingsResponse
   :members:
   :undoc-members:

.. autoclass:: ShareInfo
   :members:
   :undoc-members:

.. autoclass:: SharedDataObject
   :members:
   :undoc-members:

.. py:class:: SortBy

   .. py:attribute:: SORT_BY_DATE
      :value: "SORT_BY_DATE"

   .. py:attribute:: SORT_BY_RELEVANCE
      :value: "SORT_BY_RELEVANCE"

   .. py:attribute:: SORT_BY_TITLE
      :value: "SORT_BY_TITLE"

   .. py:attribute:: SORT_BY_UNSPECIFIED
      :value: "SORT_BY_UNSPECIFIED"

.. autoclass:: TokenDetail
   :members:
   :undoc-members:

.. autoclass:: TokenInfo
   :members:
   :undoc-members:

.. autoclass:: UpdateExchangeFilterRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateExchangeFilterResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateExchangeRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateExchangeResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateInstallationRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateInstallationResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateListingRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateListingResponse
   :members:
   :undoc-members:

.. autoclass:: UpdatePersonalizationRequestRequest
   :members:
   :undoc-members:

.. autoclass:: UpdatePersonalizationRequestResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateProviderAnalyticsDashboardRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateProviderAnalyticsDashboardResponse
   :members:
   :undoc-members:

.. autoclass:: UpdateProviderRequest
   :members:
   :undoc-members:

.. autoclass:: UpdateProviderResponse
   :members:
   :undoc-members:

.. py:class:: Visibility

   .. py:attribute:: PRIVATE
      :value: "PRIVATE"

   .. py:attribute:: PUBLIC
      :value: "PUBLIC"

.. autoclass:: VisibilityFilter
   :members:
   :undoc-members:
