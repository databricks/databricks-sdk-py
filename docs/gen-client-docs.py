#!env python3
import os.path
from dataclasses import dataclass

__dir__ = os.path.dirname(__file__)


@dataclass
class Package:
    name: str
    label: str
    description: str


class Generator:
    packages = [
        Package("workspace", "Databricks Workspace",
                "Manage workspace-level entities that include notebooks, Git checkouts, and secrets"),
        Package("compute", "Compute", "Use and configure compute for Databricks"),
        Package("jobs", "Jobs", "Schedule automated jobs on Databricks Workspaces"),
        Package("pipelines", "Delta Live Tables",
                "Manage pipelines, runs, and other Delta Live Table resources"),
        Package("files", "File Management", "Manage files on Databricks in a filesystem-like interface"),
        Package("ml", "Machine Learning",
                "Create and manage experiments, features, and other machine learning artifacts"),
        Package("serving", "Real-time Serving", "Use real-time inference for machine learning"),
        Package("iam", "Identity and Access Management",
                "Manage users, service principals, groups and their permissions in Accounts and Workspaces"),
        Package(
            "sql", "Databricks SQL",
            "Manage Databricks SQL assets, including warehouses, dashboards, queries and query history, and alerts"
        ),
        Package(
            "catalog", "Unity Catalog",
            "Configure data governance with Unity Catalog for metastores, catalogs, schemas, tables, external locations, and storage credentials"
        ),
        Package("sharing", "Delta Sharing",
                "Configure data sharing with Unity Catalog for providers, recipients, and shares"),
        Package("settings", "Settings", "Manage security settings for Accounts and Workspaces"),
        Package(
            "provisioning", "Provisioning",
            "Resource management for secure Databricks Workspace deployment, cross-account IAM roles, " +
            "storage, encryption, networking and private access."),
        Package("billing", "Billing", "Configure different aspects of Databricks billing and usage."),
        Package("oauth2", "OAuth", "Configure OAuth 2.0 application registrations for Databricks")
    ]

    def write_reference(self):
        for pkg in self.packages:
            self._write_client_package_doc(pkg)
        self._write_reference_toc()

    def _write_client_package_doc(self, pkg: Package):
        title = f'``{pkg.name}``: {pkg.label}'
        has_mixin = os.path.exists(f'{__dir__}/../databricks/sdk/mixins/{pkg.name}.py')
        with open(f'{__dir__}/autogen/{pkg.name}.rst', 'w') as f:
            f.write(f'''
{title}
{'=' * len(title)}

{pkg.description}
            
.. automodule:: databricks.sdk.service.{pkg.name}
   :members:
   :undoc-members:
''')
            if has_mixin:
                f.write(f'''
.. automodule:: databricks.sdk.mixins.{pkg.name}
   :members:
   :inherited-members:
   :undoc-members:
''')

    def _write_reference_toc(self):
        all = '\n'.join([f'   {p.name}' for p in sorted(self.packages, key=lambda p: p.name)])
        with open(f'{__dir__}/autogen/reference.rst', 'w') as f:
            f.write(f'''
Reference
=========

.. toctree::
   :maxdepth: 1
   
{all}
''')


if __name__ == '__main__':
    gen = Generator()
    gen.write_reference()
