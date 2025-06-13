[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/anjor-coinmarket-mcp-server-badge.png)](https://mseep.ai/app/anjor-coinmarket-mcp-server)

# Coinmarket MCP server

Coinmarket MCP Server

<a href="https://glama.ai/mcp/servers/6ag7ms62ns"><img width="380" height="200" src="https://glama.ai/mcp/servers/6ag7ms62ns/badge" alt="Coinmarket MCP server" /></a>

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

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Install

Install uv if you haven't already:
```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

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
        "/path/to/coinmarket_service",
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

#### Docker

You can also run the server using Docker:

```bash
# Build the image
docker build -t coinmarket-service .

# Run the container
docker run -e COINMARKET_API_KEY=your_api_key_here coinmarket-service
```

For Claude Desktop configuration with Docker:
```json
"mcpServers": {
  "coinmarket_service": {
    "command": "docker",
    "args": [
      "run",
      "--rm",
      "-e",
      "COINMARKET_API_KEY=<insert api key>",
      "coinmarket-service"
    ]
  }
}
```

## Troubleshooting

### "spawn uv ENOENT" Error

If you see this error, it means `uv` is not installed or not in your PATH:

1. **Install uv** following the instructions above
2. **Restart your terminal/Claude Desktop** after installation
3. **Verify installation**: Run `uv --version` in terminal
4. **Update PATH**: Make sure uv is in your system PATH

### Configuration Issues

- Replace `/path/to/coinmarket_service` with the actual path to your cloned repository
- Ensure your `COINMARKET_API_KEY` is valid
- The path should point to the root directory containing `pyproject.toml`


