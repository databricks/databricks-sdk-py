#!env python3
import collections
import enum
import inspect
import json
import os.path
import re
import subprocess
import importlib
from dataclasses import dataclass, is_dataclass
from enum import Enum
from pathlib import Path
from typing import Optional, Any, get_args

from databricks.sdk import AccountClient, WorkspaceClient
from databricks.sdk.core import credentials_strategy

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
class TypedArgument:
    name: str
    tpe: Optional[str]
    default: Optional[Any]

    def __str__(self):
        ret = self.name
        if self.tpe is not None:
            ret += f': {self.tpe}'
        elif self.default is not None:
            tpe = type(self.default)
            if tpe.__module__ == 'builtins':
                ret += f': {tpe.__name__}'
            else:
                ret += f': {tpe.__module__}.{tpe.__name__}'
        if self.default is not None:
            ret += f' = {self.default}'
        return ret


@dataclass
class PropertyDoc:
    name: str
    doc: Optional[str]
    tpe: Optional[str]

    def as_rst(self) -> str:
        out = ['', f'    .. py:property:: {self.name}']
        if self.tpe is not None:
            out.append(f'        :type: {self.tpe}')
        if self.doc is not None:
            # This is a class doc, which comes with 4 indentation spaces. 
            # Here we are using the doc as property doc, which needs 8 indentation spaces.
            formatted_doc = re.sub(r'\n', '\n    ', self.doc)
            out.append(f'\n        {formatted_doc}')
        return "\n".join(out)

@dataclass
class MethodDoc:
    method_name: str
    doc: Optional[str]
    required_args: list[TypedArgument]
    kwonly_args: list[TypedArgument]
    return_type: Optional[str]

    def argspec(self):
        args = ', '.join([str(x) for x in self.required_args])
        if len(self.kwonly_args) > 0:
            other = ', '.join([str(x) for x in self.kwonly_args])
            args = f'{args} [, {other}]'
        return args

    def as_rst(self, usage) -> str:
        ret_annotation = f' -> {self.return_type}' if self.return_type is not None else ''
        out = ['', f'    .. py:method:: {self.method_name}({self.argspec()}){ret_annotation}', '']
        if usage != '':
            out.append(usage)
        if self.doc is not None:
            out.append(f'        {self.doc}')
        return "\n".join(out)


@dataclass
class ServiceDoc:
    client_prefix: str
    service_name: str
    class_name: str
    methods: list[MethodDoc]
    property: list[PropertyDoc]
    doc: str
    tag: Tag

    def as_rst(self) -> str:
        if not self.doc:
            self.doc = ''
        title = f'``{self.client_prefix}.{self.service_name}``: {self.tag.name}'
        out = [
            title, '=' * len(title),
            f'.. currentmodule:: databricks.sdk.service.{self.tag.package.name}', '',
            f'.. py:class:: {self.class_name}', '', f'    {self.doc}'
        ]
        for m in self.methods:
            usage = self.usage_example(m)
            rst = m.as_rst(usage)
            if not rst:
                continue
            out.append(rst)

        for p in self.property:
            out.append(p.as_rst())

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
        folder = "account" if self.tag.is_account else "workspace"
        try:
            root = __examples__ / folder / self.service_name
            return root, os.listdir(root)
        except:
            return None, []

@dataclass
class DataclassesDoc:
    package: Package
    dataclasses: list[str]

    def as_rst(self) -> str:
        title = f'{self.package.label}'
        out = [
            title, '=' * len(title), '',
            f'These dataclasses are used in the SDK to represent API requests and responses for services in the ``databricks.sdk.service.{self.package.name}`` module.',
            '',
            f'.. py:currentmodule:: databricks.sdk.service.{self.package.name}',
        ]
        for d in self.dataclasses:
            out.append(self.dataclass_rst(d))
        return "\n".join(out)

    def dataclass_rst(self, cls) -> str:
        mod = importlib.import_module(f'databricks.sdk.service.{self.package.name}')
        clss = getattr(mod, cls)
        if issubclass(clss, Enum):
            out = [
                f'.. py:class:: {cls}',
                '',
            ]
            if clss.__doc__ is not None:
                out.append(f'   {self._get_enum_doc(clss)}')
                out.append('')
            for v in clss.__members__.keys():
                out.append(f'   .. py:attribute:: {v}')
                out.append(f'      :value: "{v}"')
                out.append('')
        else:
            out = [
                f'.. autoclass:: {cls}',
                '   :members:',
                '   :undoc-members:',
                ''
            ]
        return "\n".join(out)

    @staticmethod
    def _get_enum_doc(cls) -> str:
        stripped = []
        for line in cls.__doc__.split('\n'):
            stripped.append(line.strip())
        result = []
        current = []
        for line in stripped:
            if line == '':
                if len(current) > 0:
                    result.append(' '.join(current))
                    current = []
            else:
                current.append(line)
        if len(current) > 0:
            result.append(' '.join(current))
        return '\n   '.join(result)

