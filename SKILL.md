---
name: video-editing
description: "Review recorded footage and create or revise short-form videos (Reels, TikTok shorts), handling everything from initial clip recommendations, full storyboarding, subtitle generation, selective cropping, audio cleanup, to final vertical exports. Use for projects with local footage and optional assets or style references."
---

# Video Editing

Turn the current project's footage into useful, self-contained short videos using Pedro's editing preferences. Treat project paths as relative to the user's project, not this installed skill directory.

Read [the editing rules](references/editing-rules.md) before planning a new project or making a full edit. For a narrow revision, consult the relevant sections and preserve the latest approved decisions. Explicit user instructions and the project brief take priority over these defaults.

## Work from the current project

Inspect the supplied footage, `sources/`, `assets/`, `references/`, any `brief.md`, applicable `AGENTS.md` or `CLAUDE.md` instructions, and prior approved edits. Work with the user's existing structure rather than reorganizing it unnecessarily. Choose suitable tools yourself; do not require the user to name libraries or assume software is installed — check and install dependencies as described below.

Separate reusable workflow from project identity. Use the current project's logo, fonts, references, and audience. Do not bring another project's footage, brand assets, or claims into a new project without instructions.

## Check and install dependencies

> [!IMPORTANT]
> Before editing, confirm that every tool and library the task needs is available. Typical requirements:
>
> - `ffmpeg` and `ffprobe` (cutting, cropping, audio cleanup, export, and the bundled checker)
> - `python3` (3.9+) for the bundled scripts and any helper scripts
> - A speech-to-text tool for transcription and subtitles, e.g. `faster-whisper` or `openai-whisper`
> - Python libraries for any advanced step you choose, e.g. `numpy`, `opencv-python`, `mediapipe` (face tracking, punch-ins, title-behind-head masks)

Check with commands such as `ffmpeg -version`, `ffprobe -version`, `python3 --version`, and `python3 -c "import faster_whisper"`.

> [!WARNING]
> If anything is missing, install it instead of stopping or silently skipping the step:
>
> 1. Python packages: create or reuse a project-local virtual environment and install there — `python3 -m venv .venv && .venv/bin/pip install <package>` — then run scripts with `.venv/bin/python`. Do not install into the system Python.
> 2. System tools: use the platform package manager — `sudo pacman -S ffmpeg` (Arch), `sudo apt install ffmpeg` (Debian/Ubuntu), `brew install ffmpeg` (macOS), `winget install ffmpeg` (Windows).
> 3. Tell the user what you are installing and why. If an install needs `sudo`/administrator rights you cannot provide, or it fails, show the exact command and ask the user to run it, then continue once it is available.
> 4. Re-run the check to verify the install before continuing with the edit.

## Match the requested scope

## WORKFLOW MODES AND ACTIONS
The video editing process is modular. Always identify the user's primary goal to determine which workflow module to initiate.

### 🎬 MODE: STORYBOARDING & PLANNING (Initial Pass)
Use this mode when generating a full narrative plan from raw footage.
**Goal:** Produce a comprehensive, structured proposal for review and approval.
**Inputs Required:** Source Footage (`sources/`), Project Brief (`brief.md`).
**Process:**
1.  Perform initial analysis including full transcription of source footage.
2.  Generate a detailed storyboard proposal (including timestamps, suggested crops, draft subtitle timing) covering the entire narrative flow.
3.  Present this structured plan to the user for explicit approval, editing, or feedback *before* any rendering occurs.

### ✂️ MODE: CROP_ONLY (Direct Edit)
Use this mode when structural changes are explicitly unwanted; only selective cropping is needed.
**Goal:** Execute targeted video cropping based on precise time codes and visual instructions.
**Inputs Required:** Source Footage, Specific Time Range/Coordinates (e.g., "10:00 to 10:30").
**Process:**
1.  Validate the request for structural changes (if none are mentioned, assume only a crop).
2.  Execute targeted video cropping directly using provided time codes and coordinates without generating any storyboard or requiring narrative sign-off.

### 📝 MODE: SUBTITLE_GENERATION (Standalone)
Use this mode when the goal is purely to generate synchronized subtitle files.
**Goal:** Produce accurate subtitle data for a given segment of footage.
**Inputs Required:** Source Footage, Time Range, Desired Language.
**Process:**
1.  Transcribe and time-sync the speech within the specified time range.
2.  Generate industry-standard subtitle formats (e.g., SRT) ready for export alongside the final video.

### 🚀 MODE: FINAL_EDIT (Full Production)
Use this mode when all assets, plans, and revisions are approved, or a full edit is requested.
**Goal:** Produce the finished, polished video file.
**Process:**
1.  (If not already done) Finalize the storyboard and get final user sign-off.
2.  Apply the personal style defaults (Vertical framing, captions, etc.).
3.  Execute all necessary edits (cuts, sound mixing, graphics).
4.  Export a new version of the video file.

**Always check:** Before finalizing any edit or export, always provide a detailed summary of what was changed from previous versions.

## Apply the personal style defaults

Use comfortable vertical framing, selective punch-ins, short accurate phrase captions, natural cleaned speech, a readable oversized opening title, and a supplied signature at bottom right. A title behind the head is a preferred effect when footage and references support a clean moving mask. Let the project references guide the specific treatment. Be creative when assets are absent while keeping explanations accurate and visual choices coherent.

The detailed rules define storyboard fields, sound treatment, asset use, title masks, caption timing, delivery, and verification. Keep originals intact and retain reproducible edit records.

## Verify the delivered file

For default 1080 × 1920 exports, run the bundled technical checker with its absolute path:

```bash
python /path/to/video-editing/scripts/check-video-export.py /path/to/finished-reel.mp4
```

The checker requires `ffprobe` and `ffmpeg`, checks display geometry across all decoded frames, compares audio/video durations, and decodes the export. It reads the file without changing it. Use `--width` and `--height` for another requested output size.

Technical checks complement playback review; they cannot assess composition, title-mask edges, cut quality, caption accuracy, or how the voice sounds. Inspect those separately and report any unavailable review capability honestly. Deliver clear links to the latest versions and the subtitle files without publishing externally unless requested.
