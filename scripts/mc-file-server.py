#!/usr/bin/env python3
"""
MC File Server — Flask-based workspace file server for Mission Control
Tunnel: npx localtunnel --port 5001
"""
import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=['https://mc.marrs-mc.com'])
WORKSPACE = "/Users/openclaw_admin/.openclaw/workspace"
PORT = 5001

@app.route("/health")
def health():
    return jsonify({"status": "ok", "workspace": WORKSPACE})

@app.route("/file")
def file():
    file_path = request.args.get("path", "")
    if not file_path:
        return jsonify({"error": "Missing 'path' parameter"}), 400

    # Security: prevent directory traversal
    full_path = Path(WORKSPACE) / file_path
    try:
        full_path = full_path.resolve()
        if not str(full_path).startswith(WORKSPACE):
            return jsonify({"error": "Access denied"}), 403
    except:
        return jsonify({"error": "Invalid path"}), 400

    if not full_path.exists() or not full_path.is_file():
        return jsonify({"error": "File not found"}), 404

    try:
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        return jsonify({
            "path": str(full_path.relative_to(WORKSPACE)),
            "content": content,
            "size": len(content),
            "modified": os.path.getmtime(full_path)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def build_tree(root_path, base_path="", search=""):
    """Recursively build a nested tree of files and directories."""
    full = Path(WORKSPACE) / base_path if not base_path else Path(WORKSPACE) / base_path
    if not full.exists():
        return []
    items = []
    try:
        for f in sorted(full.iterdir()):
            rel = str(f.relative_to(WORKSPACE))
            if f.is_dir():
                children = build_tree(WORKSPACE, rel, search)
                dir_name_match = search and search in f.name.lower()
                # Always include dir if: no search, dir name matches, OR dir has matching children
                if search and not children and not dir_name_match:
                    continue
                items.append({
                    "name": f.name,
                    "path": rel,
                    "type": "directory",
                    "children": children
                })
            elif f.is_file():
                if search and search not in f.name.lower():
                    continue
                items.append({
                    "name": f.name,
                    "path": rel,
                    "type": "file",
                    "size": f.stat().st_size,
                    "modified": f.stat().st_mtime
                })
    except PermissionError:
        pass
    return items

@app.route("/list")
def list_dir():
    dir_path = request.args.get("path", ".")
    search = request.args.get("search", "").lower()

    # When search is provided and path is root, return full recursive tree
    if search and (dir_path == "." or dir_path == ""):
        tree = build_tree(WORKSPACE, "", search)
        return jsonify({"items": tree, "path": ".", "search": search})

    # Normal one-level listing (existing behaviour)
    full_path = Path(WORKSPACE) / dir_path
    try:
        full_path = full_path.resolve()
        if not str(full_path).startswith(WORKSPACE):
            return jsonify({"files": [], "path": dir_path}), 200
    except:
        return jsonify({"files": [], "path": dir_path}), 200

    if not full_path.exists() or not full_path.is_dir():
        return jsonify({"files": [], "path": dir_path}), 200

    files = []
    for f in sorted(full_path.iterdir()):
        if f.is_file() and (not search or search in f.name.lower()):
            files.append({
                "name": f.name,
                "path": str(f.relative_to(WORKSPACE)),
                "size": f.stat().st_size,
                "modified": f.stat().st_mtime
            })
    return jsonify({"files": files, "path": dir_path})

@app.route("/reports")
def reports():
    reports_dir = Path(WORKSPACE) / "reports"
    if not reports_dir.exists():
        return jsonify({"reports": []})

    files = []
    for f in sorted(reports_dir.glob("*.md"), reverse=True)[:20]:
        files.append({
            "name": f.name,
            "path": str(f.relative_to(WORKSPACE)),
            "size": f.stat().st_size,
            "modified": f.stat().st_mtime
        })
    return jsonify({"reports": files})

@app.route("/dreams")
def dreams():
    dreams_dir = Path(WORKSPACE) / "memory" / "rosie-dreams"
    if not dreams_dir.exists():
        return jsonify({"dreams": []})

    files = []
    for f in sorted(dreams_dir.glob("*.md"), reverse=True)[:10]:
        files.append({
            "name": f.name,
            "path": str(f.relative_to(WORKSPACE)),
            "size": f.stat().st_size,
            "modified": f.stat().st_mtime
        })
    return jsonify({"dreams": files})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=False, threaded=True)
