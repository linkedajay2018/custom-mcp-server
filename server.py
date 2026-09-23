from datetime import datetime
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("my-first-server")
NOTES = []

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b

@mcp.tool()
def save_note(title: str, content: str) -> str:
    """Save a note with a title and content."""
    NOTES.append({"title": title, "content": content,
                  "saved_at": datetime.now().isoformat(timespec="seconds")})
    return f"Saved '{title}'. Total notes: {len(NOTES)}"

@mcp.tool()
def search_notes(keyword: str) -> str:
    """Search saved notes by keyword."""
    k = keyword.lower()
    hits = [n for n in NOTES if k in n["title"].lower() or k in n["content"].lower()]
    if not hits:
        return f"No notes found for '{keyword}'."
    return "\n".join(f"- {n['title']}: {n['content']}" for n in hits)

if __name__ == "__main__":
    mcp.run(transport="stdio")
