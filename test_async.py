import pytest

from example import hello


@pytest.mark.asyncio
async def test_hello():
    assert "Hello, world!" == await hello()
