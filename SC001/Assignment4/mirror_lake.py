"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return: The mirror image.
    """
    new_img = SimpleImage(filename)
    blank_img = SimpleImage.blank(new_img.width, new_img.height * 2)

    for x in range(new_img.width):
        for y in range(new_img.height):
            # new_img pixel
            p = new_img.get_pixel(x, y)
            # blank 1 pixel
            bp1 = blank_img.get_pixel(x, y)
            # blank 2 pixel
            bp2 = blank_img.get_pixel(x, blank_img.height-1-y)

            bp1.red = p.red
            bp1.green = p.green
            bp1.blue = p.blue

            bp2.red = p.red
            bp2.green = p.green
            bp2.blue = p.blue
    return blank_img


def main():
    """
    This program is to print out the mirror image.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
