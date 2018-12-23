from PIL import Image

import cv2
import numpy as np
from matplotlib import pyplot as plt
import pygame

def __init__(self, file_name):
    self.sprite_sheet = pygame.image.load(file_name).convert()
 

def get_average_hsv(input_file):
    img = cv2.imread(input_file) 
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    hue, sat, val = hsv_image[:,:,0], hsv_image[:,:,1], hsv_image[:,:,2]
    flat_hue = np.ndarray.flatten(hue)
    flat_sat = np.ndarray.flatten(sat)
    flat_val = np.ndarray.flatten(val)

    avg_hue = np.mean(flat_hue)
    avg_sat = np.mean(flat_sat)
    avg_val = np.mean(flat_val)

    return avg_hue, avg_sat, avg_val

def get_image(self, x, y, width, height):

        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Return the image
        return image
