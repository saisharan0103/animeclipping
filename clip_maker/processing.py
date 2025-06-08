"""Video processing functions."""

from pathlib import Path
from moviepy.editor import VideoFileClip


def convert_to_vertical(video_path: str, output_path: str, width: int, height: int) -> Path:
    """Convert a widescreen video to a vertical format.

    Parameters
    ----------
    video_path : str
        Path to the input video.
    output_path : str
        Path where the converted video will be stored.
    width : int
        Target width of the vertical video.
    height : int
        Target height of the vertical video.

    Returns
    -------
    Path
        Path to the converted video.
    """
    # TODO: implement video conversion using moviepy
    return Path(output_path)


def split_video(path_to_video: str, output_folder: str, clip_duration: int) -> None:
    """Split a video into multiple clips of the given duration.

    Parameters
    ----------
    path_to_video : str
        Path to the video to split.
    output_folder : str
        Folder where the clips will be written.
    clip_duration : int
        Duration of each clip in seconds.
    """
    # TODO: implement splitting logic using moviepy
    pass
