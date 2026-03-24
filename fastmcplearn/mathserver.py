from fastmcp import FastMCP

mcp = FastMCP("Fast MCP Demo Server")


@mcp.tool
def greet_user(name: str) -> str:
    """Greet a user by name"""
    return f"Hello, {name}"

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Jadish FILE IS RUNNING")
    mcp.run(transport="stdio")