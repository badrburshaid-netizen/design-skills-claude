#!/usr/bin/env python3
"""
Add MCP servers to Claude Desktop configuration.
Uses full absolute paths to avoid PATH issues with Claude Desktop.
"""

import json
import os
import subprocess
import sys
import shutil

CONFIG_PATH = os.path.expanduser(
    "~/Library/Application Support/Claude/claude_desktop_config.json"
)

def find_executable(name):
    """Find the full path of an executable."""
    # Check common locations first
    common_paths = [
        os.path.expanduser("~/.local/bin/" + name),
        "/opt/homebrew/bin/" + name,
        "/usr/local/bin/" + name,
        "/usr/bin/" + name,
    ]
    for p in common_paths:
        if os.path.isfile(p) and os.access(p, os.X_OK):
            return p
    # Fall back to shutil.which
    found = shutil.which(name)
    if found:
        return found
    return None

def install_uv():
    """Install uv (which provides uvx) if not already installed."""
    uvx_path = find_executable("uvx")
    if uvx_path:
        print(f"uvx already installed at: {uvx_path}")
        return uvx_path
    
    print("Installing uv (provides uvx)...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "uv"],
            check=True, capture_output=True
        )
        uvx_path = find_executable("uvx")
        if uvx_path:
            print(f"uvx installed at: {uvx_path}")
            return uvx_path
    except subprocess.CalledProcessError:
        pass
    
    # Try curl install method
    try:
        subprocess.run(
            "curl -LsSf https://astral.sh/uv/install.sh | sh",
            shell=True, check=True
        )
        uvx_path = find_executable("uvx")
        if uvx_path:
            print(f"uvx installed at: {uvx_path}")
            return uvx_path
    except subprocess.CalledProcessError:
        pass
    
    print("WARNING: Could not install uvx. fetch server may not work.")
    return "uvx"  # fallback

def find_node_executables():
    """Find node and npx full paths."""
    node_path = find_executable("node")
    npx_path = find_executable("npx")
    return node_path, npx_path

def load_config():
    """Load existing Claude Desktop config."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    return {"mcpServers": {}}

def save_config(config):
    """Save Claude Desktop config."""
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Config saved to: {CONFIG_PATH}")

def main():
    print("=== MCP Server Setup for Claude Desktop ===")
    print()
    
    # Find executables
    uvx_path = install_uv()
    node_path, npx_path = find_node_executables()
    
    print(f"uvx path: {uvx_path}")
    print(f"node path: {node_path or 'NOT FOUND'}")
    print(f"npx path:  {npx_path or 'NOT FOUND'}")
    print()
    
    if not node_path or not npx_path:
        print("ERROR: Node.js/npx not found. Please install Node.js first:")
        print("  brew install node")
        sys.exit(1)
    
    # Load existing config
    config = load_config()
    if "mcpServers" not in config:
        config["mcpServers"] = {}
    
    # Determine repo path (filesystem server root)
    repo_path = os.path.expanduser("~/Documents/GitHub/design-skills-claude")
    if not os.path.exists(repo_path):
        repo_path = os.path.expanduser("~/Documents")
    
    # Define servers with FULL ABSOLUTE PATHS
    new_servers = {
        "fetch": {
            "command": uvx_path,
            "args": ["mcp-server-fetch"]
        },
        "filesystem": {
            "command": node_path,
            "args": [
                npx_path.replace("/npx", "/node_modules/.bin/") + "/../lib/node_modules/@modelcontextprotocol/server-filesystem/dist/index.js"
                if False else  # placeholder
                "--",  # will be replaced below
            ]
        },
        "memory": {
            "command": node_path,
            "args": [npx_path, "--yes", "@modelcontextprotocol/server-memory"]
        },
        "sequential-thinking": {
            "command": node_path,
            "args": [npx_path, "--yes", "@modelcontextprotocol/server-sequential-thinking"]
        }
    }
    
    # Fix filesystem server - use npx properly
    new_servers["filesystem"] = {
        "command": node_path,
        "args": [
            npx_path,
            "--yes",
            "@modelcontextprotocol/server-filesystem",
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Desktop"),
            repo_path
        ]
    }
    
    # Add servers to config
    added = []
    updated = []
    for name, server_config in new_servers.items():
        if name in config["mcpServers"]:
            config["mcpServers"][name] = server_config
            updated.append(name)
        else:
            config["mcpServers"][name] = server_config
            added.append(name)
    
    save_config(config)
    
    print()
    print("=== Results ===")
    if added:
        print(f"Added servers:   {', '.join(added)}")
    if updated:
        print(f"Updated servers: {', '.join(updated)}")
    
    print()
    print("Full paths used:")
    for name, srv in new_servers.items():
        print(f"  {name}: {srv['command']}")
    
    print()
    print("NEXT STEPS:")
    print("1. Quit Claude Desktop completely (Cmd+Q)")
    print("2. Reopen Claude Desktop")
    print("3. Look for the hammer icon in the chat input")
    print("4. You should see 5 MCP server groups")
    print()
    print("If fetch still fails, run this to check uvx:")
    print("  which uvx && uvx --version")

if __name__ == "__main__":
    main()
