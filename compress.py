# -*- coding: utf-8 -*-

import os
from os import listdir
from os.path import isfile, join, splitext
from io import BytesIO
import argparse

from PIL import Image
from pydub import AudioSegment

class Compress():

    def __init__(self, src_dir, des_dir):
        self.src_dir = src_dir
        self.des_dir = des_dir

    def get_files(self):
        onlyfiles = [f for f in listdir(self.src_dir) if isfile(join(self.src_dir, f))]
        return onlyfiles

    def compress_mp3(self, file_name):
        sound = AudioSegment.from_file(join(self.src_dir, file_name))
        out = BytesIO()
        sound.export(out, format="mp3", bitrate="32k")
        self.save(file_name, out.getvalue())

    def compress_img(self, file_name):
        im = Image.open(join(self.src_dir, file_name))
        out = BytesIO()
        im.save(out, format='jpeg', quality=20)
        self.save(splitext(file_name)[0]+'.jpg', out.getvalue())

    def save(self, file_name, data):
        with open(join(self.des_dir, file_name), 'wb') as f:
            f.write(data)

    def run(self):
        os.makedirs(self.src_dir, exist_ok=True)
        os.makedirs(self.des_dir, exist_ok=True)
        files = self.get_files()
        count = len(files)
        for i, f in enumerate(files):
            if f.endswith('.mp3'):
                self.compress_mp3(f)
            elif f.endswith(('.png', '.jpg', '.jpeg')):
                self.compress_img(f)
            else:
                continue
            print('({}/{}){}'.format(i + 1, count, f))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('src_dir')
    parser.add_argument('des_dir')
    
    a = parser.parse_args()
    Compress(a.src_dir, a.des_dir).run()

