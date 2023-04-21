#!/usr/bin/env python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scorpion.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: slegaris <slegaris@student.42madrid.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/04/21 13:48:44 by slegaris          #+#    #+#              #
#    Updated: 2023/04/21 13:56:32 by slegaris         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import sys
import exifread
from getkey import getkey, keys

def read_exif(file_path):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                print(f"{tag}: {tags[tag]}")

print("Welcome to the EXIF data viewer!\n"
        "To view the EXIF data for each image, press Enter.\n"
        "To exit the program, press Esc.\n")

if len(sys.argv) == 1:
    files = os.listdir('.')
else:
    files = sys.argv[1:]

for file_path in files:
    if os.path.isdir(file_path):
        for root, _, filenames in os.walk(file_path):
            for filename in filenames:
                print(f"Image: {os.path.join(root, filename)}")
                while True:
                    key = getkey()
                    if key == keys.ENTER:
                        read_exif(os.path.join(root, filename))
                        break
                    elif key == keys.ESC:
                        sys.exit()
    else:
        print(f"Image: {file_path}")
        while True:
            key = getkey()
            if key == keys.ENTER:
                read_exif(file_path)
                break
            elif key == keys.ESC:
                sys.exit()
