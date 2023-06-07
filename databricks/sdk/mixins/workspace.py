import typing

from ..service import workspace

ExportFormat = workspace.ExportFormat
Language = workspace.Language


def _fqcn(x: any) -> str:
    return f'{x.__module__}.{x.__name__}'


class WorkspaceExt(workspace.WorkspaceAPI):

    def upload(self,
               path: str,
               content: typing.BinaryIO,
               *,
               format: ExportFormat = ExportFormat.AUTO,
               language: Language = None):
        if not isinstance(format, ExportFormat):
            raise ValueError(
                f'format is expected to be {_fqcn(ExportFormat)}, but got {_fqcn(format.__class__)}')
        if language and not isinstance(language, Language):
            raise ValueError(
                f'language is expected to be {_fqcn(Language)}, but got {_fqcn(language.__class__)}')
        data = {'path': path, 'format': format.value}
        if language:
            data['language'] = language.value
        return self._api.do('POST', '/api/2.0/workspace/import', files={'content': content}, data=data)

    def download(self, path: str, *, format: ExportFormat = ExportFormat.AUTO) -> typing.BinaryIO:
        return self._api.do('GET',
                            '/api/2.0/workspace/export',
                            query={
                                'path': path,
                                'direct_download': 'true',
                                'format': format.value
                            },
                            raw=True)
