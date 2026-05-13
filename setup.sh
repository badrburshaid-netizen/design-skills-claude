#!/bin/bash
# ============================================================
# DESIGN SKILLS + DBA RESEARCH SKILLS CLAUDE - FULL AUTO SETUP
# One command to install everything and connect to Claude
# Usage: bash setup.sh
# ============================================================

set -e

REPO_DIR="$HOME/design-skills-claude"
CLAUDE_CONFIG_DIR="$HOME/Library/Application Support/Claude"
CLAUDE_CONFIG="$CLAUDE_CONFIG_DIR/claude_desktop_config.json"

echo ""
echo "=================================================="
echo " DESIGN SKILLS + DBA CLAUDE - AUTO SETUP"
echo " github.com/badrburshaid-netizen/design-skills-claude"
echo "=================================================="
echo ""

# Step 1: Clone or pull the repository
echo "[1/5] Setting up repository..."
if [ -d "$REPO_DIR" ]; then
  echo "  Repo already exists. Pulling latest changes..."
  cd "$REPO_DIR" && git pull
  echo "  Repository updated successfully"
else
  git clone https://github.com/badrburshaid-netizen/design-skills-claude.git "$REPO_DIR"
  echo "  Cloned to $REPO_DIR"
fi

# Step 2: Install Python MCP dependency
echo ""
echo "[2/5] Installing MCP Python package..."
pip3 install mcp --quiet
echo "  MCP installed successfully"

# Step 3: Verify Python files exist
echo ""
echo "[3/5] Verifying files..."
MISSING=0
for f in design_skills.py dba_skills.py mcp_server.py; do
  if [ -f "$REPO_DIR/$f" ]; then
    echo "  $f - OK"
  else
    echo "  ERROR: $f is missing!"
    MISSING=1
  fi
done

if [ $MISSING -eq 1 ]; then
  echo "  Some files are missing. Try running: cd $REPO_DIR && git pull"
  exit 1
fi

# Step 4: Test the skills scripts
echo ""
echo "[4/5] Running script tests..."
python3 "$REPO_DIR/design_skills.py" > /dev/null 2>&1 && echo "  design_skills.py - OK" || echo "  WARNING: design_skills.py had errors"
python3 -c "import sys; sys.path.insert(0,'$REPO_DIR'); from dba_skills import count_total_dba_skills; print(f'  dba_skills.py - OK ({count_total_dba_skills()} DBA skills loaded)')"
python3 -c "
import sys, subprocess
result = subprocess.run(['python3', '-c', 'import sys; sys.path.insert(0,"$REPO_DIR"); import mcp_server'], capture_output=True, text=True)
print('  mcp_server.py - ' + ('OK' if result.returncode == 0 else 'WARNING: ' + result.stderr[:100]))
"

# Step 5: Update Claude Desktop config
echo ""
echo "[5/5] Configuring Claude Desktop..."
mkdir -p "$CLAUDE_CONFIG_DIR"

if [ -f "$CLAUDE_CONFIG" ]; then
  echo "  Existing Claude config found. Updating MCP server entry..."
  python3 << PYEOF
import json, os
config_path = os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
repo_path = os.path.expanduser("~/design-skills-claude/mcp_server.py")
with open(config_path, "r") as f:
    config = json.load(f)
if "mcpServers" not in config:
    config["mcpServers"] = {}
config["mcpServers"]["design-dba-skills"] = {
    "command": "python3",
    "args": [repo_path]
}
with open(config_path, "w") as f:
    json.dump(config, f, indent=2)
print(f"  Config updated: {config_path}")
PYEOF
else
  echo "  Creating new Claude Desktop config..."
  python3 << PYEOF
import json, os
config_path = os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
repo_path = os.path.expanduser("~/design-skills-claude/mcp_server.py")
config = {
    "mcpServers": {
        "design-dba-skills": {
            "command": "python3",
            "args": [repo_path]
        }
    }
}
os.makedirs(os.path.dirname(config_path), exist_ok=True)
with open(config_path, "w") as f:
    json.dump(config, f, indent=2)
print(f"  Config created: {config_path}")
PYEOF
fi

# Final summary
echo ""
echo "=================================================="
echo " SETUP COMPLETE!"
echo "=================================================="
echo ""
echo "  Repo:   $REPO_DIR"
echo "  Config: $CLAUDE_CONFIG"
echo ""
echo "  NEXT STEP: Restart Claude Desktop"
echo "  After restart, Claude will have 13 new tools:"
echo ""
echo "  DESIGN TOOLS:"
echo "    - get_graphic_design_skills"
echo "    - get_photo_skills"
echo "    - get_presentation_skills"
echo "    - get_all_design_skills"
echo "    - search_design_skills"
echo ""
echo "  DBA RESEARCH TOOLS:"
echo "    - get_dba_research_methodology"
echo "    - get_dba_academic_writing"
echo "    - get_dba_statistical_software"
echo "    - get_dba_business_theory"
echo "    - get_dba_doctoral_competencies"
echo "    - get_bordeaux_dba_resources"
echo "    - get_all_dba_skills"
echo "    - search_dba_skills"
echo ""
echo "  Good luck with your DBA thesis at University of Bordeaux!"
echo "=================================================="
