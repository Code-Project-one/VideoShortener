from moviepy.editor import VideoFileClip

def split_video_into_clips(video_path, clip_duration=60):
    video = VideoFileClip(video_path)
    audio = video.audio
    total_duration = video.duration

    clip_number = 1
    start_time = 0
    end_time = clip_duration

    while start_time < total_duration:
        clip = video.subclip(start_time, end_time)
        clip = clip.set_audio(audio)

        clip_filename = f"clip_{clip_number}.mp4"
        clip.write_videofile(clip_filename, codec="libx264", audio_codec="aac")

        print(f"Created {clip_filename}")

        start_time = end_time
        end_time += clip_duration
        clip_number += 1

    video.close()

# Example usage
video_path = "video.mp4"
split_video_into_clips(video_path, clip_duration=60)
