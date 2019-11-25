#!/usr/bin/env python

import sys

import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
from matplotlib.image import imread

# check that python version is 3
if sys.version_info[0] != 3:
    raise Exception("Python3 should be used with this module")

# Rate of animations [per second]
FRAMES_PER_SEC = 50

def import_images():
    # Get user input
    image1_path = input("Enter path for first image\n")
    image2_path = input("Enter path for second image\n")

    # Matplotlib's image module reads images in RGB format (unlike OpenCV!)
    img1 = imread(image1_path)
    img2 = imread(image2_path)

    time = int(input("Enter duration(in seconds) for blending: "))

    # Run animation
    blend(img1, img2, time)

def blend(img1, img2, time):
    fig = plt.figure()

    # Initialise animation frame (matrix)
    blended = np.zeros(img1.shape)

    # Initialise list of images
    imgs = []

    # Global variable
    global FRAMES_PER_SEC

    # Loop cycles over specified number of frames
    for i in range(FRAMES_PER_SEC * time // 2):
        # Increment the opacity variable (0 -> 1)
        alpha = 2 * i / (FRAMES_PER_SEC * time)
        # Generate next frame: scale images inversily (sum of opacity = 1)
        blended = np.array((1 - alpha) * img1 + alpha * img2, dtype=np.uint8)
        # Append image to animation (list of frames)
        imgs.append([plt.imshow(blended, animated=True)])

    # add mirror animation to current animations
    imgs += imgs[::-1]
    
    # Run animation
    ani = animation.ArtistAnimation(fig, imgs, interval=(1 / FRAMES_PER_SEC * 1000))

    # Necessary finish
    plt.show()

if __name__ == "__main__":
    import_images()
