#!/usr/bin/env python3

import os
import subprocess
import sys

W = 20
H = 50

DUR_CMD = 'ffprobe -i {file} -show_entries format=duration -v quiet -of csv="p=0"'
SPR_CMD = 'ffmpeg -i {file} -frames 1 -q:v 2 -filter_complex "fps={fps},scale=-1:96,tile={W}x{H}" {file}.png'


def main(filename):
  cmd_out = subprocess.run(DUR_CMD.format(file=filename), capture_output=True, shell=True, text=True)
  duration = (W * H * 1.0) / float(cmd_out.stdout)
  os.system(SPR_CMD.format(file=filename, fps=duration, W=W, H=H))


if __name__ == '__main__':
  main(sys.argv[1])
