import pygame
from PIL import Image

def _init_(self, input_image):
    self.image = pygame.image.load(input_image).convert()

#def get_segment(self):
    

def segment_division(input_image.size):
    if (input_image.size<3):
        return [input_image.size, 1]
    result = list()
    for i in range(1, int(input_image.size ** 0.5) + 1):
       div, mod = divmod(input_image.size, i)
       #ignore 1 and n itself as factors
       if mod == 0 and i != 1 and div != input_image.size:
           result.append(div)
           result.append(i)
    if len(result)==0: # if no factors then add 1
        return divide_equally(input_image.size+1)
    return result[len(result)-2:]

