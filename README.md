# Cartoon Clipper System

`clip_maker` is a small command line program that turns widescreen cartoons or anime episodes into vertical clips for TikTok, Instagram Reels and other short‑video apps.

## Requirements

* Python 3.8 or newer
* `ffmpeg` installed on your system and available in the PATH

## Installation

1. Download or clone this repository.
2. Open a terminal (Command Prompt on Windows or the Terminal app on macOS/Linux).
3. Run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

## Preparing your videos

1. Put the `.mp4` files you want to clip in the `input` folder. You can create the folder if it does not exist.
2. Choose the text you want to appear at the top (`title`) and bottom (`episode`).

## Running the program

Execute this command from the project folder:

```bash
python -m clip_maker.cli \
    --input ./input \
    --output ./output \
    --title "Ben 10" \
    --episode "S1E01" \
    --clip-length 30
```

* `--input` is the folder with your source videos.
* `--output` is where the short clips will be written.
* `--title` shows at the top of every clip.
* `--episode` shows at the bottom of every clip.
* `--clip-length` sets how long each short clip will be in seconds (default 30).
* `--width` and `--height` can be used to change the output resolution if needed (default 1080x1920).

When the command finishes, open the `output` folder to see your new vertical clips.

## Example

If your videos are already in the `input` folder and you are happy with the defaults, this short command will work:

```bash
python -m clip_maker.cli --title "Ben 10" --episode "S1E01"
```

This tool is designed to be simple, so even a beginner can run it after following these steps. Enjoy making your own cartoon clips!
