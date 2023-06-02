from ..service import workspace

ExportFormat = workspace.ExportFormat

class WorkspaceExt(workspace.WorkspaceAPI):
    def direct_download(self, path: str, *, format: ExportFormat = ExportFormat.SOURCE) -> bytes:
        return self._api.do('GET', '/api/2.0/workspace/export', query={
            'path': path,
            'direct_download': 'true',
            'format': format.value
        }, raw=True)