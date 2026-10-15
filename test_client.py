import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(command="python", args=["job_hunt_server.py"])
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Tools on the menu:", [t.name for t in tools.tools])
            result = await session.call_tool("next_actions", {})
            print("Client called next_actions ->")
            print(result.content[0].text)

asyncio.run(main())

params = StdioServerParameters(command="python", args=["job_hunt_server.py"])

