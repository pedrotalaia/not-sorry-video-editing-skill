```
███╗   ██╗  ██████╗  ████████╗     ███████╗  ██████╗  ██████╗  ██████╗  ██╗   ██╗
████╗  ██║ ██╔═══██╗ ╚══██╔══╝     ██╔════╝ ██╔═══██╗ ██╔══██╗ ██╔══██╗ ╚██╗ ██╔╝
██╔██╗ ██║ ██║   ██║    ██║        ███████╗ ██║   ██║ ██████╔╝ ██████╔╝  ╚████╔╝
██║╚██╗██║ ██║   ██║    ██║        ╚════██║ ██║   ██║ ██╔══██╗ ██╔══██╗   ╚██╔╝
██║ ╚████║ ╚██████╔╝    ██║        ███████║ ╚██████╔╝ ██║  ██║ ██║  ██║    ██║
╚═╝  ╚═══╝  ╚═════╝     ╚═╝        ╚══════╝  ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝    ╚═╝
                    ▶  V I D E O   E D I T I N G   S K I L L  ◀
```

An agent skill for Claude Code and Codex that turns raw footage into short vertical
videos (Reels, TikTok, Shorts): storyboarding, cropping, subtitles, audio cleanup,
and checked 1080 × 1920 exports.

> [!IMPORTANT]
> **Requirements**
> - `ffmpeg` + `ffprobe` — cutting, cropping, audio cleanup, export, export checks
> - `python3` 3.9+ — bundled scripts
> - Speech-to-text — `faster-whisper` or `openai-whisper` (transcription & subtitles)
> - Optional Python libs — `numpy`, `opencv-python`, `mediapipe` (tracking, punch-ins, title-behind-head masks)
>
> Missing something? The agent checks and installs it for you (Python packages into a project `.venv`, system tools via pacman / apt / brew / winget). If `sudo` is needed, it shows you the exact command to run.

- How the agent works: [SKILL.md](SKILL.md)
- Editing rules: [references/editing-rules.md](references/editing-rules.md)
- Installation: [INSTALL.md](INSTALL.md)
