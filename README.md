# Motion Extraction


## Overview

Motion Extraction is a Python script that automates the process of applying a visual trick to highlight motions in a video. The technique is based on the principles outlined in the [YouTube video](https://www.youtube.com/watch?v=NSS6yAMZF78).

The script utilizes the MoviePy library for video editing and Pytube for downloading YouTube videos. It applies an inverted color effect and selectively freezes frames to emphasize motion in the video.

## Features

- **YouTube Video Support**: Download and process YouTube videos easily.
- **Custom Clipping**: Specify start and end times to process only a portion of the video.
- **Freeze Effect**: Apply a freeze effect to highlight motion, with customizable freeze duration.
- **Audio Options**: Choose whether to include audio in the output video.
- **Frame Rate Control**: Adjust the frames per second (fps) for the output video.
- **Multi-threading**: Utilize multiple threads for faster video processing.

## Requirements

- Python 3.x
- MoviePy
- Pytube

## Installation

```bash
pip install moviepy pytube
```

## Usage

```bash
python motion_extraction.py (--youtube <video_url> | --file <video_path>) [--clipStart <start_time>] [--clipEnd <end_time>] [--output <output_path>] [--freeze <freeze_delay>] [--audio] [--fps <frames_per_second>] [--threads <num_threads>]
```

### Options

- `--youtube` or `-y`: URL of the YouTube video.
- `--file` or `-f`: Path to the video file.
- `--clipStart` or `-s`: Subclip start time.
- `--clipEnd` or `-e`: Subclip end time.
- `--output` or `-o`: Path to the output file.
- `--freeze` or `-fd`: Freeze delay (-1 for the entire clip).
- `--audio` or `-na`: Keep audio (optional).
- `--fps`: Frames per second (optional, default is 24).
- `--threads` or `-th`: Number of threads for video processing (optional, default is 4).

## Example

```bash
python motion_extraction.py --youtube https://www.youtube.com/watch?v=example_video_url --clipStart 2 --clipEnd 8 --output output_video.mp4 --freeze 1 --audio --fps 30 --threads 8
```

This example downloads a YouTube video, processes a subclip from 30 seconds to 1 minute 30 seconds, adds a freeze effect with a 1-second delay, includes audio, sets the output video's frame rate to 30 fps, and utilizes 8 threads for processing.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Inspiration: [Link to the YouTube video](https://www.youtube.com/watch?v=NSS6yAMZF78)
