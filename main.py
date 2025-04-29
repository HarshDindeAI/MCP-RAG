from mcp.server.fastmcp import FastMCP
from search import search_tool
mcp = FastMCP("MCP-RAG")



@mcp.tool()
def search(query: str) -> str:
    """Searches the vector store for the most relevant documents to the query.
    
    Args:
    query (str): The query to search for.
    
    Returns:
    str: The text of the most relevant documents.
    """
    
    return search_tool(query)

@mcp.prompt("search_prompt")
def search_prompt(query: str) -> str:   
    """Prompt to search the vector store for the most relevant documents to the query.
    
    Args:
    query (str): The query to search for.
    
    Returns:
    str: The text of the most relevant documents.
    """
    
    return f"You are a helpfull assistant , who is has access of a search tool which contain knowladge. You can use the search tool to find the most relevant documents to the query. The query is: {query}. Please provide a detailed answer based on the search results." \

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"