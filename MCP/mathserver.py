from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int)->int:
    """
    Summary : Add two numbers
    """
    return a + b

@mcp.tool()
def multiply(a: int, b: int)->int:
    """Multiply two numbers"""
    return a * b

# the transport: "stdio" argument is called for:
# stdio is standard input/output to receive and respond to tool function calls


if __name__ == "__main__":
    mcp.run(transport="stdio")