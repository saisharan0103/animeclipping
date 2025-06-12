"""Preset configurations for clip_maker."""

from typing import Dict

PRESETS: Dict[str, Dict] = {
    "raw": {
        "clip_length": 30,
        "overlay_style": "basic",
    },
    "viral": {
        "clip_length": 20,
        "overlay_style": "bold",
    },
    "chill": {
        "clip_length": 30,
        "overlay_style": "fade",
    },
}


def load_preset(name: str) -> Dict:
    """Return configuration dictionary for the given preset name."""
    return PRESETS.get(name, PRESETS["raw"])
