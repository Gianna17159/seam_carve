PROGRAM DESCRIPTION

This program resizes an image horizontally by removing unimportant pixels from the image. This finds the vertical "seams" in the image representing the pixels that have the lowest difference in color from their neighbors and, thus, can be removed without significantly altering the image. 

THE ALGORITHM

To resize an image, the seam careve algorithm completes two main steps:

1. Finding the importance value of each pixel in the image.
2. Finding the seam of least importance in the image to be removed

These steps are repeated multiple times until the remaining image has decreased by the desired amount of width.

TO RUN CODE

Running the program will produce two images: the first will be a modification of the original image that has the seam(s) carved out, the second is the original image with a visual representation of the seam(s) that were carved.
Running the code normally will automatically use the default image (example01.png) provided in the seamcarve_images folder and will carve just 1 seam. You can also use your own custom image, or increase the number of seams carved.
To run the program with custom images/number of seams, provide that information as inputs to the main method using the terminal.

To run code...

1. with the default image and 1 seam: python seamcarve.py
2. with the default image and more than one seam: python seamcarve.py --seamcount <number>
3. with a custom image and one seam: python seamcarve.py --path <path to custom image>
4. with a custom image and more than one seam: python seamcarve.py --path <path to custom image> --seamcount <number>
