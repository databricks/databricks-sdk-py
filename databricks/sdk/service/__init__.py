# Import all service modules
from databricks.sdk.service import (apps, billing, catalog, cleanrooms,
                                    compute, dashboards, files, iam, jobs,
                                    marketplace, ml, oauth2, pipelines,
                                    provisioning, serving, settings, sharing,
                                    sql, vectorsearch, workspace)

# Re-export all modules
__all__ = [
    "apps",
    "billing",
    "catalog",
    "cleanrooms",
    "compute",
    "dashboards",
    "files",
    "iam",
    "jobs",
    "marketplace",
    "ml",
    "oauth2",
    "pipelines",
    "provisioning",
    "serving",
    "settings",
    "sharing",
    "sql",
    "vectorsearch",
    "workspace",
]
