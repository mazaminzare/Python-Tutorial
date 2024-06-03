import asyncio
import aiohttp


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net"
    ]

    # Schedule all fetch operations concurrently
    tasks = [fetch(url) for url in urls]

    # Wait for all tasks to complete and gather their results
    results = await asyncio.gather(*tasks)

    for url, content in zip(urls, results):
        print(f"Content from {url}: {content[:100]}...")  # Print first 100 characters of each response


# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
