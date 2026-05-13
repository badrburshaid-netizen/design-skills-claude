#!/usr/bin/env python3
"""
MCP Server: Design Skills + DBA Research Skills for Claude
===========================================================
Zero external dependencies - works with Python 3.9+
Uses raw JSON-RPC over stdio (MCP protocol).
Claude Desktop config (already written to your Mac):
~/Library/Application Support/Claude/claude_desktop_config.json
Repo: https://github.com/badrburshaid-netizen/design-skills-claude
"""

import sys
import json
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from design_skills import (
    GRAPHIC_DESIGN_SKILLS,
    PHOTO_SKILLS,
    PRESENTATION_SKILLS,
    count_total_skills,
)

from dba_skills import (
    RESEARCH_METHODOLOGY_SKILLS,
    ACADEMIC_WRITING_SKILLS,
    STATISTICAL_SOFTWARE_SKILLS,
    BUSINESS_THEORY_SKILLS,
    DOCTORAL_COMPETENCY_SKILLS,
    BORDEAUX_DBA_RESOURCES,
    count_total_dba_skills,
)

# ─────────────────────────────────────────────────────────────
# TOOL DEFINITIONS
# ─────────────────────────────────────────────────────────────
TOOLS = [
      # ── DESIGN SKILLS ──
    {
              "name": "get_graphic_design_skills",
              "description": "Returns the top skills needed for professional graphic design, organized by category.",
              "inputSchema": {
                            "type": "object",
                            "properties": {
                                              "category": {
                                                                    "type": "string",
                                                                    "description": "Optional: filter by category. Options: Foundations, Technical_Software, Branding_Identity, Print_Production, Digital_Design, Soft_Creative_Skills."
                                              }
                            }
              }
    },
      {
                "name": "get_photo_skills",
                "description": "Returns top skills for photography and photo selection for design.",
                "inputSchema": {
                              "type": "object",
                              "properties": {
                                                "category": {
                                                                      "type": "string",
                                                                      "description": "Optional: filter by category. Options: Photography_Fundamentals, Photo_Editing, Selecting_Photos_for_Design, Stock_Photo_Platforms, Advanced_Photo_Skills."
                                                }
                              }
                }
      },
      {
                "name": "get_presentation_skills",
                "description": "Returns top skills for creating professional presentations.",
                "inputSchema": {
                              "type": "object",
                              "properties": {
                                                "category": {
                                                                      "type": "string",
                                                                      "description": "Optional: filter by category. Options: Design_Principles_for_Slides, Software_Tools, Content_Structure, Visual_Enhancement, Delivery_Communication, Professional_Standards."
                                                }
                              }
                }
      },
      {
                "name": "get_all_design_skills",
                "description": "Returns ALL design skills across graphic design, photography, and presentations.",
                "inputSchema": {"type": "object", "properties": {}}
      },
      {
                "name": "search_design_skills",
                "description": "Search across all design skills for a specific keyword.",
                "inputSchema": {
                              "type": "object",
                              "properties": {
                                                "keyword": {
                                                                      "type": "string",
                                                                      "description": "Keyword to search for (e.g. Figma, color, typography)"
                                                }
                              },
                              "required": ["keyword"]
                }
      },
      # ── DBA RESEARCH SKILLS ──
      {
                "name": "get_dba_research_methodology",
                "description": "Returns research methodology skills for a DBA thesis: philosophical foundations, quantitative, qualitative, mixed-methods, and data collection.",
                "inputSchema": {
                              "type": "object",
                              "properties": {
                                                "category": {
                                                                      "type": "string",
                                                                      "description": "Optional: filter by category. Options: Philosophical_Foundations, Quantitative_Methods, Qualitative_Methods, Mixed_Methods, Data_Collection."
                                                }
                              }
                }
      },
      {
                "name": "get_dba_academic_writing",
                "description": "Returns academic writing and literature review skills for a DBA thesis at University of Bordeaux.",
                "inputSchema": {
                              "type": "object",
                              "properties": {
                                                "category": {
                                                                      "type": "string",
                                                                      "description": "Optional: filter by category. Options: Thesis_Structure, Literature_Review_Skills, Citation_Management, Academic_Writing_Style."
                                                }
                              }
                }
      },
      {
                "name": "get_dba_statistical_software",
                "description": "Returns statistical and data analysis software skills for DBA research: R, SPSS, SmartPLS, Python, Excel.",
                "inputSchema": {
                              "type": "object",
                              "properties": {
                                                "category": {
                                                                      "type": "string",
                                                                      "description": "Optional: filter by category. Options: R_Statistical_Computing, SPSS_Statistics, SmartPLS, Python_for_Research, Microsoft_Excel_for_Research."
                                                }
                              }
                }
      },
      {
                "name": "get_dba_business_theory",
                "description": "Returns key business and management theories for DBA research: strategic management, OB, innovation, finance, and marketing frameworks.",
                "inputSchema": {
                              "type": "object",
                              "properties": {
                                                "category": {
                                                                      "type": "string",
                                                                      "description": "Optional: filter by category. Options: Strategic_Management_Theories, Organizational_Behavior_Theories, Innovation_Entrepreneurship_Theories, Finance_Accounting_Frameworks, Marketing_Consumer_Theories."
                                                }
                              }
                }
      },
      {
                "name": "get_dba_doctoral_competencies",
                "description": "Returns doctoral competency skills for DBA: research design, critical thinking, thesis defense, professional skills, and AI tools for research.",
                "inputSchema": {
                              "type": "object",
                              "properties": {
                                                "category": {
                                                                      "type": "string",
                                                                      "description": "Optional: filter by category. Options: Research_Design, Critical_Thinking, Thesis_Defense_Preparation, Professional_Skills, AI_Tools_for_DBA_Research."
                                                }
                              }
                }
      },
      {
                "name": "get_bordeaux_dba_resources",
                "description": "Returns University of Bordeaux specific DBA resources: French academic system, key journals, and Bordeaux research centers.",
                "inputSchema": {
                              "type": "object",
                              "properties": {
                                                "category": {
                                                                      "type": "string",
                                                                      "description": "Optional: filter by category. Options: French_Academic_System, Key_Journals_for_DBA, Bordeaux_Research_Centers."
                                                }
                              }
                }
      },
      {
                "name": "get_all_dba_skills",
                "description": "Returns ALL DBA research skills across all domains: methodology, writing, statistics, theory, competencies, and Bordeaux-specific resources.",
                "inputSchema": {"type": "object", "properties": {}}
      },
      {
                "name": "search_dba_skills",
                "description": "Search across all DBA skills for a specific keyword (e.g. SEM, Zotero, Bordeaux, grounded theory, SPSS).",
                "inputSchema": {
                              "type": "object",
                              "properties": {
                                                "keyword": {
                                                                      "type": "string",
                                                                      "description": "Keyword to search for across all DBA skill categories"
                                                }
                              },
                              "required": ["keyword"]
                }
      },
]

