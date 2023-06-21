#!env python3
import collections
import inspect
import json
import os.path
from dataclasses import dataclass
from pathlib import Path

from databricks.sdk import AccountClient, WorkspaceClient
from databricks.sdk.core import credentials_provider

__dir__ = os.path.dirname(__file__)
__examples__ = Path(f'{__dir__}/../examples').absolute()


@dataclass
class Package:
    name: str
    label: str
    description: str


@dataclass
class Tag:
    name: str
    service: str
    is_account: bool
    package: Package


@dataclass
class MethodDoc:
    method_name: str
    doc: str
    required_args: list[str]
    kwonly_args: list[str]

    def argspec(self):
        args = ', '.join(self.required_args)
        if len(self.kwonly_args) > 0:
            other = ', '.join(self.kwonly_args)
            args = f'{args} [, {other}]'
        return args

    def as_rst(self, usage) -> str:
        if self.doc is None: return ''
        out = ['', f'    .. py:method:: {self.method_name}({self.argspec()})', usage, f'        {self.doc}']
        return "\n".join(out)


@dataclass
class ServiceDoc:
    service_name: str
    class_name: str
    methods: list[MethodDoc]
    doc: str
    tag: Tag

    def as_rst(self) -> str:
        if not self.doc:
            self.doc = ''
        out = [
            self.tag.name, '=' * len(self.tag.name), f'.. py:class:: {self.class_name}', '', f'    {self.doc}'
        ]
        for m in self.methods:
            usage = self.usage_example(m)
            rst = m.as_rst(usage)
            if not rst:
                continue
            out.append(rst)

        return "\n".join(out)

    def usage_example(self, m):
        out = []
        example_root, example_files = self.examples()
        for potential_example in example_files:
            if not potential_example.startswith(m.method_name):
                continue
            out.append("")
            out.append("        Usage:")
            out.append("")
            out.append("        .. code-block::")
            out.append("")
            with (example_root / potential_example).open('r') as f:
                for line in f.readlines():
                    line = line.rstrip("\n")
                    out.append(f'            {line}')
            out.append("")
            return "\n".join(out)
        return ""

    def examples(self):
        try:
            root = __examples__ / self.service_name
            return root, os.listdir(root)
        except:
            return None, []


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

    def __init__(self):
        self.mapping = self._load_mapping()

    def _load_mapping(self) -> dict[str, Tag]:
        mapping = {}
        pkgs = {p.name: p for p in self.packages}
        with open(os.path.expanduser('~/.openapi-codegen.json'), 'r') as f:
            config = json.load(f)
            if 'spec' not in config:
                raise ValueError('Cannot find OpenAPI spec')
            with open(config['spec'], 'r') as fspec:
                spec = json.load(fspec)
                for tag in spec['tags']:
                    t = Tag(name=tag['name'],
                            service=tag['x-databricks-service'],
                            is_account=tag.get('x-databricks-is-accounts', False),
                            package=pkgs[tag['x-databricks-package']])
                    mapping[tag['name']] = t
        return mapping

    def class_methods(self, inst) -> list[MethodDoc]:
        method_docs = []
        for name in dir(inst):
            if name[0] == '_':
                # private members
                continue
            instance_attr = getattr(inst, name)
            if not callable(instance_attr):
                continue
            args = inspect.getfullargspec(instance_attr)
            method_docs.append(
                MethodDoc(method_name=name,
                          required_args=args.args[1:],
                          kwonly_args=args.kwonlyargs,
                          doc=instance_attr.__doc__))
        return method_docs

    def service_docs(self, client_inst) -> list[ServiceDoc]:
        ignore_client_fields = ('config', 'dbutils', 'api_client', 'files')
        all = []
        for service_name, service_inst in client_inst.__dict__.items():
            if service_name in ignore_client_fields:
                continue
            class_doc = service_inst.__doc__
            class_name = service_inst.__class__.__name__
            all.append(
                ServiceDoc(service_name=service_name,
                           class_name=class_name,
                           doc=class_doc,
                           tag=self._get_tag_name(service_inst.__class__.__name__, service_name),
                           methods=self.class_methods(service_inst)))
        return all

    def _get_tag_name(self, class_name, service_name) -> Tag:
        if class_name[-3:] == 'Ext':
            # ClustersExt, DbfsExt, WorkspaceExt, but not ExternalLocations
            class_name = class_name.replace('Ext', 'API')
        class_name = class_name[:-3]
        for tag_name, t in self.mapping.items():
            if t.service == class_name:
                return t
        raise KeyError(f'Cannot find {class_name} / {service_name} tag')

    def load_client(self, client, folder, label, description):
        client_services = []
        package_to_services = collections.defaultdict(list)
        for svc in self.service_docs(client):
            client_services.append(svc.service_name)
            package_to_services[svc.tag.package.name].append(svc.service_name)
            with open(f'{__dir__}/{folder}/{svc.service_name}.rst', 'w') as f:
                f.write(svc.as_rst())
        ordered_packages = []
        for pkg in self.packages:
            if pkg.name not in package_to_services:
                continue
            ordered_packages.append(pkg.name)
            self._write_client_package_doc(folder, pkg, package_to_services[pkg.name])
        self._write_client_packages(folder, label, description, ordered_packages)

    def _write_client_packages(self, folder: str, label: str, description: str, packages: list[str]):
        with open(f'{__dir__}/{folder}/index.rst', 'w') as f:
            all = "\n  ".join([f'{folder}-{name}' for name in packages])
            f.write(f'''
{label}
{'=' * len(label)}
 
{description}
 
.. toctree::
  :maxdepth: 1
  
  {all}''')

    def _write_client_package_doc(self, folder: str, pkg: Package, services: list[str]):
        with open(f'{__dir__}/{folder}/{folder}-{pkg.name}.rst', 'w') as f:
            all = "\n  ".join(services)
            f.write(f'''
{pkg.label}
{'=' * len(pkg.label)}
 
{pkg.description}
 
.. toctree::
  :maxdepth: 1
  
  {all}''')


if __name__ == '__main__':

    @credentials_provider('noop', [])
    def noop_credentials(_: any):
        return lambda: {}

    gen = Generator()

    w = WorkspaceClient(credentials_provider=noop_credentials)
    gen.load_client(w, 'workspace', 'Workspace APIs', 'These APIs are available from WorkspaceClient')

    a = AccountClient(credentials_provider=noop_credentials)
    gen.load_client(a, 'account', 'Account APIs', 'These APIs are available from AccountClient')
