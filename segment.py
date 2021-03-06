import pygame
from PIL import Image 

def segment_division(input_image):
    size = input_image.size
    area = size[0] * size[1]
    #print(size)
    """
    if size < 3:
        return [size, 1]
    """
    result = list()
    x = int(area ** 0.5)
    for i in range(1, x + 1):
       div, mod = divmod(area, i) 
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
        
        self.image = self.get_image(pygame.image.load(input_image).convert(), x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def get_image(self, input_image, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """
        # Create a new blank image
        image = self.image.Surface([width, height])
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(input_image, (0, 0), (x, y, width, height))
 
        # Return the image
        return image    