# ─────────────────────────────────────────────────────────────
# TOOL EXECUTION
# ─────────────────────────────────────────────────────────────
def execute_tool(name, arguments):

      # ── DESIGN SKILLS ──
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
                for domain_name, domain_data in [("Graphic Design", GRAPHIC_DESIGN_SKILLS), ("Photography", PHOTO_SKILLS), ("Presentations", PRESENTATION_SKILLS)]:
                              for category, skills in domain_data.items():
                                                for skill in skills:
                                                                      if keyword in skill.lower():
                                                                                                results.append({"domain": domain_name, "category": category, "skill": skill})
                                                                                return json.dumps({"keyword": keyword, "matches": len(results), "results": results}, indent=2)

                                    # ── DBA SKILLS ──
      elif name == "get_dba_research_methodology":
                category = arguments.get("category", "").strip()
                data = {category: RESEARCH_METHODOLOGY_SKILLS[category]} if category and category in RESEARCH_METHODOLOGY_SKILLS else RESEARCH_METHODOLOGY_SKILLS
                return json.dumps({"domain": "DBA Research Methodology", "skills": data, "total": sum(len(v) for v in data.values())}, indent=2)

      elif name == "get_dba_academic_writing":
                category = arguments.get("category", "").strip()
                data = {category: ACADEMIC_WRITING_SKILLS[category]} if category and category in ACADEMIC_WRITING_SKILLS else ACADEMIC_WRITING_SKILLS
                return json.dumps({"domain": "DBA Academic Writing", "skills": data, "total": sum(len(v) for v in data.values())}, indent=2)

      elif name == "get_dba_statistical_software":
                category = arguments.get("category", "").strip()
                data = {category: STATISTICAL_SOFTWARE_SKILLS[category]} if category and category in STATISTICAL_SOFTWARE_SKILLS else STATISTICAL_SOFTWARE_SKILLS
                return json.dumps({"domain": "DBA Statistical Software", "skills": data, "total": sum(len(v) for v in data.values())}, indent=2)

      elif name == "get_dba_business_theory":
                category = arguments.get("category", "").strip()
                data = {category: BUSINESS_THEORY_SKILLS[category]} if category and category in BUSINESS_THEORY_SKILLS else BUSINESS_THEORY_SKILLS
                return json.dumps({"domain": "DBA Business Theory", "skills": data, "total": sum(len(v) for v in data.values())}, indent=2)

      elif name == "get_dba_doctoral_competencies":
                category = arguments.get("category", "").strip()
                data = {category: DOCTORAL_COMPETENCY_SKILLS[category]} if category and category in DOCTORAL_COMPETENCY_SKILLS else DOCTORAL_COMPETENCY_SKILLS
                return json.dumps({"domain": "DBA Doctoral Competencies", "skills": data, "total": sum(len(v) for v in data.values())}, indent=2)

      elif name == "get_bordeaux_dba_resources":
                category = arguments.get("category", "").strip()
                data = {category: BORDEAUX_DBA_RESOURCES[category]} if category and category in BORDEAUX_DBA_RESOURCES else BORDEAUX_DBA_RESOURCES
                return json.dumps({"domain": "University of Bordeaux DBA Resources", "skills": data, "total": sum(len(v) for v in data.values())}, indent=2)

      elif name == "get_all_dba_skills":
                return json.dumps({
                              "source": "Claude AI + University of Bordeaux DBA Research",
                              "institution": "University of Bordeaux - IAE Bordeaux",
                              "degree": "Doctorate of Business Administration (DBA)",
                              "total_skills": count_total_dba_skills(),
                              "domains": {
                                                "research_methodology": RESEARCH_METHODOLOGY_SKILLS,
                                                "academic_writing": ACADEMIC_WRITING_SKILLS,
                                                "statistical_software": STATISTICAL_SOFTWARE_SKILLS,
                                                "business_theory": BUSINESS_THEORY_SKILLS,
                                                "doctoral_competencies": DOCTORAL_COMPETENCY_SKILLS,
                                                "bordeaux_resources": BORDEAUX_DBA_RESOURCES,
                              }
                }, indent=2)

      elif name == "search_dba_skills":
                keyword = arguments.get("keyword", "").lower()
                results = []
                all_dba = [
                    ("Research Methodology", RESEARCH_METHODOLOGY_SKILLS),
                    ("Academic Writing", ACADEMIC_WRITING_SKILLS),
                    ("Statistical Software", STATISTICAL_SOFTWARE_SKILLS),
                    ("Business Theory", BUSINESS_THEORY_SKILLS),
                    ("Doctoral Competencies", DOCTORAL_COMPETENCY_SKILLS),
                    ("Bordeaux Resources", BORDEAUX_DBA_RESOURCES),
                ]
                for domain_name, domain_data in all_dba:
                              for category, skills in domain_data.items():
                                                for skill in skills:
                                                                      if keyword in skill.lower():
                                                                                                results.append({"domain": domain_name, "category": category, "skill": skill})
                                                                                return json.dumps({"keyword": keyword, "matches": len(results), "results": results}, indent=2)

      else:
                return json.dumps({"error": f"Unknown tool: {name}"})

  # ─────────────────────────────────────────────────────────────
  # JSON-RPC MCP PROTOCOL HANDLER
