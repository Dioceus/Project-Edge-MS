from PIL import Image

def get_rgb(input_file, x, y):
        pix = input_file.load()
        return 3*pix[x,y] 

def get_average_lightness(input_file, x, y, width, height):
        total_val = 0.0
        for x in range(width):
                for y in range(height):
                        total_val += total_val + get_rgb(input_file, x, y)
        #total_val *= 3  
        return total_val/(width*height) 
