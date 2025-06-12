"""Subtitle generation and handling module."""

from typing import Optional
from moviepy.editor import VideoFileClip


def transcribe_audio(video_path: str, model: str = "base") -> str:
    """Transcribe audio using Whisper and return subtitle file path.

    Parameters
    ----------
    video_path : str
        Path to the input video.
    model : str
        Whisper model size.

    Returns
    -------
    str
        Path to the generated subtitle file.
    """
    # TODO: invoke Whisper to create subtitles
    return ""


def burn_in_subtitles(video_clip: VideoFileClip, subtitle_path: str) -> VideoFileClip:
    """Burn subtitles into a video clip.

    Parameters
    ----------
    video_clip : VideoFileClip
        Clip to apply subtitles to.
    subtitle_path : str
        Path to the subtitle file (.srt or .txt).

    Returns
    -------
    VideoFileClip
        Video with subtitles burned in.
    """
    # TODO: overlay subtitles using MoviePy
    return video_clip
