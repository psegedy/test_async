import pytest
import tornado.httpclient
import tornado.httpserver

from server import application

# You can redefine event_loop
#
# @pytest.yield_fixture
# def event_loop():
#     loop = asyncio.get_event_loop()
#     yield loop
#     loop.close()


@pytest.fixture
def http_server(event_loop):
    """Tornado async HTTP server."""
    # start server on port 8080
    server = tornado.httpserver.HTTPServer(application)
    server.listen(8080)
    yield server
    # stop server on cleanup
    server.stop()


@pytest.fixture
def http_client(http_server):
    """Tornado async HTTP client."""
    client = tornado.httpclient.AsyncHTTPClient()
    yield client
    # stop client on cleanup
    client.close()
