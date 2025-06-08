# ==========================================================
# 📦 PROJECT OVERVIEW — Cartoon Clipper System
# ==========================================================
You are building a CLI-based video processing tool called `clip_maker` to automate the process of clipping 16:9 cartoon/anime episodes into 9:16 short-form videos for Instagram Reels, YouTube Shorts, and TikTok.

The app should:
1. Read 16:9 landscape videos from ./input/
2. Convert to 9:16 (1080x1920) format by:
   - Creating a black background canvas
   - Resizing video to fit width 1080
   - Centering the video vertically
3. Add static text:
   - TOP: show title (e.g., "Ben 10")
   - BOTTOM: episode label (e.g., "S1E01")
4. Split the processed video into 30-second clips (or configurable duration)
5. Export clips to ./output/

You will now:
- Create the full project structure with correct Python modules
- Implement the CLI (argparse-based) and stubs for all core logic
- Follow best practices: clean imports, modular code, default config, clear comments

# ==========================================================
# 🧱 PROJECT STRUCTURE (CREATE THIS)
# ==========================================================
cartoon_clipper/
├── input/                   # Folder for input MP4s
├── output/                  # Folder for final clips
├── clip_maker/
│   ├── __init__.py
│   ├── config.py            # Store default values like clip length, dimensions
│   ├── processing.py        # Video formatting and clip-splitting logic
│   ├── overlay.py           # Caption rendering functions
│   ├── cli.py               # argparse entry point
│   └── utils.py             # Path setup, logging helpers
├── requirements.txt         # Libraries like moviepy, ffmpeg-python, tqdm
├── README.md
└── setup.py                 # Optional pip-install config

# ==========================================================
# 🧠 FUNCTIONAL REQUIREMENTS
# ==========================================================

### CLI (clip_maker/cli.py)
- Use argparse to parse:
  --input        : path to input folder
  --output       : path to output folder
  --title        : string for top caption
  --episode      : string for bottom caption
  --clip-length  : int (in seconds)
  --width        : default 1080
  --height       : default 1920

- CLI should:
  1. Load all .mp4 files from input folder
  2. Pass them through the convert → overlay → split pipeline
  3. Print clear logs, no GUI

### Processing (clip_maker/processing.py)
- Function: `convert_to_vertical(video_path, output_path, width, height)`
- Function: `split_video(path_to_video, output_folder, clip_duration)`

### Overlay (clip_maker/overlay.py)
- Function: `add_captions(video_clip, title, episode, width, height)`
- Use TextClip from moviepy to overlay top & bottom text

### Config (clip_maker/config.py)
- Store default WIDTH = 1080, HEIGHT = 1920, CLIP_LENGTH = 30

### Utils (clip_maker/utils.py)
- Helper: scan_input_folder(folder) → returns list of .mp4 files
- Create folders if not exist

### README.md
Include:
- How to install dependencies
- How to run CLI
- Example command

### requirements.txt
Include:
- moviepy
- ffmpeg-python
- tqdm

# ==========================================================
# ✅ OUTPUT EXPECTATION
# ==========================================================
Generate all necessary files in one go — correctly structured.
Implement full `cli.py` with working argparse logic.
All other modules can have function stubs with docstrings + `pass` or `TODO` markers.

Do NOT include subtitle generation.
Do NOT include GUI.
Do NOT use Jupyter or notebook format — this is a standalone CLI tool.
