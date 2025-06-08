# Cartoon Clipper System

`clip_maker` is a command line tool for converting widescreen cartoon or anime episodes into vertical clips for social media.

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
    --clip-length 30
```

The command above processes all `.mp4` files in `./input`, converts them to 9:16 format with captions, splits the result into 30‑second clips, and writes them to `./output`.
