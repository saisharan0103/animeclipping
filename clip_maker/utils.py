"""Utility helpers for clip_maker."""

from pathlib import Path
from typing import List, Dict
import json


def ensure_folder(path: str) -> Path:
    """Ensure that a folder exists and return the Path object."""
    folder = Path(path)
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def scan_input_folder(folder: str) -> List[Path]:
    """Return a list of MP4 files in the given folder."""
    path = Path(folder)
    return sorted(path.glob("*.mp4"))


def load_cache(cache_file: str) -> Dict[str, str]:
    """Load cache of processed videos from JSON file."""
    path = Path(cache_file)
    if path.exists():
        with path.open("r") as f:
            return json.load(f)
    return {}


def save_cache(cache: Dict[str, str], cache_file: str) -> None:
    """Save cache dictionary to disk."""
    path = Path(cache_file)
    with path.open("w") as f:
        json.dump(cache, f)


def is_processed(cache: Dict[str, str], video_path: str) -> bool:
    """Check if a video has been processed already."""
    return video_path in cache


def mark_processed(cache: Dict[str, str], video_path: str, output: str) -> None:
    """Mark a video as processed in the cache."""
    cache[video_path] = output
