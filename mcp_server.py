#!/usr/bin/env python3
"""
MCP Server: Design Skills for Claude
=====================================
This MCP (Model Context Protocol) server exposes design skills data
as tools that Claude can call directly.

Installation:
  pip install mcp

Usage with Claude Desktop:
  Add to ~/Library/Application Support/Claude/claude_desktop_config.json:
  {
    "mcpServers": {
      "design-skills": {
        "command": "python3",
        "args": ["/path/to/mcp_server.py"]
      }
    }
  }

Repo: https://github.com/badrburshaid-netizen/design-skills-claude
"""

import json
import sys
from typing import Any

# MCP SDK import
try:
    from mcp.server import Server
    from mcp.server.stdio import stdio_server
    from mcp import types
except ImportError:
    print("ERROR: MCP SDK not installed. Run: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Import skills data from main module
from design_skills import (
    GRAPHIC_DESIGN_SKILLS,
    PHOTO_SKILLS,
    PRESENTATION_SKILLS,
    count_total_skills,
)

# ─────────────────────────────────────────────────────────────
# MCP SERVER SETUP
# ─────────────────────────────────────────────────────────────
server = Server("design-skills-claude")


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    """Return all available design skills tools."""
    return [
        types.Tool(
            name="get_graphic_design_skills",
            description=(
                "Returns the top skills needed for professional graphic design, "
                "organized by category: Foundations, Software, Branding, Print, "
                "Digital Design, and Soft Skills."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": (
                            "Optional: filter by category name. Options: "
                            "Foundations, Technical_Software, Branding_Identity, "
                            "Print_Production, Digital_Design, Soft_Creative_Skills. "
                            "Leave empty to get all categories."
                        ),
                    }
                },
            },
        ),
        types.Tool(
            name="get_photo_skills",
            description=(
                "Returns top skills for photography and photo selection for design, "
                "including how to select the best images, editing tools, "
                "stock platforms, and advanced techniques."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": (
                            "Optional: filter by category. Options: "
                            "Photography_Fundamentals, Photo_Editing, "
                            "Selecting_Photos_for_Design, Stock_Photo_Platforms, "
                            "Advanced_Photo_Skills. Leave empty for all."
                        ),
                    }
                },
            },
        ),
        types.Tool(
            name="get_presentation_skills",
            description=(
                "Returns top skills for creating professional presentations, "
                "including slide design principles, software tools, "
                "content structure, delivery tips, and standards."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": (
                            "Optional: filter by category. Options: "
                            "Design_Principles_for_Slides, Software_Tools, "
                            "Content_Structure, Visual_Enhancement, "
                            "Delivery_Communication, Professional_Standards. "
                            "Leave empty for all."
                        ),
                    }
                },
            },
        ),
        types.Tool(
            name="get_all_design_skills",
            description=(
                "Returns ALL design skills across all three domains: "
                "Graphic Design, Photography & Photo Selection, "
                "and Professional Presentations in a single structured response."
            ),
            inputSchema={"type": "object", "properties": {}},
        ),
        types.Tool(
            name="search_design_skills",
            description=(
                "Search across all design skills for a specific keyword. "
                "Returns all matching skills with their category and domain."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "Keyword to search for (e.g., 'Figma', 'color', 'typography')",
                    }
                },
                "required": ["keyword"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[types.TextContent]:
    """Handle tool calls from Claude."""

    if name == "get_graphic_design_skills":
        category = arguments.get("category", "").strip()
        if category and category in GRAPHIC_DESIGN_SKILLS:
            data = {category: GRAPHIC_DESIGN_SKILLS[category]}
        else:
            data = GRAPHIC_DESIGN_SKILLS
        return [types.TextContent(
            type="text",
            text=json.dumps({
                "domain": "Graphic Design",
                "skills": data,
                "total": sum(len(v) for v in data.values()),
            }, indent=2)
        )]

    elif name == "get_photo_skills":
        category = arguments.get("category", "").strip()
        if category and category in PHOTO_SKILLS:
            data = {category: PHOTO_SKILLS[category]}
        else:
            data = PHOTO_SKILLS
        return [types.TextContent(
            type="text",
            text=json.dumps({
                "domain": "Photography & Photo Selection",
                "skills": data,
                "total": sum(len(v) for v in data.values()),
            }, indent=2)
        )]

    elif name == "get_presentation_skills":
        category = arguments.get("category", "").strip()
        if category and category in PRESENTATION_SKILLS:
            data = {category: PRESENTATION_SKILLS[category]}
        else:
            data = PRESENTATION_SKILLS
        return [types.TextContent(
            type="text",
            text=json.dumps({
                "domain": "Professional Presentations",
                "skills": data,
                "total": sum(len(v) for v in data.values()),
            }, indent=2)
        )]

    elif name == "get_all_design_skills":
        return [types.TextContent(
            type="text",
            text=json.dumps({
                "source": "Claude AI + GitHub Design Roadmap Research",
                "repo": "https://github.com/badrburshaid-netizen/design-skills-claude",
                "total_skills": count_total_skills(),
                "domains": {
                    "graphic_design": GRAPHIC_DESIGN_SKILLS,
                    "photography_and_photo_selection": PHOTO_SKILLS,
                    "professional_presentations": PRESENTATION_SKILLS,
                }
            }, indent=2)
        )]

    elif name == "search_design_skills":
        keyword = arguments.get("keyword", "").lower()
        results = []
        all_domains = [
            ("Graphic Design", GRAPHIC_DESIGN_SKILLS),
            ("Photography & Photo Selection", PHOTO_SKILLS),
            ("Professional Presentations", PRESENTATION_SKILLS),
        ]
        for domain_name, domain_data in all_domains:
            for category, skills in domain_data.items():
                for skill in skills:
                    if keyword in skill.lower():
                        results.append({
                            "domain": domain_name,
                            "category": category.replace("_", " "),
                            "skill": skill,
                        })
        return [types.TextContent(
            type="text",
            text=json.dumps({
                "keyword": keyword,
                "matches_found": len(results),
                "results": results,
            }, indent=2)
        )]

    else:
        return [types.TextContent(
            type="text",
            text=json.dumps({"error": f"Unknown tool: {name}"})
        )]


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────
async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
