import contextlib
import functools
import typing
from http.server import BaseHTTPRequestHandler


@contextlib.contextmanager
def http_fixture_server(handler: typing.Callable[[BaseHTTPRequestHandler], None]):
    from http.server import HTTPServer
    from threading import Thread

    class _handler(BaseHTTPRequestHandler):

        def __init__(self, handler: typing.Callable[[BaseHTTPRequestHandler], None], *args):
            self._handler = handler
            super().__init__(*args)

        def __getattr__(self, item):
            if 'do_' != item[0:3]:
                raise AttributeError(f'method {item} not found')
            return functools.partial(self._handler, self)

    handler_factory = functools.partial(_handler, handler)
    srv = HTTPServer(('localhost', 0), handler_factory)
    t = Thread(target=srv.serve_forever)
    try:
        t.daemon = True
        t.start()
        yield 'http://{0}:{1}'.format(*srv.server_address)
    finally:
        srv.shutdown()
