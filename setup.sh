#!/bin/bash
# ============================================================
#  DESIGN SKILLS CLAUDE - FULL AUTO SETUP SCRIPT
#  One command to install everything and connect to Claude
#  Usage: bash setup.sh
# ============================================================

set -e

REPO_DIR="$HOME/design-skills-claude"
CLAUDE_CONFIG_DIR="$HOME/Library/Application Support/Claude"
CLAUDE_CONFIG="$CLAUDE_CONFIG_DIR/claude_desktop_config.json"

echo ""
echo "=================================================="
echo "  DESIGN SKILLS CLAUDE - AUTO SETUP"
echo "  github.com/badrburshaid-netizen/design-skills-claude"
echo "=================================================="
echo ""

# Step 1: Clone the repository
echo "[1/5] Cloning repository..."
if [ -d "$REPO_DIR" ]; then
  echo "      Repo already exists. Pulling latest..."
  cd "$REPO_DIR" && git pull
else
  git clone https://github.com/badrburshaid-netizen/design-skills-claude.git "$REPO_DIR"
  echo "      Cloned to $REPO_DIR"
fi

# Step 2: Install Python MCP dependency
echo ""
echo "[2/5] Installing MCP Python package..."
pip3 install mcp --quiet
echo "      MCP installed successfully"

# Step 3: Verify Python files exist
echo ""
echo "[3/5] Verifying files..."
if [ -f "$REPO_DIR/design_skills.py" ] && [ -f "$REPO_DIR/mcp_server.py" ]; then
  echo "      design_skills.py - OK"
  echo "      mcp_server.py - OK"
else
  echo "      ERROR: Files missing. Check your clone."
  exit 1
fi

# Step 4: Test the skills script
echo ""
echo "[4/5] Running skills script test..."
python3 "$REPO_DIR/design_skills.py" > /dev/null 2>&1 && echo "      design_skills.py runs successfully" || echo "      WARNING: Script had errors"

# Step 5: Update Claude Desktop config
echo ""
echo "[5/5] Configuring Claude Desktop..."
mkdir -p "$CLAUDE_CONFIG_DIR"

# Check if config already exists
if [ -f "$CLAUDE_CONFIG" ]; then
  echo "      Existing Claude config found. Adding MCP server..."
  # Use Python to safely merge JSON
  python3 << PYEOF
import json, os

config_path = os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
repo_path = os.path.expanduser("~/design-skills-claude/mcp_server.py")

with open(config_path, "r") as f:
    config = json.load(f)

if "mcpServers" not in config:
    config["mcpServers"] = {}

config["mcpServers"]["design-skills"] = {
    "command": "python3",
    "args": [repo_path]
}

with open(config_path, "w") as f:
    json.dump(config, f, indent=2)

print(f"      Config updated: {config_path}")
PYEOF
else
  echo "      Creating new Claude Desktop config..."
  python3 << PYEOF
import json, os

config_path = os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
repo_path = os.path.expanduser("~/design-skills-claude/mcp_server.py")

config = {
    "mcpServers": {
        "design-skills": {
            "command": "python3",
            "args": [repo_path]
        }
    }
}

with open(config_path, "w") as f:
    json.dump(config, f, indent=2)

print(f"      Config created: {config_path}")
PYEOF
fi

# Final verification
echo ""
echo "=================================================="
echo "  SETUP COMPLETE!"
echo "=================================================="
echo ""
echo "  Repo:    $REPO_DIR"
echo "  Config:  $CLAUDE_CONFIG"
echo ""
echo "  NEXT STEP: Restart Claude Desktop"
echo "  After restart, Claude will have 5 new tools:"
echo ""
echo "    - get_graphic_design_skills"
echo "    - get_photo_skills"
echo "    - get_presentation_skills"
echo "    - get_all_design_skills"
echo "    - search_design_skills"
echo ""
echo "  Try asking Claude:"
echo "    'What are the top graphic design skills?'"
echo "    'How do I select photos for design?'"
echo "    'What skills do I need for presentations?'"
echo ""
echo "  Repo: github.com/badrburshaid-netizen/design-skills-claude"
echo "=================================================="
