#!/usr/bin/env python3
"""
Add popular MCP servers to Claude Desktop config.
Run: python3 add_mcp_servers.py
Then restart Claude Desktop.
"""

import json
import os
import subprocess
import sys

CONFIG_PATH = os.path.expanduser(
    "~/Library/Application Support/Claude/claude_desktop_config.json"
)

def find_executable(name):
    """Find the absolute path of an executable."""
    # Common locations on macOS with Homebrew
    candidates = [
        "/opt/homebrew/bin/" + name,
        "/usr/local/bin/" + name,
        os.path.expanduser("~/.local/bin/" + name),
        "/usr/bin/" + name,
    ]
    for path in candidates:
        if os.path.isfile(path) and os.access(path, os.X_OK):
            return path
    # Try 'which' as fallback
    try:
        result = subprocess.run(["which", name], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return None

# Find absolute paths
uvx_path = find_executable("uvx")
npx_path = find_executable("npx")

print("Detected executables:")
print("  uvx:", uvx_path or "NOT FOUND")
print("  npx:", npx_path or "NOT FOUND")

if not uvx_path:
    print("")
    print("ERROR: uvx not found. Install it with:")
    print("  pip3 install uv")
    print("Then re-run this script.")
    sys.exit(1)

if not npx_path:
    print("")
    print("ERROR: npx not found. Install Node.js with:")
    print("  brew install node")
    print("Then re-run this script.")
    sys.exit(1)

# New MCP servers to add
NEW_SERVERS = {
    "fetch": {
        "command": uvx_path,
        "args": ["mcp-server-fetch"]
    },
    "filesystem": {
        "command": npx_path,
        "args": ["-y", "@modelcontextprotocol/server-filesystem",
                 os.path.expanduser("~")]
    },
    "memory": {
        "command": npx_path,
        "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "sequential-thinking": {
        "command": npx_path,
        "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
}

# Load or create config
if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)
else:
    config = {}

if "mcpServers" not in config:
    config["mcpServers"] = {}

# Add new servers
added = []
skipped = []
for name, server_config in NEW_SERVERS.items():
    if name not in config["mcpServers"]:
        config["mcpServers"][name] = server_config
        added.append(name)
    else:
        # Update existing entry to use absolute paths
        config["mcpServers"][name] = server_config
        skipped.append(name + " (updated with absolute path)")

# Save config
with open(CONFIG_PATH, "w") as f:
    json.dump(config, f, indent=2)

print("")
print("Config updated at:", CONFIG_PATH)
if added:
    print("  Added:", ", ".join(added))
if skipped:
    print("  Updated:", ", ".join(skipped))
print("")
print("Now QUIT Claude Desktop (Cmd+Q) and reopen it.")
print("Then click the hammer icon to see all tools.")
