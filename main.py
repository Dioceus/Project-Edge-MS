import argparse
import os
import json
from analyze import get_average_lightness
from segment import segment_division 
from segment import Segment 
from PIL import Image 

"""
1. Take image
2. Determine Average Lightness of an image (Sum of R,G,B) 
2. a) Add up the R,G,B of every pixel, and divide by number of pixels to get average Lightness
3. Segment the image (Cut into parts, use Spritesheets)
4. Analyze each segment - Determine average lightness of each segment 
5. If Segment Lightness is different than the average Lightness of the image, then count that as a lesion
5. a) If T1 - Weighted MRI Image - Look for dark spots - avg lightness of spots should be less than avg lightness of image 
5. b) If T2 - Weighted MRI Image - Look for bright spots - avg lightness of spots should be greater than avg lightness of image 
"""

def main(filepath):
    
    input_image = Image.open(filepath)
    
    with Image.open(filepath) as input_image: 
         width, height = input_image.size 

    input_image = Image.open(filepath)
    # Init variables, determine average lightness of the image 
    avg_lightness = get_average_lightness(input_image, 0, 0, width, height)
    segment_width = segment_division(input_image)[0] 
    segment_height = segment_division(input_image)[1] 

    num_across = int(width / segment_width)
    num_down = int(height / segment_height)
    single_segments = []
    n = num_across * num_down 

    for i in range(num_across):
         for j in range(num_down):
              single_segments.append(Segment(input_image, i * segment_width, j * segment_height, segment_width, segment_height)) 
     
    type_of_mri = int(input("Which type of MRI are you using? Enter 1 if T-1 Weighted MRI or 2 for T-2 Weighted MRI."))
    print(determine_lesions(n, type_of_mri, avg_lightness, single_segments))

def determine_lesions(num_segments, MRI_type, img_avg_lightness, segmented_region = []):
     num_lesions = 0 
     for count in range(num_segments):
          if MRI_type == 1: #T-MRI 1, so it should detect black spots
               if get_average_lightness(segmented_region[count], segmented_region[count].x, segmented_region[count].y, segmented_region[count].width, segmented_region[count].height) < img_avg_lightness:
                    num_lesions += 1
          else: #T-MRI 2, so it should detect white spots
               if get_average_lightness(segmented_region[count], segmented_region[count].x, segmented_region[count].y, segmented_region[count].width, segmented_region[count].height) > img_avg_lightness:
                    num_lesions += 1
     return num_lesions 

image_path = input("Please enter the image filepath for the MRI image you wish to analyze. ")
main(image_path)