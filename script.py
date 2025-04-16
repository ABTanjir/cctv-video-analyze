import cv2
import os

VIDEO_FOLDER = 'videos'
OUTPUT_FOLDER = 'motion_frames'
MIN_AREA = 1100
FRAME_SKIP = 1
RESIZE_WIDTH = 640

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mov', '.mkv']

def is_video_file(filename):
    return any(filename.lower().endswith(ext) for ext in VIDEO_EXTENSIONS)

for video_file in os.listdir(VIDEO_FOLDER):
    if not is_video_file(video_file):
        continue

    video_path = os.path.join(VIDEO_FOLDER, video_file)
    cap = cv2.VideoCapture(video_path)

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    frame_idx = 0
    motion_idx = 0

    # Create subfolder for this video
    base_name = os.path.splitext(video_file)[0]
    video_output_folder = os.path.join(OUTPUT_FOLDER, base_name)
    os.makedirs(video_output_folder, exist_ok=True)

    print(f"Processing {video_file}...")

    while ret:
        frame1_resized = cv2.resize(frame1, (RESIZE_WIDTH, int(frame1.shape[0] * RESIZE_WIDTH / frame1.shape[1])))
        frame2_resized = cv2.resize(frame2, (RESIZE_WIDTH, int(frame2.shape[0] * RESIZE_WIDTH / frame2.shape[1])))

        diff = cv2.absdiff(frame1_resized, frame2_resized)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (7, 7), 0)

        _, thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        cleaned = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel)

        contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area >= MIN_AREA:
                print(f"Motion detected at frame({frame_idx}): area >> {area:.2f} pixels")
                output_name = f"motion_{motion_idx:04d}.jpg"
                output_path = os.path.join(video_output_folder, output_name)
                cv2.imwrite(output_path, frame1)
                motion_idx += 1
                break

        for _ in range(FRAME_SKIP):
            frame1 = frame2
            ret, frame2 = cap.read()
            frame_idx += 1
            if not ret:
                break

    cap.release()
    print(f"Finished {video_file}: {motion_idx} motion frames saved.\n")

print("All videos processed........")
