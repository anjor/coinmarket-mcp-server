import os

from dotenv import load_dotenv
import requests
import json
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
from pydantic import AnyUrl
import mcp.server.stdio

load_dotenv()
API_KEY = os.getenv("COINMARKET_API_KEY")
if not API_KEY:
    raise ValueError("Missing COINMARKETCAP_API_KEY environment variable")


async def get_currency_listings():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'2',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': API_KEY,
    }

    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status()
    data = json.loads(response.text)
    return data

server = Server("coinmarket_service")

@server.list_resources()
async def handle_list_resources() -> list[types.Resource]:
    """
    List available coinmarket resources.
    """
    return [
        types.Resource(
            uri=AnyUrl("coinmarket://cryptocurrency/listings"),
            name="Latest cryptocurrency listings from coinmarket",
            description="Cryptocurrency listings",
            mimeType="application/json",
        )
    ]

@server.read_resource()
async def handle_read_resource(uri: AnyUrl) -> str:
    if uri.scheme != "coinmarket":
        raise ValueError(f"Unsupported scheme: {uri.scheme}")
    if uri.path != "/listings":
        raise ValueError(f"Unsupported path: {uri.path}")

    try:
        data = await get_currency_listings()
        return json.dumps(data, indent=2)
    except Exception as e:
        raise RuntimeError(f"Failed to fetch data: {e}")


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """
    List available tools.
    Each tool specifies its arguments using JSON Schema validation.
    """
    return [
        types.Tool(
            name="get_currency_listings",
            description="Get latest cryptocurrency listings",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """
    Handle tool execution requests.
    Tools can modify server state and notify clients of changes.
    """
    if name != "get_currency_listings":
        raise ValueError(f"Unknown tool: {name}")

    try:
        data = await get_currency_listings()
        return [
            types.TextContent(
                type="text",
                text=json.dumps(data, indent=2),
            )
        ]
    except Exception as e:
        raise RuntimeError(f"Failed to fetch data: {e}")


async def main():
    # Run the server using stdin/stdout streams
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="coinmarket_service",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
