from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

def main():
    print("Hello from lark-msg-helper!")
    mcp.run()


if __name__ == "__main__":
    main()
