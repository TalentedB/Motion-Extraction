from moviepy.editor import *
import moviepy.video.fx.all as vfx
import copy
from time import sleep
import os
from pytube import YouTube
import argparse

def motionExtraction(clip_path = None, clipping = None, output_path = "output_video.mp4", freeze_delay = 1, audio = False, fps = 24, threads = 4):
    clip = VideoFileClip(clip_path)

    if clipping:
        clip = clip.subclip(clipping[0], clipping[1])

    inverted_clip = clip
    inverted_clip = inverted_clip.fx(vfx.invert_colors)

    # if freeze_delay is -1, then freeze the entire clip
    if freeze_delay == -1:
        inverted_clip = inverted_clip.fx(vfx.freeze, freeze_duration=clip.duration)
    else:
        inverted_clip = inverted_clip.fx(vfx.freeze, freeze_duration=freeze_delay)

    inverted_clip = inverted_clip.set_opacity(0.5)

    final = CompositeVideoClip([clip, inverted_clip])

    final = final.subclip(0, clip.duration)


    final.write_videofile(output_path, remove_temp=True, fps=fps, threads=threads, audio=audio)


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


def main():
    parser = argparse.ArgumentParser(description='Motion Extraction Script')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--youtube', '-y', metavar='<video_url>', type=str, help='URL of the YouTube video')
    group.add_argument('--file', '-f', metavar='<video_path>', type=str, help='Path to the video file')
    parser.add_argument('--clipStart', '-s', metavar='<clip_start>', type=str, help='Subclip start time')
    parser.add_argument('--clipEnd', '-e', metavar='<clip_end>', type=str, help='Subclip end time')
    parser.add_argument('--output', '-o', metavar='<output_path>', type=str, help='Path to the output file')
    parser.add_argument('--freeze', '-fd', metavar='<freeze_delay>', type=float, help='Freeze delay (-1 for entire clip))')
    parser.add_argument('--audio', '-na', metavar='<keep_audio>', help='Keep audio')
    parser.add_argument('--fps', '-fps', metavar='<fps>', type=int, help='Frames per second')
    parser.add_argument('--threads', '-th', metavar='<threads>', type=int, help='Number of threads for video processing')

    args = parser.parse_args()

    clipping = None
    if args.clipStart or args.clipEnd:
        clipping = [args.clipStart, args.clipEnd]

    if args.youtube:	
        # Process YouTube video URL
        Download(link=args.youtube)

        motionExtraction(clip_path="temp/tempvideo.mp4", clipping=clipping, output_path=args.output, freeze_delay=args.freeze, audio=args.audio, fps=args.fps, threads=args.threads)
        os.remove("temp/tempvideo.mp4")

    elif args.file:
        # Process Video file path
        motionExtraction(clip_path=args.file, clipping=clipping, output_path=args.output, freeze_delay=args.freeze, audio=args.audio, fps=args.fps, threads=args.threads)
    else:
        # ? Invalid arguments passed and or missing arguemnts
        print('Invalid arguments')
        exit(1)

		



if __name__ == '__main__':
	main()














