import moviepy as mp
import cv2
import numpy as np

def cartoonify(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 300, 300)
    
    data = np.float32(color).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(data, 8, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    centers = np.uint8(centers)
    quantized = centers[labels.flatten()]
    quantized = quantized.reshape(color.shape)
    
    cartoon = cv2.bitwise_and(quantized, quantized, mask=edges)
    return cartoon

def process_frame(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cartoon_frame = cartoonify(frame_rgb)
    return cv2.cvtColor(cartoon_frame, cv2.COLOR_RGB2BGR)

# Load the video
video = mp.VideoFileClip("E:\\Utkarsh\\YouTubeVideoGenerate\\video-clipper\\video-clipper\\clip_60_1080x1920.mp4")


# Get video properties
fps = video.fps
width, height = video.size

# Initialize VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video_out = cv2.VideoWriter('cartoon_video.mp4', fourcc, fps, (width, height))

# Process each frame
for frame in video.iter_frames():
    cartoon_frame = process_frame(frame)
    video_out.write(cartoon_frame)
    del cartoon_frame  # Release memory

video_out.release()
