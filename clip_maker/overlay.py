"""Functions for adding text overlays to videos."""

from moviepy.editor import TextClip, CompositeVideoClip, VideoFileClip


def add_captions(video_clip: VideoFileClip, title: str, episode: str, width: int, height: int) -> CompositeVideoClip:
    """Add top and bottom captions to a video clip.

    Parameters
    ----------
    video_clip : VideoFileClip
        Clip to add captions to.
    title : str
        Text to display at the top.
    episode : str
        Text to display at the bottom.
    width : int
        Width of the final video.
    height : int
        Height of the final video.

    Returns
    -------
    CompositeVideoClip
        Video clip with captions overlaid.
    """
    # TODO: implement caption overlay using moviepy
    return video_clip
