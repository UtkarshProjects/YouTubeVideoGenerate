# src/main.py

import os
from video_processing.clipper import VideoClipper
from video_processing.animator import VideoAnimator
from utils.helpers import load_video, save_video

def main():
    video_path = input("Enter the path to the video file: ")
    
    if not os.path.exists(video_path):
        print("The specified video file does not exist.")
        return

    duration = 60  # duration in seconds
    resolutions = [(1080, 1920)]  # different resolutions
    # resolutions = [(1920, 1080), (1280, 720), (640, 360)]  # different resolutions

    clipper = VideoClipper()
    animator = VideoAnimator()

    for resolution in resolutions:
        clip = clipper.create_clip(video_path, duration, resolution)
        if clip is None:
            print(f"Failed to create video clip for resolution {resolution}.")
            continue
        print(f"Clip is {clip} and type is {type(clip)}")
        animated_clip = animator.animate(clip)
        if animated_clip is None:
            print(f"Failed to animate video clip for resolution {resolution}.")
            continue        
        output_path = f"output/animated_clip_{resolution[0]}x{resolution[1]}.mp4"
        save_video(animated_clip, output_path)
        print(f"Saved animated clip at {output_path}")

if __name__ == "__main__":
    main()