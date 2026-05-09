# Design Skills Claude - MCP Integration

> Top skills for Graphic Design, Photography & Photo Selection, and Professional Presentations integrated directly into Claude via MCP.

**Repo:** [badrburshaid-netizen/design-skills-claude](https://github.com/badrburshaid-netizen/design-skills-claude)
**Source:** Claude AI + GitHub Design Roadmap Research

---

## What This Does

This repository contains a full MCP (Model Context Protocol) server that adds design skills knowledge directly into Claude Desktop as callable tools. Once installed, you can ask Claude:

- "What are the top graphic design skills I need?"
- "How do I select the best photos for my design project?"
- "What skills do I need to make professional presentations?"
- "Search design skills for Figma"

Claude will call the tools from this repo and return structured, expert answers.

---

## Files

| File | Description |
|------|-------------|
| design_skills.py | Master database of all design skills |
| mcp_server.py | MCP server that exposes skills as Claude tools |
| README.md | Setup guide and documentation |

---

## Skills Covered

### Graphic Design (40+ skills)
- Foundations: Color Theory, Typography, Layout, Visual Hierarchy
- Software: Illustrator, Photoshop, InDesign, Figma, Canva, CorelDRAW
- Branding, Print Production, Digital Design, Soft Skills

### Photography and Photo Selection (45+ skills)
- Photography fundamentals (exposure, lighting, composition)
- Editing tools (Lightroom, Photoshop, Capture One, Luminar AI)
- How to SELECT photos for design (10 key criteria)
- Stock platforms (Unsplash, Pexels, Shutterstock, Adobe Stock)
- Advanced techniques (AI upscaling, masking, compositing)

### Professional Presentations (45+ skills)
- Slide design principles (whitespace, hierarchy, data viz)
- Software (PowerPoint, Google Slides, Canva, Gamma, Prezi)
- Content structure (story arc, CTA, speaker notes)
- Delivery and communication (public speaking, virtual)
- Standards (font sizes, accessibility, branding compliance)

---

## Add to Claude Desktop (MCP Integration)

### Step 1: Clone the repo
```bash
git clone https://github.com/badrburshaid-netizen/design-skills-claude.git
cd design-skills-claude
```

### Step 2: Install dependencies
```bash
pip install mcp
```

### Step 3: Add to Claude Desktop config

Open your Claude Desktop config file:

Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Add this:
```json
{
  "mcpServers": {
    "design-skills": {
      "command": "python3",
      "args": ["/full/path/to/design-skills-claude/mcp_server.py"]
    }
  }
}
```

### Step 4: Restart Claude Desktop

After restarting, you will see 5 new tools available in Claude:

| Tool | Description |
|------|-------------|
| get_graphic_design_skills | Get graphic design skills by category |
| get_photo_skills | Get photography and photo selection skills |
| get_presentation_skills | Get professional presentation skills |
| get_all_design_skills | Get all skills at once |
| search_design_skills | Search skills by keyword |

---

## Run Standalone (Without Claude)

```bash
python3 design_skills.py
```

Exports: design_skills.json, design_skills.txt, SKILLS.md

---

## License
MIT - Free to use, modify, and distribute.
