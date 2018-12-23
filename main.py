import argparse
import os
import json
from shutil import rmtree
from analyze import get_average_hsv

def main(input_folder):
     # Append '/' to folder location if not present
    input_folder += '' if '/' in input_folder else '/'
    # Filter images for jpg files only
    images = [img for img in os.listdir(input_folder) if img.endswith('.jpg')]

    # Init variables
    total_h = total_s = total_v = 0.0
    h, s, v = get_average_hsv(input_folder)


