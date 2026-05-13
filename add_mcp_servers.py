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

# New MCP servers to add
NEW_SERVERS = {
    "fetch": {
        "command": "uvx",
        "args": ["mcp-server-fetch"]
    },
    "filesystem": {
        "command": "npx",
        "args": [
            "-y",
            "@modelcontextprotocol/server-filesystem",
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Desktop"),
            os.path.expanduser("~/design-skills-claude")
        ]
    },
    "memory": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "sequential-thinking": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
}

def check_tool(name):
    try:
        result = subprocess.run(
            ["which", name],
            capture_output=True, text=True
        )
        return result.returncode == 0
    except Exception:
        return False

def main():
    print()
    print("=" * 50)
    print(" ADD MCP SERVERS TO CLAUDE DESKTOP")
    print("=" * 50)
    print()

    # Check prerequisites
    print("[1/3] Checking prerequisites...")
    has_npx = check_tool("npx")
    has_uvx = check_tool("uvx")
    has_node = check_tool("node")

    print(f"  node: {'OK' if has_node else 'MISSING - install from nodejs.org'}")
    print(f"  npx:  {'OK' if has_npx else 'MISSING - comes with Node.js'}")
    print(f"  uvx:  {'OK' if has_uvx else 'MISSING - install with: pip3 install uv'}")

    if not has_node or not has_npx:
        print()
        print("  Node.js is required for most servers.")
        print("  Install it from: https://nodejs.org")
        print("  Then re-run this script.")
        print()
        choice = input("  Continue anyway? (y/n): ").strip().lower()
        if choice != "y":
            sys.exit(0)

    # Install uvx if missing
    if not has_uvx:
        print()
        print("  Installing uv/uvx for the fetch server...")
        os.system("pip3 install uv --quiet")
        print("  uvx installed.")

    # Load existing config
    print()
    print("[2/3] Updating Claude Desktop config...")

    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
        print(f"  Existing config found.")
    else:
        config = {}
        print("  No existing config. Creating new one.")

    if "mcpServers" not in config:
        config["mcpServers"] = {}

    # Show what will be added
    existing = list(config["mcpServers"].keys())
    to_add = []
    to_skip = []

    for name in NEW_SERVERS:
        if name in config["mcpServers"]:
            to_skip.append(name)
        else:
            to_add.append(name)

    if existing:
        print(f"  Already configured: {', '.join(existing)}")
    if to_skip:
        print(f"  Skipping (already exist): {', '.join(to_skip)}")
    if to_add:
        print(f"  Adding: {', '.join(to_add)}")

    # Add new servers
    for name in to_add:
        config["mcpServers"][name] = NEW_SERVERS[name]

    # Save config
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)

    print()
    print("[3/3] Config saved!")
    print(f"  Path: {CONFIG_PATH}")

    # Show final config
    print()
    print("  Active MCP servers:")
    for name in config["mcpServers"]:
        print(f"    - {name}")

    print()
    print("=" * 50)
    print(" DONE!")
    print("=" * 50)
    print()
    print("  ACTION REQUIRED:")
    print("  Quit Claude Desktop (Cmd+Q) and reopen it.")
    print()
    print("  New tools you will have:")
    print("  - fetch:               Read any webpage or article")
    print("  - filesystem:          Read/write your Mac files")
    print("  - memory:              Remember facts across chats")
    print("  - sequential-thinking: Deep step-by-step reasoning")
    print()
    print("  All tools ready for your DBA thesis work!")
    print("=" * 50)
    print()

if __name__ == "__main__":
    main()
