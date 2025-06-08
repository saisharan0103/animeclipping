"""Command line interface for clip_maker."""

import argparse
from pathlib import Path
from typing import Iterable
from moviepy.editor import VideoFileClip

from . import config, processing, overlay, utils


def process_file(video_path: Path, output_folder: Path, title: str, episode: str, clip_length: int, width: int, height: int) -> None:
    """Process a single video file through conversion, caption, and splitting."""
    temp_output = output_folder / f"{video_path.stem}_vertical.mp4"

    # Convert to vertical format
    converted = processing.convert_to_vertical(str(video_path), str(temp_output), width, height)

    # Load converted clip to add captions
    clip = VideoFileClip(str(converted))
    captioned = overlay.add_captions(clip, title, episode, width, height)

    captioned_output = output_folder / f"{video_path.stem}_captioned.mp4"
    captioned.write_videofile(str(captioned_output))

    # Split captioned video into clips
    processing.split_video(str(captioned_output), str(output_folder), clip_length)


def run_cli(args: Iterable[str]) -> None:
    parser = argparse.ArgumentParser(description="Create vertical cartoon clips for social media")
    parser.add_argument("--input", default="./input", help="Path to input folder")
    parser.add_argument("--output", default="./output", help="Path to output folder")
    parser.add_argument("--title", required=True, help="Title text for the top caption")
    parser.add_argument("--episode", required=True, help="Episode text for the bottom caption")
    parser.add_argument("--clip-length", type=int, default=config.CLIP_LENGTH, help="Length of each clip in seconds")
    parser.add_argument("--width", type=int, default=config.WIDTH, help="Output video width")
    parser.add_argument("--height", type=int, default=config.HEIGHT, help="Output video height")

    parsed = parser.parse_args(args)

    input_folder = utils.ensure_folder(parsed.input)
    output_folder = utils.ensure_folder(parsed.output)

    videos = utils.scan_input_folder(str(input_folder))
    if not videos:
        print("No MP4 files found in input folder.")
        return

    for video in videos:
        print(f"Processing {video.name}...")
        process_file(video, output_folder, parsed.title, parsed.episode, parsed.clip_length, parsed.width, parsed.height)
        print(f"Finished {video.name}")


if __name__ == "__main__":
    run_cli(None)
