def load_video(video_path):
    from moviepy import VideoFileClip
    try:
        video = VideoFileClip(video_path)
        return video
    except Exception as e:
        print(f"Error loading video: {e}")
        return None

def save_video(video, output_path):
    if video is None:
        print("Error: No video to save.")
        return
    try:
        video.write_videofile(output_path, codec='libx264', audio_codec='aac')
    except Exception as e:
        print(f"Error saving video: {e}")