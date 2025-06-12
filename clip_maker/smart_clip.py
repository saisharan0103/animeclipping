"""Smart clipping strategies for detecting scenes or audio events."""

from typing import List, Dict

# Placeholder types for scene time ranges
TimeRange = Dict[str, int]


def split_smart(video_path: str, output_folder: str, method: str, default_length: int) -> List[Dict]:
    """Split video using smart scene or audio detection.

    Parameters
    ----------
    video_path : str
        Path to the input video.
    output_folder : str
        Where to store the generated clips.
    method : str
        Strategy to use ("scene", "audio", "speech").
    default_length : int
        Fallback clip length when no detection is available.

    Returns
    -------
    List[Dict]
        Metadata for produced clips. Currently placeholder.
    """
    # TODO: implement scene or audio based clipping
    return []
