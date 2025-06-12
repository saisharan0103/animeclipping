"""Simple plugin management for optional features."""

from typing import Callable, Dict, List

# Placeholder registration system
_PLUGINS: Dict[str, Callable] = {}


def register(name: str, func: Callable) -> None:
    """Register a processing plugin by name."""
    _PLUGINS[name] = func


def get(name: str) -> Callable:
    """Retrieve a plugin by name."""
    return _PLUGINS[name]


def available() -> List[str]:
    """Return a list of registered plugin names."""
    return list(_PLUGINS.keys())
