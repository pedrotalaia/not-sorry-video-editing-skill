# Install for Claude Code and Codex

This folder is one shared skill. Both apps read `SKILL.md`, the editing rules,
and the export checker from the same source, so edits stay in sync.

Run from this folder:

```bash
python3 scripts/install-skill.py
```

The installer links Claude Code at `~/.claude/skills/video-editing` and Codex at
`~/.agents/skills/video-editing`. If this folder already lives directly in
`~/.agents/skills`, Codex already discovers it and no extra link is created.
Existing files or links pointing elsewhere are preserved; rerunning is safe.
Keep this source folder in place while either app uses it.

Invoke `/video-editing` in Claude Code or `$video-editing` in Codex. The skill
also supports automatic selection for relevant video-editing requests. It will
be available on your next Codex turn; check each app's `/skills` list.

These paths install for local Claude Code and Codex, not the Claude web app.
See the official [Claude Code skill documentation](https://code.claude.com/docs/en/skills)
and [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills).
