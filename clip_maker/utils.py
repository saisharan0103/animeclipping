"""Utility helpers for clip_maker."""

from pathlib import Path
from typing import List


def ensure_folder(path: str) -> Path:
    """Ensure that a folder exists and return the Path object."""
    folder = Path(path)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def scan_input_folder(folder: str) -> List[Path]:
    """Return a list of MP4 files in the given folder."""
    path = Path(folder)
    return sorted(path.glob("*.mp4"))
