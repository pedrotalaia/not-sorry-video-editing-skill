#!/usr/bin/env python3
"""Link this shared video-editing skill into Codex and Claude Code discovery."""

import argparse
from pathlib import Path
import sys


def install(label: str, skills_dir: Path, source: Path) -> bool:
    # Codex already discovers this folder when it lives directly in ~/.agents/skills.
    if source.parent == skills_dir.resolve():
        print(f"{label}: already available at {source}")
        return True

    destination = skills_dir / "video-editing"
    if destination.exists() or destination.is_symlink():
        if destination.resolve() == source:
            print(f"{label}: already linked at {destination}")
            return True
        print(f"{label}: refusing to replace existing {destination}", file=sys.stderr)
        return False

    try:
        skills_dir.mkdir(parents=True, exist_ok=True)
        destination.symlink_to(source, target_is_directory=True)
    except OSError as error:
        print(f"{label}: cannot install {destination}: {error}", file=sys.stderr)
        return False

    print(f"{label}: installed {destination} -> {source}")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--home", type=Path, default=Path.home(),
        help="User home containing .agents and .claude (default: current user's home)",
    )
    args = parser.parse_args()
    source = Path(__file__).resolve().parent.parent
    if not (source / "SKILL.md").is_file():
        parser.error(f"Missing SKILL.md in {source}")

    install_home = args.home.expanduser().resolve()
    results = [
        install("Codex", install_home / ".agents" / "skills", source),
        install("Claude Code", install_home / ".claude" / "skills", source),
    ]
    if all(results):
        print("Ready: use $video-editing in Codex or /video-editing in Claude Code.")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
