import pytest


@pytest.mark.asyncio
async def test_hello(http_client):
    """Test asynchronous web server."""
    resp = await http_client.fetch("http://localhost:8080/")
    assert resp.body == b"Hello, world"
