# Algorithm for Detecting lesions in MRI scans

Here is the algorithm for non-coding contributors

1. Enter image
2. Determine Average Lightness of an image (Sum of R,G,B) 
   by finding the sum of the R,G,B value of every pixel, and divide by number of pixels to get average Lightness
3. Segment the image (Cut into parts, use Spritesheets)
4. Analyze each segment -> That is, determine average lightness of each segment 
5. If Segment Lightness is different than the average Lightness of the image, then count that as a lesion.
   
   If T1 - Weighted MRI Image - Look for dark spots - avg lightness of spots should be less than avg lightness of image. 
    If T2 - Weighted MRI Image - Look for bright spots - avg lightness of spots should be greater than avg lightness of image 
