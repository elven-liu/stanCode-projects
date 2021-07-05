"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, green screen figure image
    :return: the green screen pixels are replaced by pixels of background image
    """
    for y in range(background_img.height):
        for x in range(background_img.width):
            pixel_fg = figure_img.get_pixel(x, y)
            bigger = max(pixel_fg.red, pixel_fg.blue)
            # The green pixels will be replaced when green pixel is 2 times higher than the bigger pixel.
            if pixel_fg.green > (bigger * 2):
                pixel_bg = background_img.get_pixel(x, y)
                pixel_fg.red = pixel_bg.red
                pixel_fg.blue = pixel_bg.blue
                pixel_fg.green = pixel_bg.green

    return figure_img


def main():
    """
    This function conducts green screen replacement
    which is able to photoshop a person onto any background
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    space_ship.make_as_big_as(figure)
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
