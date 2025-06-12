# Cartoon Clipper System

`clip_maker` is a command line tool for converting widescreen cartoon or anime episodes into vertical clips for social media.

Key features include optional subtitle generation, viral caption presets, smart scene detection, metadata export, and a simple caching mechanism.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m clip_maker.cli \
    --input ./input \
    --output ./output \
    --title "Ben 10" \
    --episode "S1E01" \
    --preset viral \
    --use-subs \
    --smart scene \
    --export-csv
```

The command above processes all `.mp4` files in `./input`, converts them to vertical format with captions, optionally generates subtitles, splits the result into smart clips, and writes them to `./output` along with a `metadata.csv` file.
