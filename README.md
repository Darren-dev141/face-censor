# Face Censor

Detects faces in a video file with OpenCV and censors them, with a small PyQt6 UI.

## How it works

- `main.py` loads a Haar cascade classifier (`faces.xml`), scans each frame of the input video, and draws filled rectangles over detected faces.
- The censored video is written to `output2.mkv`; press `q` during the preview window to stop early.

## Run

```bash
pip install -r requirements.txt
python main.py
```

Point `output()` at your own video file (update the filename in `btnclick()`).

## Stack

Python, OpenCV, PyQt6
