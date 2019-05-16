from example import hello


async def test_hello():
    assert "Hello world!" == await hello()
