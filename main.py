from moviepy.editor import *
import moviepy.video.fx.all as vfx
import copy

clip = VideoFileClip("video.mp4")

clip = clip.subclip(20, 40)

inverted_clip = clip
inverted_clip = inverted_clip.fx(vfx.invert_colors)
inverted_clip = inverted_clip.fx(vfx.freeze, freeze_duration=1)
inverted_clip = inverted_clip.set_opacity(0.5)

clip = CompositeVideoClip([clip, inverted_clip])
# showing clip
clip.ipython_display(width = 280)