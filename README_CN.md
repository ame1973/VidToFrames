[English Documentation](README.md)

# VideoFramer

一个轻量级且高效的视频帧提取工具。VideoFramer 允许您轻松地将视频文件转换为连续的图像帧，并且支持自定义设置。

## 主要特性
- 支持多种视频格式（MP4、AVI、MOV 等）
- 可调节的帧提取率
- 支持批量处理
- 可自定义输出格式（JPG、PNG）
- 简单的命令行界面
- 跨平台兼容（Windows、macOS、Linux）

## 应用场景
- 视频分析
- 机器学习数据集准备
- 动画参考
- 缩略图生成
- 动作研究

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
3. 提取的帧将保存在 `frames` 目录中

## 配置

您可以在脚本中修改以下参数：
- `frame_interval`：跳过的帧数（默认：10）
- `video_directory`：输入视频目录（默认："video"）
- `output_directory`：输出帧目录（默认："frames"）

## 支持的视频格式

- .mp4
- .avi
- .mov
- .mkv

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---