class Generator:
    packages = [
        Package("workspace", "Workspace",
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
        Package("oauth2", "OAuth", "Configure OAuth 2.0 application registrations for Databricks"),
        Package("vectorsearch", "Vector Search", "Create and query Vector Search indexes"),
        Package("dashboards", "Dashboards", "Manage Lakeview dashboards"),
        Package("marketplace", "Marketplace", "Manage AI and analytics assets such as ML models, notebooks, applications in an open marketplace"),
    ]

    def __init__(self):
        self.mapping = self._load_mapping()

    def _openapi_spec(self) -> str:
        if 'DATABRICKS_OPENAPI_SPEC' in os.environ:
            with open(os.environ['DATABRICKS_OPENAPI_SPEC']) as f:
                return f.read()
        with open(f'{__dir__}/../.codegen/_openapi_sha') as f:
            sha = f.read().strip()
        return subprocess.check_output(['deco', 'openapi', 'get', sha]).decode('utf-8')

    def _load_mapping(self) -> dict[str, Tag]:
        mapping = {}
        pkgs = {p.name: p for p in self.packages}
        spec = json.loads(self._openapi_spec())
        for tag in spec['tags']:
            t = Tag(name=tag['name'],
                    service=tag['x-databricks-service'],
                    is_account=tag.get('x-databricks-is-accounts', False),
                    package=pkgs[tag['x-databricks-package']])
            mapping[tag['name']] = t
        return mapping

    @staticmethod
    def _get_type_from_annotations(annotations, name):
        tpe = annotations.get(name)
        if len(get_args(tpe)) > 0:
            tpe = get_args(tpe)[0]
        if isinstance(tpe, type):
            tpe = tpe.__name__
        return tpe

    @staticmethod
    def _to_typed_args(argspec: inspect.FullArgSpec, required: bool) -> list[TypedArgument]:
        annotations = argspec.annotations if argspec.annotations is not None else {}
        if required:
            argslist = argspec.args[1:]
            defaults = {}
            for i, x in enumerate(argspec.defaults if argspec.defaults is not None else []):
                defaults[argslist[i - len(argspec.defaults)]] = x
        else:
            argslist = argspec.kwonlyargs
            defaults = argspec.kwonlydefaults
        out = []
        for arg in argslist:
            tpe = Generator._get_type_from_annotations(annotations, arg)
            out.append(TypedArgument(name=arg, tpe=tpe, default=defaults.get(arg)))
        return out

    def class_properties(self, inst) -> list[PropertyDoc]:
        property_docs = []
        for name in dir(inst):
            if name[0] == '_':
                # private members
                continue
            instance_attr = getattr(inst, name)
            if name.startswith('_'):
                continue
            if inspect.ismethod(instance_attr):
                continue
            property_docs.append(
                PropertyDoc(name=name,
                            doc=instance_attr.__doc__,
                            tpe=instance_attr.__class__.__name__))
        return property_docs

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
                          required_args=self._to_typed_args(args, required=True),
                          kwonly_args=self._to_typed_args(args, required=False),
                          doc=instance_attr.__doc__,
                          return_type=Generator._get_type_from_annotations(args.annotations, 'return')))
        return method_docs

    def service_docs(self, client_inst, client_prefix: str) -> list[ServiceDoc]:
        ignore_client_fields = ('config', 'dbutils', 'api_client', 'get_workspace_client', 'get_workspace_id')
        all = []
        for service_name, service_inst in inspect.getmembers(client_inst, lambda o: not inspect.ismethod(o)):
            if service_name.startswith('_'):
                continue
            if service_name in ignore_client_fields:
                continue
            class_doc = service_inst.__doc__
            class_name = service_inst.__class__.__name__
            print(f'Processing service {client_prefix}.{service_name}')
            all += self.service_docs(service_inst, client_prefix + "." + service_name)

            all.append(
                ServiceDoc(client_prefix=client_prefix,
                           service_name=service_name,
                           class_name=class_name,
                           doc=class_doc,
                           tag=self._get_tag_name(service_inst.__class__.__name__, service_name),
                           methods=self.class_methods(service_inst),
                           property=self.class_properties(service_inst)))
        return all

    @staticmethod
    def _should_document(obj):
        return is_dataclass(obj) or (type(obj) == enum.EnumType and obj != Enum)

    @staticmethod
    def _make_folder_if_not_exists(folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def write_dataclass_docs(self):
        self._make_folder_if_not_exists(f'{__dir__}/dbdataclasses')
        for pkg in self.packages:
            module = importlib.import_module(f'databricks.sdk.service.{pkg.name}')
            all_members = [name for name, _ in inspect.getmembers(module, predicate=self._should_document)]
            doc = DataclassesDoc(package=pkg, dataclasses=sorted(all_members))
            with open(f'{__dir__}/dbdataclasses/{pkg.name}.rst', 'w') as f:
                f.write(doc.as_rst())
        all = "\n   ".join(sorted([p.name for p in self.packages]))
        with open(f'{__dir__}/dbdataclasses/index.rst', 'w') as f:
            f.write(f'''
Dataclasses
===========

.. toctree::
   :maxdepth: 1
   
   {all}''')

    def _get_tag_name(self, class_name, service_name) -> Tag:
        if class_name[-3:] == 'Ext':
            # ClustersExt, DbfsExt, WorkspaceExt, but not ExternalLocations
            class_name = class_name.replace('Ext', 'API')
        class_name = class_name[:-3]
        for tag_name, t in self.mapping.items():
            if t.service.lower() == str(class_name).lower():
                return t
        raise KeyError(f'Cannot find {class_name} / {service_name} tag')

    def load_client(self, client, folder, label, description):
        client_services = []
        package_to_services = collections.defaultdict(list)
        client_prefix = 'w' if isinstance(client, WorkspaceClient) else 'a'
        service_docs = self.service_docs(client, client_prefix)
        for svc in service_docs:
            client_services.append(svc.service_name)
            package = svc.tag.package.name
            package_to_services[package].append((svc.service_name, svc.client_prefix + "." + svc.service_name))
            self._make_folder_if_not_exists(f'{__dir__}/{folder}/{package}')
            with open(f'{__dir__}/{folder}/{package}/{svc.service_name}.rst', 'w') as f:
                f.write(svc.as_rst())
        ordered_packages = []
        for pkg in self.packages:
            if pkg.name not in package_to_services:
                continue
            ordered_packages.append(pkg.name)
            # Order services inside the package by full path to have subservices grouped together
            package_to_services[pkg.name].sort(key=lambda x: x[1])
            ordered_services_names = [x[0] for x in package_to_services[pkg.name]]
            self._write_client_package_doc(folder, pkg, ordered_services_names)
        self._write_client_packages(folder, label, description, ordered_packages)

    def _write_client_packages(self, folder: str, label: str, description: str, packages: list[str]):
        """Writes out the top-level index for the APIs supported by a client."""
        self._make_folder_if_not_exists(f'{__dir__}/{folder}')
        with open(f'{__dir__}/{folder}/index.rst', 'w') as f:
            all = "\n   ".join([f'{name}/index' for name in sorted(packages)])
            f.write(f'''
{label}
{'=' * len(label)}

{description}

.. toctree::
   :maxdepth: 1

   {all}''')

    def _write_client_package_doc(self, folder: str, pkg: Package, services: list[str]):
        """Writes out the index for a single package supported by a client."""
        self._make_folder_if_not_exists(f'{__dir__}/{folder}/{pkg.name}')
        with open(f'{__dir__}/{folder}/{pkg.name}/index.rst', 'w') as f:
            all = "\n   ".join(services)
            f.write(f'''
{pkg.label}
{'=' * len(pkg.label)}

{pkg.description}

.. toctree::
   :maxdepth: 1

   {all}''')


if __name__ == '__main__':

    @credentials_strategy('noop', [])
    def noop_credentials(_: any):
        return lambda: {}

    gen = Generator()

    w = WorkspaceClient(credentials_provider=noop_credentials)
    gen.load_client(w, 'workspace', 'Workspace APIs', 'These APIs are available from WorkspaceClient')

    a = AccountClient(credentials_provider=noop_credentials)
    gen.load_client(a, 'account', 'Account APIs', 'These APIs are available from AccountClient')

    gen.write_dataclass_docs()
