import cv2
import os
from pathlib import Path

def extract_frames(video_path, output_dir, frame_interval=10):
    # Create output directory
    video_name = Path(video_path).stem
    frames_dir = Path(output_dir) / video_name
    frames_dir.mkdir(parents=True, exist_ok=True)
    
    # Open video
    cap = cv2.VideoCapture(str(video_path))
    frame_count = 0
    saved_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        # Save image every 10 frames
        if frame_count % frame_interval == 0:
            output_path = frames_dir / f"frame_{saved_count:04d}.jpg"
            cv2.imwrite(str(output_path), frame)
            saved_count += 1
            
        frame_count += 1
    
    cap.release()
    return saved_count

def process_video_directory(video_dir, output_dir):
    video_dir = Path(video_dir)
    output_dir = Path(output_dir)
    
    # Supported video formats
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv')
    
    for video_file in video_dir.glob('*'):
        if video_file.suffix.lower() in video_extensions:
            print(f"Processing video: {video_file.name}")
            frames_saved = extract_frames(video_file, output_dir)
            print(f"Saved {frames_saved} frames")

if __name__ == "__main__":
    video_directory = "video"  # Directory containing videos
    output_directory = "frames"  # Directory for output frames
    
    process_video_directory(video_directory, output_directory) 