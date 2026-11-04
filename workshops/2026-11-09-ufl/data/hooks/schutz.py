"""PreToolUse hook for Claude Code that blocks Edit and Write outside the project folder.

Shown in session 2 of the Uni for Life 2026 workshop. Register it in
.claude/settings.json with matcher "Edit|Write" and command
"python .claude/hooks/schutz.py". Exit code 2 blocks the tool call and
passes the stderr message back to the agent.
"""

import json
import os
import sys

daten = json.load(sys.stdin)
eingabe = daten.get("tool_input", {})
pfad = eingabe.get("file_path") or eingabe.get("notebook_path")
if not pfad:
    sys.exit(0)

projekt = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR") or daten.get("cwd", "."))
ziel = os.path.realpath(os.path.join(daten.get("cwd", projekt), pfad))
try:
    innen = os.path.commonpath([projekt, ziel]) == projekt
except ValueError:
    # Paths on different Windows drives have no common path.
    innen = False

if not innen:
    print(f"Blockiert: {ziel} liegt ausserhalb des Projektordners {projekt}.", file=sys.stderr)
    sys.exit(2)
