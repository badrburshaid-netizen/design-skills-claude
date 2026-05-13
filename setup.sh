#!/bin/bash
# ============================================================
# DESIGN SKILLS + DBA RESEARCH SKILLS CLAUDE - FULL AUTO SETUP
# No external dependencies required - pure Python 3.9+
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
echo "[1/4] Setting up repository..."
if [ -d "$REPO_DIR" ]; then
  echo "  Repo already exists. Pulling latest changes..."
  cd "$REPO_DIR" && git pull
  echo "  Repository updated successfully"
else
  git clone https://github.com/badrburshaid-netizen/design-skills-claude.git "$REPO_DIR"
  echo "  Cloned to $REPO_DIR"
fi

# Step 2: Check Python version (3.9+ required, no pip packages needed)
echo ""
echo "[2/4] Checking Python..."
PYTHON_VERSION=$(python3 --version 2>&1)
echo "  Found: $PYTHON_VERSION"
python3 -c "import sys; v=sys.version_info; assert v >= (3,9), f'Python 3.9+ required, got {v.major}.{v.minor}'" && echo "  Python OK - zero external dependencies needed!" || {
  echo "  ERROR: Python 3.9+ is required. Install from https://python.org"
  exit 1
}

# Step 3: Verify all Python files and syntax
echo ""
echo "[3/4] Verifying files and syntax..."
MISSING=0
for f in design_skills.py dba_skills.py mcp_server.py; do
  if [ -f "$REPO_DIR/$f" ]; then
    echo "  $f - found"
  else
    echo "  ERROR: $f is missing!"
    MISSING=1
  fi
done

if [ $MISSING -eq 1 ]; then
  echo "  Some files are missing. Try: cd $REPO_DIR && git pull"
  exit 1
fi

cd "$REPO_DIR"
python3 -c "
import sys
sys.path.insert(0, '.')
from design_skills import count_total_skills
from dba_skills import count_total_dba_skills
print(f'  design_skills.py - OK ({count_total_skills()} design skills)')
print(f'  dba_skills.py    - OK ({count_total_dba_skills()} DBA skills)')
"
python3 -m py_compile mcp_server.py && echo "  mcp_server.py    - OK (syntax verified)"

# Step 4: Update Claude Desktop config
echo ""
echo "[4/4] Configuring Claude Desktop..."
mkdir -p "$CLAUDE_CONFIG_DIR"

if [ -f "$CLAUDE_CONFIG" ]; then
  echo "  Existing Claude config found. Updating..."
  python3 << PYEOF
import json, os
config_path = os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
repo_path = os.path.expanduser("~/design-skills-claude/mcp_server.py")
with open(config_path, "r") as f:
    config = json.load(f)
if "mcpServers" not in config:
    config["mcpServers"] = {}
config["mcpServers"].pop("design-skills", None)
config["mcpServers"]["design-dba-skills"] = {
    "command": "python3",
    "args": [repo_path]
}
with open(config_path, "w") as f:
    json.dump(config, f, indent=2)
print(f"  Config saved: {config_path}")
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

echo ""
echo "=================================================="
echo " SETUP COMPLETE!"
echo "=================================================="
echo ""
echo "  Repo:   $REPO_DIR"
echo "  Config: $CLAUDE_CONFIG"
echo ""
echo "  ACTION REQUIRED: Quit Claude Desktop (Cmd+Q)"
echo "  then reopen it to activate the 13 new tools."
echo ""
echo "  DBA TOOLS: get_dba_research_methodology,"
echo "    get_dba_academic_writing, get_dba_statistical_software,"
echo "    get_dba_business_theory, get_dba_doctoral_competencies,"
echo "    get_bordeaux_dba_resources, get_all_dba_skills, search_dba_skills"
echo ""
echo "  Good luck with your DBA thesis at University of Bordeaux!"
echo "=================================================="
