#!env python3
import inspect
import json
import os.path
import typing
from dataclasses import dataclass
from pathlib import Path

from databricks.sdk import WorkspaceClient, AccountClient
from databricks.sdk.core import credentials_provider

__dir__ = os.path.dirname(__file__)
__examples__ = Path(f'{__dir__}/../examples').absolute()


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
    doc_name: str
    class_name: str
    methods: list[MethodDoc]
    doc: str

    def as_rst(self) -> str:
        if not self.doc:
            self.doc = '' # TODO: fill from parent
        out = [
            self.doc_name,
            '=' * len(self.doc_name),
            f'.. py:class:: {self.class_name}',
            '', f'    {self.doc}']
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


def class_methods(inst, service_name) -> list[MethodDoc]:
    method_docs = []
    for name in dir(inst):
        if name[0] == '_':
            # private members
            continue
        instance_attr = getattr(inst, name)
        if not callable(instance_attr):
            continue

        args = inspect.getfullargspec(instance_attr)
        method_docs.append(MethodDoc(
            method_name=name,
            required_args=args.args[1:],
            kwonly_args=args.kwonlyargs,
            doc=instance_attr.__doc__
        ))
    return method_docs


def service_docs(client_inst, tag_mapping) -> list[ServiceDoc]:
    ignore_client_fields = ('config', 'dbutils', 'api_client', 'files')
    all = []
    for service_name, service_inst in    client_inst.__dict__.items():
        if service_name in ignore_client_fields:
            continue
        class_doc = service_inst.__doc__
        # if class_doc is not None:
        #     bases = service_inst.__class__.__bases__
        #     if len(bases) > 0:
        #         class_doc = bases[0].__doc__
        class_name = service_inst.__class__.__name__
        if class_name[-3:] == 'Ext':
            # ClustersExt, DbfsExt, WorkspaceExt, but not ExternalLocations
            class_name = class_name.replace('Ext', 'API')
        all.append(ServiceDoc(
            service_name=service_name,
            doc_name=tag_mapping.get(class_name, service_name),
            class_name=class_name,
            doc=class_doc,
            methods=class_methods(service_inst, service_name)
        ))
    return all


if __name__ == '__main__':
    @credentials_provider('noop', [])
    def noop_credentials(_: any):
        return lambda: {}

    tag_mapping = {}
    with open(os.path.expanduser('~/.openapi-codegen.json'), 'r') as f:
        config = json.load(f)
        if 'spec' not in config:
            raise ValueError('Cannot find OpenAPI spec')
        with open(config['spec'], 'r') as fspec:
            spec = json.load(fspec)
            for tag in spec['tags']:
                tag_mapping[f"{tag['x-databricks-service']}API"] = tag['name']

    w = WorkspaceClient(credentials_provider=noop_credentials)

    workspace_services = []
    for svc in service_docs(w, tag_mapping):
        workspace_services.append(svc.service_name)
        with open(f'{__dir__}/workspace/{svc.service_name}.rst', 'w') as f:
            f.write(svc.as_rst())
    with open(f'{__dir__}/workspace/index.rst', 'w') as f:
        all = "\n  ".join(workspace_services)
        f.write(f'''
Workspace APIs
==============
 
These apis are available from WorkspaceClient
 
.. toctree::
  :maxdepth: 1
  
  {all}''')

    a = AccountClient(credentials_provider=noop_credentials)

    account_services = []
    for svc in service_docs(a, tag_mapping):
        account_services.append(svc.service_name)
        with open(f'{__dir__}/account/{svc.service_name}.rst', 'w') as f:
            f.write(svc.as_rst())
    with open(f'{__dir__}/account/index.rst', 'w') as f:
        all = "\n  ".join(account_services)
        f.write(f'''
Account APIs
============
 
These apis are available from AccountClient
 
.. toctree::
  :maxdepth: 1
  
  {all}''')
