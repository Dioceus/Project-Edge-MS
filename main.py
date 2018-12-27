import argparse
import os
import json
from shutil import rmtree
from analyze import get_average_lightness
from segment import segment_division 
from segment import Segment 
from PIL import Image 

"""
1. Take image
2. Determine Average Lightness of an image (Sum of R,G,B) - Done 
2. a) Add up the R,G,B of every pixel, and divide by number of pixels to get average Lightness
3. Segment the image (Cut into parts, use Spritesheets)
4. ANalyze each segment - Determine average lightness of each segment 
5. If Segment Lightness is different than the average Lightness of the image, then count that as a lesion

Problem:
1. Precision: How do I know how to segment the image, into what sizes and how many images: lesions can vary in size
2. Possibly the fact that the spots are not the only white things, so the image needs to check with surroundings

"""

def main(path, filename):
     
    input_image = Image.open(path) 
    
    with Image.open(filename) as input_image: 
         width, height = input_image.size 

    # Init variables, determine average lightness of the image 
    avg_lightness = get_average_lightness(input_image, 0, 0, width, height)

    num_across = width / segment_division(input_image)[0]
    num_down = height / segment_division(input_image)[1]
    single_segments = []
    segment_width = segment_division(input_image)[0] 
    segment_height = segment_division(input_image)[1] 
    for i in range(num_across):
         for j in range(num_down):
              single_segments.append(Segment(input_image, i * segment_width, j * segment_height, segment_width, segment_height)) 
    
    


