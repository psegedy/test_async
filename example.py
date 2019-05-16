import asyncio


async def hello():
    await asyncio.sleep(3)
    return "Hello, world!"


async def main():
    print(await hello())

if __name__ == "__main__":
    # Python < 3.7
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())

    # Python 3.7+
    asyncio.run(main())
