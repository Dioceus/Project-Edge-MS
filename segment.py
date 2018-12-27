import pygame
from PIL import Image 

def segment_division(input_image):
    size = input_image.size
    """
    if size < 3:
        return [size, 1]
    """
    result = list()
    for i in range(1, int(size ** 0.5) + 1):
       div, mod = divmod(size, i)
       #ignore 1 and n itself as factors
       if mod == 0 and i != 1 and div != size:
           result.append(div)
           result.append(i)
    if len(result)==0: # if no factors then add 1
        return segment_division(size+1)
    return result[len(result)-2:]
    #segment_division[0] is width and segment_division[1] is height 

class Segment:
    #image = input_image
    #width = 0
    #height = 0
    def _init_(self, input_image, x, y, width, height):
        self.image = pygame.image.load(input_image).convert()
        self.x = x
        self.y = y
        self.width = width
        self.height = height 
        



