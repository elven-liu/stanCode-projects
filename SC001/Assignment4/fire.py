"""
File: fire.py
Name: Elven Liu
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    This function is to detect if this area's red pixel is above average * HURDLE_FACTOR and highlight the fire area
    with red and other areas with gray.
    :param filename: str, the file path of the original image
    :return: The image with fire-emphasized area.
    """
    new_img = SimpleImage(filename)
    for pixel in new_img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3
        # fire area will be red
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        # other area will be gray scale
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return new_img


def main():
    """
    This program helps to detect fire, so the fire area will be red and other areas will be gray.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