# ─────────────────────────────────────────────────────────────
def handle_request(req):
      method = req.get("method", "")
      req_id = req.get("id")

    if method == "initialize":
              return {
                            "jsonrpc": "2.0", "id": req_id,
                            "result": {
                                              "protocolVersion": "2024-11-05",
                                              "capabilities": {"tools": {}},
                                              "serverInfo": {"name": "design-dba-skills-claude", "version": "2.0.0"}
                            }
              }

elif method == "tools/list":
          return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS}}

elif method == "tools/call":
          params = req.get("params", {})
          tool_name = params.get("name", "")
          tool_args = params.get("arguments", {})
          try:
                        result_text = execute_tool(tool_name, tool_args)
                        return {
                            "jsonrpc": "2.0", "id": req_id,
                            "result": {"content": [{"type": "text", "text": result_text}]}
                        }
except Exception as e:
            return {
                              "jsonrpc": "2.0", "id": req_id,
                              "result": {"content": [{"type": "text", "text": f"Error: {str(e)}"}], "isError": True}
            }

elif method == "notifications/initialized":
        return None

else:
        return {
                      "jsonrpc": "2.0", "id": req_id,
                      "error": {"code": -32601, "message": f"Method not found: {method}"}
        }

# ─────────────────────────────────────────────────────────────
# MAIN LOOP
# ─────────────────────────────────────────────────────────────
def main():
      while True:
                try:
                              line = sys.stdin.readline()
                              if not line:
                                                break
                                            line = line.strip()
                              if not line:
                                                continue
                                            req = json.loads(line)
                              response = handle_request(req)
                              if response is not None:
                                                print(json.dumps(response), flush=True)
                except json.JSONDecodeError:
                              pass
except KeyboardInterrupt:
            break
except Exception as e:
            error_resp = {"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}
            print(json.dumps(error_resp), flush=True)

if __name__ == "__main__":
      main()
  
