#!/usr/bin/env python3
"""
MCP Server: Design Skills for Claude
=====================================
Zero external dependencies - works with Python 3.9+
Uses raw JSON-RPC over stdio (MCP protocol).

Claude Desktop config (already written to your Mac):
  ~/Library/Application Support/Claude/claude_desktop_config.json

Repo: https://github.com/badrburshaid-netizen/design-skills-claude
"""

import sys
import json
import os

# Add the directory containing this script to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from design_skills import (
    GRAPHIC_DESIGN_SKILLS,
    PHOTO_SKILLS,
    PRESENTATION_SKILLS,
    count_total_skills,
)

# ─────────────────────────────────────────────────────────────
# TOOL DEFINITIONS
# ─────────────────────────────────────────────────────────────
TOOLS = [
    {
        "name": "get_graphic_design_skills",
        "description": "Returns the top skills needed for professional graphic design, organized by category: Foundations, Software, Branding, Print, Digital Design, and Soft Skills.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Optional: filter by category. Options: Foundations, Technical_Software, Branding_Identity, Print_Production, Digital_Design, Soft_Creative_Skills. Leave empty for all."
                }
            }
        }
    },
    {
        "name": "get_photo_skills",
        "description": "Returns top skills for photography and photo selection for design, including how to select the best images, editing tools, stock platforms, and advanced techniques.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Optional: filter by category. Options: Photography_Fundamentals, Photo_Editing, Selecting_Photos_for_Design, Stock_Photo_Platforms, Advanced_Photo_Skills. Leave empty for all."
                }
            }
        }
    },
    {
        "name": "get_presentation_skills",
        "description": "Returns top skills for creating professional presentations, including slide design, software tools, content structure, delivery tips, and standards.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Optional: filter by category. Options: Design_Principles_for_Slides, Software_Tools, Content_Structure, Visual_Enhancement, Delivery_Communication, Professional_Standards. Leave empty for all."
                }
            }
        }
    },
    {
        "name": "get_all_design_skills",
        "description": "Returns ALL design skills across all three domains: Graphic Design, Photography and Photo Selection, and Professional Presentations in a single structured response.",
        "inputSchema": {"type": "object", "properties": {}}
    },
    {
        "name": "search_design_skills",
        "description": "Search across all design skills for a specific keyword. Returns all matching skills with their category and domain.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "keyword": {
                    "type": "string",
                    "description": "Keyword to search for (e.g. Figma, color, typography, lighting, stock)"
                }
            },
            "required": ["keyword"]
        }
    }
]

# ─────────────────────────────────────────────────────────────
# TOOL EXECUTION
# ─────────────────────────────────────────────────────────────
def execute_tool(name, arguments):
    if name == "get_graphic_design_skills":
        category = arguments.get("category", "").strip()
        data = {category: GRAPHIC_DESIGN_SKILLS[category]} if category and category in GRAPHIC_DESIGN_SKILLS else GRAPHIC_DESIGN_SKILLS
        return json.dumps({"domain": "Graphic Design", "skills": data, "total": sum(len(v) for v in data.values())}, indent=2)

    elif name == "get_photo_skills":
        category = arguments.get("category", "").strip()
        data = {category: PHOTO_SKILLS[category]} if category and category in PHOTO_SKILLS else PHOTO_SKILLS
        return json.dumps({"domain": "Photography and Photo Selection", "skills": data, "total": sum(len(v) for v in data.values())}, indent=2)

    elif name == "get_presentation_skills":
        category = arguments.get("category", "").strip()
        data = {category: PRESENTATION_SKILLS[category]} if category and category in PRESENTATION_SKILLS else PRESENTATION_SKILLS
        return json.dumps({"domain": "Professional Presentations", "skills": data, "total": sum(len(v) for v in data.values())}, indent=2)

    elif name == "get_all_design_skills":
        return json.dumps({
            "source": "Claude AI + GitHub Design Roadmap Research",
            "repo": "https://github.com/badrburshaid-netizen/design-skills-claude",
            "total_skills": count_total_skills(),
            "domains": {
                "graphic_design": GRAPHIC_DESIGN_SKILLS,
                "photography_and_photo_selection": PHOTO_SKILLS,
                "professional_presentations": PRESENTATION_SKILLS,
            }
        }, indent=2)

    elif name == "search_design_skills":
        keyword = arguments.get("keyword", "").lower()
        results = []
        for domain_name, domain_data in [
            ("Graphic Design", GRAPHIC_DESIGN_SKILLS),
            ("Photography and Photo Selection", PHOTO_SKILLS),
            ("Professional Presentations", PRESENTATION_SKILLS),
        ]:
            for category, skills in domain_data.items():
                for skill in skills:
                    if keyword in skill.lower():
                        results.append({"domain": domain_name, "category": category.replace("_", " "), "skill": skill})
        return json.dumps({"keyword": keyword, "matches_found": len(results), "results": results}, indent=2)

    else:
        return json.dumps({"error": f"Unknown tool: {name}"})

# ─────────────────────────────────────────────────────────────
# MCP JSON-RPC STDIO HANDLER
# ─────────────────────────────────────────────────────────────
def send(obj):
    msg = json.dumps(obj)
    sys.stdout.write(msg + "\n")
    sys.stdout.flush()

def handle(request):
    method = request.get("method", "")
    req_id = request.get("id")

    if method == "initialize":
        send({
            "jsonrpc": "2.0", "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "design-skills-claude", "version": "1.0.0"}
            }
        })

    elif method == "notifications/initialized":
        pass  # No response needed

    elif method == "tools/list":
        send({
            "jsonrpc": "2.0", "id": req_id,
            "result": {"tools": TOOLS}
        })

    elif method == "tools/call":
        params = request.get("params", {})
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})
        result_text = execute_tool(tool_name, arguments)
        send({
            "jsonrpc": "2.0", "id": req_id,
            "result": {
                "content": [{"type": "text", "text": result_text}],
                "isError": False
            }
        })

    elif method == "ping":
        send({"jsonrpc": "2.0", "id": req_id, "result": {}})

    else:
        if req_id is not None:
            send({
                "jsonrpc": "2.0", "id": req_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"}
            })

# ─────────────────────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────────────────────
def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
            handle(request)
        except json.JSONDecodeError:
            pass
        except Exception as e:
            sys.stderr.write(f"Error: {e}\n")
            sys.stderr.flush()

if __name__ == "__main__":
    main()
