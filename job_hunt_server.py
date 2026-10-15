from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jobhunt")

@mcp.tool()
def list_targets() -> str:
    """List Boss's India job hunt target companies and roles."""
    return (
        "1. Meltwater - AI Engineer, Team Lead (Hyderabad)\n"
        "2. Vertafore - Sr. Manager, SRE (Hyderabad)\n"
        "3. Pulsora - AI Engineer (Hyderabad)\n"
        "4. HighRadius - SRE (Hyderabad)\n"
        "5. Charles Schwab - Sr Manager SRE (Hyderabad)"
    )

#Tool #2: log_application — this one takes inputs (like your count_big dial) and writes to a file. Add this under tool #1:
@mcp.tool()
def log_application(company: str, role: str) -> str:
    """Log a job application with today's date."""
    from datetime import date
    line = f"{date.today()} | {company} | {role}\n"
    with open("applications.txt", "a") as f:
        f.write(line)
    return f"Logged: {company} - {role}"
#Tool #3: get_status — reads the tracker back. Add this:
@mcp.tool()
def get_status() -> str:
    """Show all logged job applications."""
    try:
        with open("applications.txt") as f:
            content = f.read().strip()
        return content if content else "No applications logged yet."
    except FileNotFoundError:
        return "No applications logged yet."
#Tool #4 (last one): next_actions — the AI tells you what to do today. Type this:
@mcp.tool()
def next_actions() -> str:
    """Suggest today's job hunt actions."""
    try:
        with open("applications.txt") as f:
            lines = [l for l in f.read().strip().split("\n") if l.strip()]
    except FileNotFoundError:
        lines = []
    targets = ["Meltwater", "Vertafore", "Pulsora", "HighRadius", "Charles Schwab"]
    applied = [t for t in targets if any(t.lower() in l.lower() for l in lines)]
    remaining = [t for t in targets if t not in applied]
    out = f"Applied ({len(applied)}): {', '.join(applied) if applied else 'none'}\n"
    out += f"Still to apply ({len(remaining)}): {', '.join(remaining) if remaining else 'none'}\n"
    out += "Today: " + (f"apply to {remaining[0]} next." if remaining else "follow up on your applications.")
    return out
if __name__ == "__main__":
    mcp.run()

