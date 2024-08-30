import json
import urllib.parse
from typing import Dict, List

import requests


class RoundTripLogger:

    def __init__(self,
                 response: requests.Response,
                 debug_headers: bool,
                 debug_truncate_bytes: int,
                 raw=False):
        self._debug_headers = debug_headers
        self._debug_truncate_bytes = max(debug_truncate_bytes, 96)
        self._raw = raw
        self._response = response

    def generate(self) -> str:
        request = self._response.request
        url = urllib.parse.urlparse(request.url)
        query = ''
        if url.query:
            query = f'?{urllib.parse.unquote(url.query)}'
        sb = [f'{request.method} {urllib.parse.unquote(url.path)}{query}']
        if self._debug_headers:
            for k, v in request.headers.items():
                sb.append(f'> * {k}: {self._only_n_bytes(v, self._debug_truncate_bytes)}')
        if request.body:
            sb.append("> [raw stream]" if self._raw else self._redacted_dump("> ", request.body))
        sb.append(f'< {self._response.status_code} {self._response.reason}')
        if self._raw and self._response.headers.get('Content-Type', None) != 'application/json':
            # Raw streams with `Transfer-Encoding: chunked` do not have `Content-Type` header
            sb.append("< [raw stream]")
        elif self._response.content:
            sb.append(self._redacted_dump("< ", self._response.content.decode('utf-8')))
        return '\n'.join(sb)

    @staticmethod
    def _mask(m: Dict[str, any]):
        for k in m:
            if k in {'bytes_value', 'string_value', 'token_value', 'value', 'content'}:
                m[k] = "**REDACTED**"

    @staticmethod
    def _map_keys(m: Dict[str, any]) -> List[str]:
        keys = list(m.keys())
        keys.sort()
        return keys

    @staticmethod
    def _only_n_bytes(j: str, num_bytes: int = 96) -> str:
        diff = len(j.encode('utf-8')) - num_bytes
        if diff > 0:
            return f"{j[:num_bytes]}... ({diff} more bytes)"
        return j

    def _recursive_marshal_dict(self, m, budget) -> dict:
        out = {}
        self._mask(m)
        for k in sorted(m.keys()):
            raw = self._recursive_marshal(m[k], budget)
            out[k] = raw
            budget -= len(str(raw))
        return out

    def _recursive_marshal_list(self, s, budget) -> list:
        out = []
        for i in range(len(s)):
            if i > 0 >= budget:
                out.append("... (%d additional elements)" % (len(s) - len(out)))
                break
            raw = self._recursive_marshal(s[i], budget)
            out.append(raw)
            budget -= len(str(raw))
        return out

    def _recursive_marshal(self, v: any, budget: int) -> any:
        if isinstance(v, dict):
            return self._recursive_marshal_dict(v, budget)
        elif isinstance(v, list):
            return self._recursive_marshal_list(v, budget)
        elif isinstance(v, str):
            return self._only_n_bytes(v, self._debug_truncate_bytes)
        else:
            return v

    def _redacted_dump(self, prefix: str, body: str) -> str:
        if len(body) == 0:
            return ""
        try:
            # Unmarshal body into primitive types.
            tmp = json.loads(body)
            max_bytes = 96
            if self._debug_truncate_bytes > max_bytes:
                max_bytes = self._debug_truncate_bytes
            # Re-marshal body taking redaction and character limit into account.
            raw = self._recursive_marshal(tmp, max_bytes)
            return "\n".join([f'{prefix}{line}' for line in json.dumps(raw, indent=2).split("\n")])
        except json.JSONDecodeError:
            return f'{prefix}[non-JSON document of {len(body)} bytes]'
