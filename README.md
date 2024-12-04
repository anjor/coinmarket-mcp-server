# Coinmarket MCP server

Coinmarket MCP Server

## Components

### Resources

The server implements a few of the [Coinmarket API](https://coinmarketcap.com/api/documentation/v1/#section/Introduction) endpoints
- Custom coinmarket:// URI scheme for accessing individual notes
- Each note resource has a name, description and text/plain mimetype

### Tools

The server implements two tools:
- `get-currency-listings`: Get the latest currency listings
- `get-quotes`: Get quotes for tokens
  - Takes "slug" (example: bitcoin) or "symbol" (example: BTC) as optional string argument

## Configuration

Requires coinmarket API key.

## Quickstart

### Install

#### Claude Desktop

On MacOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
On Windows: `%APPDATA%/Claude/claude_desktop_config.json`

<details>
  <summary>Development/Unpublished Servers Configuration</summary>
  ```
  "mcpServers": {
    "coinmarket_service": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/anjor/repos/anjor/coinmarket_service",
        "run",
        "coinmarket_service"
      ],
      "env": {
        "COINMARKET_API_KEY": "<insert api key>"
      }
    }
  }
  ```
</details>


