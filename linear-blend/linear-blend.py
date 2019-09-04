#!/usr/bin/env python

import sys

import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt
from matplotlib.image import imread

if sys.version_info[0] != 3:
    raise Exception("Python3 should be used with this module")


FRAMES_PER_SEC = 50


def import_images():
    image1_path = input("Enter path for first image\n")
    image2_path = input("Enter path for second image\n")

    # Matplotlib's image module reads images in RGB format (unlike OpenCV!)
    img1 = imread(image1_path)
    img2 = imread(image2_path)

    time = int(input("Enter duration(in seconds) for blending: "))

    blend(img1, img2, time)


def blend(img1, img2, time):
    fig = plt.figure()
    blended = np.zeros(img1.shape)

    imgs = []
    global FRAMES_PER_SEC
    for i in range(FRAMES_PER_SEC * time):
        alpha = i / (FRAMES_PER_SEC * time)

        blended = np.array((1 - alpha) * img1 + alpha * img2, dtype=np.uint8)
        imgs.append([plt.imshow(blended, animated=True)])

    ani = animation.ArtistAnimation(
        fig, imgs, interval=(1 / FRAMES_PER_SEC * 1000), repeat_delay=50
    )

    plt.show()


if __name__ == "__main__":
    import_images()
