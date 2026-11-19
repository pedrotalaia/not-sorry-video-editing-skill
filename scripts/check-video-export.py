#!/usr/bin/env python3
"""Read-only geometry, timing, and decode checks for a short-form video export."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('video', type=Path)
    parser.add_argument('--width', type=int, default=1080)
    parser.add_argument('--height', type=int, default=1920)
    args = parser.parse_args()
    errors = []
    if args.width <= 0 or args.height <= 0:
        parser.error('Expected dimensions must be positive.')
    if not args.video.is_file():
        parser.error(f'Video does not exist: {args.video}')
    for tool in ('ffprobe', 'ffmpeg'):
        if shutil.which(tool) is None:
            parser.error(f'{tool} is required but unavailable.')

    def probe(*extra):
        result = subprocess.run(['ffprobe', '-v', 'error', *extra, '-of', 'json',
                                 str(args.video.resolve())], check=True,
                                capture_output=True, text=True)
        return json.loads(result.stdout)

    try:
        metadata = probe('-show_streams', '-show_format')
        videos = [s for s in metadata['streams'] if s['codec_type'] == 'video']
        audios = [s for s in metadata['streams'] if s['codec_type'] == 'audio']
        if not videos:
            raise ValueError('No video stream found.')
        video = videos[0]
        expected_dar = Fraction(args.width, args.height)
        actual_dar = video.get('display_aspect_ratio', '')
        if (video.get('width'), video.get('height')) != (args.width, args.height):
            errors.append('Stored dimensions do not match the requested export size.')
        if video.get('sample_aspect_ratio') != '1:1':
            errors.append(f"Stream pixel aspect ratio is {video.get('sample_aspect_ratio')}; expected 1:1.")
        try:
            if Fraction(actual_dar.replace(':', '/')) != expected_dar:
                errors.append(f'Display aspect ratio is {actual_dar}; expected {expected_dar}.')
        except (ValueError, ZeroDivisionError):
            errors.append(f'Display aspect ratio is missing or invalid: {actual_dar}.')
        for item in video.get('side_data_list', []):
            if float(item.get('rotation', 0)) % 360:
                errors.append('The video contains nonzero rotation metadata; review orientation.')
        if float(video.get('tags', {}).get('rotate', 0)) % 360:
            errors.append('The video contains a nonzero rotate tag; review orientation.')

        frames = probe('-select_streams', 'v:0', '-show_frames', '-show_entries',
                       'frame=width,height,sample_aspect_ratio')['frames']
        if not frames:
            errors.append('No video frames could be inspected.')
        invalid = sum(f.get('sample_aspect_ratio') != '1:1' or
                      (f.get('width'), f.get('height')) != (args.width, args.height)
                      for f in frames)
        if invalid:
            errors.append(f'{invalid} decoded frames have unexpected pixel geometry.')

        video_duration = video.get('duration')
        audio_duration = audios[0].get('duration') if audios else None
        if not audios:
            errors.append('No audio stream found; confirm whether a silent export was intended.')
        if video_duration is not None and audio_duration is not None:
            if abs(float(video_duration)-float(audio_duration)) > .10:
                errors.append('Audio/video durations differ by more than 100 ms.')

        decoded = subprocess.run(['ffmpeg', '-v', 'error', '-xerror', '-i',
            str(args.video.resolve()), '-map', '0:v:0', '-map', '0:a:0?',
            '-f', 'null', '-'], capture_output=True, text=True)
        if decoded.returncode or decoded.stderr.strip():
            errors.append('Full decode reported an error: '+decoded.stderr.strip()[:1200])
        report = {
            'file': str(args.video.resolve()), 'passed': not errors,
            'width': video.get('width'), 'height': video.get('height'),
            'pixel_aspect_ratio': video.get('sample_aspect_ratio'),
            'display_aspect_ratio': actual_dar, 'frames_checked': len(frames),
            'video_duration': video_duration, 'audio_duration': audio_duration,
            'full_decode_passed': decoded.returncode == 0 and not decoded.stderr.strip(),
            'errors': errors,
            'requires_separate_review': 'Framing, cuts, graphics, caption accuracy, listening, and perceived sync.'
        }
        print(json.dumps(report, indent=2))
        return int(bool(errors))
    except (subprocess.CalledProcessError, ValueError, KeyError) as error:
        print(json.dumps({'file': str(args.video), 'passed': False,
                          'errors': [str(error)]}, indent=2))
        return 1


if __name__ == '__main__':
    sys.exit(main())
