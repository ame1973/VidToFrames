[中文文档](README_CN.md)

# VideoFramer

A lightweight and efficient tool for extracting frames from video files. VideoFramer allows you to easily convert videos into sequential image frames with customizable settings.

## Key Features
- Extract frames from various video formats (MP4, AVI, MOV, etc.)
- Adjustable frame extraction rate
- Batch processing support
- Customizable output formats (JPG, PNG)
- Simple command-line interface
- Cross-platform compatibility (Windows, macOS, Linux)

## Use Cases
- Video analysis
- Machine learning dataset preparation
- Animation reference
- Thumbnail generation
- Motion study

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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---