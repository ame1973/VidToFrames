[中文文档](README_CN.md)

# Video to Image Converter

A simple and efficient Python tool to extract frames from videos.

## Features

- Extract frames from videos at specified intervals
- Support multiple video formats (mp4, avi, mov, mkv)
- Batch processing for multiple videos
- Organized output structure with separate folders for each video

## Requirements

- Python 3.x
- OpenCV (cv2)
- pathlib

## Installation

```bash
pip install opencv-python
```

## Usage

1. Place your videos in the `video` directory
2. Run the script:
```bash
python video_to_frames.py
```
3. Extracted frames will be saved in the `frames` directory

## Configuration

You can modify these parameters in the script:
- `frame_interval`: Number of frames to skip (default: 10)
- `video_directory`: Input video directory (default: "video")
- `output_directory`: Output frames directory (default: "frames")

## Supported Video Formats

- .mp4
- .avi
- .mov
- .mkv

## License

MIT License

---