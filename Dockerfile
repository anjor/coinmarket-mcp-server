FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Copy project files
COPY pyproject.toml uv.lock README.md ./
COPY src/ src/

# Install dependencies
RUN uv sync --frozen --no-cache

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"

# Expose port (if needed for future HTTP functionality)
EXPOSE 8080

# Run the MCP server
CMD ["uv", "run", "coinmarket_service"]