[English Documentation](README.md)

# 视频转图像工具

一个简单高效的 Python 视频帧提取工具。

## 功能特点

- 按指定间隔提取视频帧
- 支持多种视频格式（mp4、avi、mov、mkv）
- 支持批量处理多个视频
- 为每个视频创建独立的输出文件夹，结构清晰

## 环境要求

- Python 3.x
- OpenCV (cv2)
- pathlib

## 安装

```bash
pip install opencv-python
```

## 使用方法

1. 将视频文件放入 `video` 目录
2. 运行脚本：
```bash
python video_to_frames.py
```
3. 提取的图片帧将保存在 `frames` 目录中

## 配置参数

你可以在脚本中修改以下参数：
- `frame_interval`：跳帧间隔（默认：10）
- `video_directory`：输入视频目录（默认："video"）
- `output_directory`：输出图片目录（默认："frames"）

## 支持的视频格式

- .mp4
- .avi
- .mov
- .mkv

## 许可证

MIT 许可证

---