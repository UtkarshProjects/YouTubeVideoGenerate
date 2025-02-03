from moviepy import VideoFileClip

class VideoClipper:
    def __init__(self):
        pass

    def create_clip(self, video_path, duration, resolution):
        try:
            # video = VideoFileClip(video_path).subclip(0, duration)
            # target_width, target_height = resolution

            # Calculate the new height to maintain the 9:16 aspect ratio
            # new_height = int(target_width * 16 / 9)

            video = VideoFileClip(video_path)
            clip = video.subclipped(0, duration)
            clip = clip.resized(resolution)
            output_path = f"clip_{duration}_{resolution[0]}x{resolution[1]}.mp4"
            clip.write_videofile(output_path, codec='libx264')
            video.close()
            return clip

            # Resize and crop the video to the target resolution with 9:16 aspect ratio
            # video = video.resize(height=new_height).crop(width=target_width, height=target_height, x_center=video.w / 2, y_center=video.h / 2)

            # return video
        except Exception as e:
            print(f"Error processing video: {e}")
            return None
        
    # def create_clip(self, video_path, duration, resolution):
    #     from moviepy import VideoFileClip

    #     video = VideoFileClip(video_path)
    #     clip = video.subclipped(0, duration)
    #     clip = clip.resized(resolution)
    #     output_path = f"clip_{duration}_{resolution[0]}x{resolution[1]}.mp4"
    #     clip.write_videofile(output_path, codec='libx264')
    #     video.close()
    #     return output_path