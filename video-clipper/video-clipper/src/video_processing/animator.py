import cv2
import numpy as np
from moviepy import VideoFileClip

class VideoAnimator:
    def __init__(self):
        pass

    def cartoonize_frame(self, frame):
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Apply median blur
        gray = cv2.medianBlur(gray, 5)
        # Detect edges
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        # Apply bilateral filter to smoothen the image
        color = cv2.bilateralFilter(frame, 9, 300, 300)
        # Combine edges and color
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return cartoon

    def animate(self, video):
        try:
            def process_frame(frame):
                return self.cartoonize_frame(frame)

            # video = VideoFileClip(video_path)

            # animated_video = video.fl(lambda gf, t: add_filter(gf(t)))
            animated_video = video.fl(process_frame)
            # animated_video = video.fl_image(process_frame)
            return animated_video
        except Exception as e:
            print(f"Error animating video: {e}")
            return None