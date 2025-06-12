"""Command line interface for clip_maker."""

import argparse
from pathlib import Path
from typing import Iterable, List, Dict

from moviepy.editor import VideoFileClip

from . import (
    config,
    processing,
    overlay,
    utils,
    smart_clip,
    subtitle,
    presets,
    metadata,
)


def process_file(video_path: Path, output_folder: Path, options: argparse.Namespace) -> List[Dict]:
    """Process a single video file through conversion and plugins.

    Returns a list of metadata entries for each produced clip.
    """

    temp_output = output_folder / f"{video_path.stem}_vertical.mp4"

    # Convert to vertical format
    converted = processing.convert_to_vertical(
        str(video_path), str(temp_output), options.width, options.height
    )

    current_clip = VideoFileClip(str(converted))

    if options.use_subs:
        # TODO: generate subtitles using Whisper and optionally burn them in
        subtitle_path = subtitle.transcribe_audio(str(video_path))
        current_clip = subtitle.burn_in_subtitles(current_clip, subtitle_path)

    captioned = overlay.add_captions(
        current_clip, options.title, options.episode, options.width, options.height
    )

    captioned_output = output_folder / f"{video_path.stem}_captioned.mp4"
    captioned.write_videofile(str(captioned_output))

    clips_meta: List[Dict] = []
    if options.smart != "none":
        clips_meta = smart_clip.split_smart(
            str(captioned_output), str(output_folder), options.smart, options.clip_length
        )
    else:
        processing.split_video(
            str(captioned_output), str(output_folder), options.clip_length
        )
    # TODO: collect metadata for each produced clip
    return clips_meta


def run_cli(args: Iterable[str]) -> None:
    parser = argparse.ArgumentParser(
        description="Create vertical cartoon clips for social media"
    )
    parser.add_argument("--input", default="./input", help="Path to input folder")
    parser.add_argument("--output", default="./output", help="Path to output folder")
    parser.add_argument("--title", required=True, help="Title text for the top caption")
    parser.add_argument("--episode", required=True, help="Episode text for the bottom caption")
    parser.add_argument(
        "--clip-length",
        type=int,
        default=config.CLIP_LENGTH,
        help="Length of each clip in seconds",
    )
    parser.add_argument("--width", type=int, default=config.WIDTH, help="Output video width")
    parser.add_argument("--height", type=int, default=config.HEIGHT, help="Output video height")
    parser.add_argument(
        "--preset",
        default="raw",
        help="Preset configuration profile name",
    )
    parser.add_argument(
        "--use-subs",
        action="store_true",
        help="Generate and burn-in subtitles using Whisper",
    )
    parser.add_argument(
        "--smart",
        choices=["scene", "audio", "speech", "none"],
        default="none",
        help="Smart clipping method",
    )
    parser.add_argument(
        "--export-csv",
        action="store_true",
        help="Export metadata CSV for scheduling",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reprocess even if video was processed before",
    )

    parsed = parser.parse_args(args)

    preset_conf = presets.load_preset(parsed.preset)

    # Override defaults from preset when values are not explicitly provided
    if "clip_length" in preset_conf and parsed.clip_length == config.CLIP_LENGTH:
        parsed.clip_length = preset_conf["clip_length"]

    input_folder = utils.ensure_folder(parsed.input)
    output_folder = utils.ensure_folder(parsed.output)

    cache_file = output_folder / "cache.json"
    cache = utils.load_cache(str(cache_file))

    videos = utils.scan_input_folder(str(input_folder))
    if not videos:
        print("No MP4 files found in input folder.")
        return

    all_meta: List[Dict] = []
    for video in videos:
        if not parsed.force and utils.is_processed(cache, str(video)):
            print(f"Skipping {video.name}, already processed")
            continue

        print(f"Processing {video.name}...")
        meta = process_file(video, output_folder, parsed)
        all_meta.extend(meta)
        utils.mark_processed(cache, str(video), video.name)
        print(f"Finished {video.name}")

    utils.save_cache(cache, str(cache_file))

    if parsed.export_csv:
        metadata.write_metadata_csv(all_meta, str(output_folder))


if __name__ == "__main__":
    run_cli(None)
