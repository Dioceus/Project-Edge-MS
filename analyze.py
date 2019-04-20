from PIL import Image

def get_rgb(input_file, x, y): 
        #Determines the sum of r,g,b values from taking in an image
        RGB = input_file.getpixel((x,y))
        r_value = RGB[0]
        g_value = RGB[1]
        b_value = RGB[2] 
        return (r_value + g_value + b_value) 

def get_average_lightness(input_file, x, y, width, height):
        total_val = 0.0
        for x in range(width):
                for y in range(height):
                        total_val += get_rgb(input_file, x, y)
        return total_val/(width*height) 
