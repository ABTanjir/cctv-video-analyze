# Motion Frame Extractor

This Python script processes video files in a specified folder and extracts frames where motion is detected, saving them as image files. It uses OpenCV for motion detection and basic image processing techniques to filter noise.

## 📁 Folder Structure

```
.
├── videos/             # Input folder with video files
├── motion_frames/      # Output folder where motion frames will be saved
├── script.py           # Motion detection script
└── README.md           # This file
```

## 🚀 Features

- Detects motion between frames using frame differencing and contour analysis.
- Skips frames to optimize performance (`FRAME_SKIP`).
- Resizes frames to reduce noise and improve performance.
- Filters small movements using `MIN_AREA`.
- Saves full original frames with detected motion.

## 🧠 How It Works

1. Compares consecutive frames using `cv2.absdiff()`.
2. Converts to grayscale, blurs the image, and applies thresholding.
3. Uses morphological operations to clean up the image.
4. Finds contours and filters by area.
5. Saves frames where significant motion is detected.

## 🛠 Configuration

You can customize the script by modifying the constants at the top of the script:

```python
VIDEO_FOLDER = 'videos'         # Folder containing input videos
OUTPUT_FOLDER = 'motion_frames' # Folder to save frames with motion
MIN_AREA = 1100                 # Minimum contour area to count as motion
FRAME_SKIP = 1                  # Number of frames to skip (higher = faster, less accurate)
RESIZE_WIDTH = 640              # Resize frame width (helps reduce noise)
```

## 📦 Requirements

- Python 3.x
- OpenCV (`cv2`)

Install dependencies:

```bash
pip install opencv-python
```

## 🧪 Usage

1. Place your `.mp4`, `.avi`, `.mov`, or `.mkv` files in the `videos/` directory.
2. Run the script:

```bash
python script.py
```

3. Motion frames will be saved in the `motion_frames/` directory.

## ✅ Supported Formats

- `.mp4`
- `.avi`
- `.mov`
- `.mkv`

## 📄 Output Example

Saved files will be named using the format:

```
<video_name>_motion_<index>.jpg
```

Example:

```
sample_video_motion_0002.jpg
```

## 📬 Contributions

Feel free to contribute improvements or report issues!

---

**Author:** _[Your Name]_  
**License:** MIT
