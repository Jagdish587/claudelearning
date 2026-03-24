import asyncio
from fastmcp import Client

async def main():
    async with Client("http://127.0.0.1:8000/mcp") as client:

        # List available tools
        tools = await client.list_tools()
        print("Available tools:", tools)

        # # Call greet_user
        # res = await client.call_tool("greet_user", {"name": "Jagdish"})
        # print("greet_user:", res)

        # Call add
        res = await client.call_tool("add", {"a": 30, "b": 5})
        print("jagdish add:", res)



if __name__ == "__main__":
    asyncio.run(main())