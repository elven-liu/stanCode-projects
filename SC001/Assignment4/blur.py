"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(smile):
    """
    :param smile: (SimpleImage) the original image
    :return: the blur image (only 1 time)
    """
    blank_smile = SimpleImage.blank(smile.width, smile.height)

    for x in range(smile.width):
        for y in range(smile.height):
            # smile pixel
            p = smile.get_pixel(x, y)
            # blank pixel
            b = blank_smile.get_pixel(x, y)

            # pixel(0,0) will only have 3 neighborhoods.
            if x == 0 and y == 0:
                b.red = (p.red + smile.get_pixel(x, y + 1).red +
                         smile.get_pixel(x + 1, y).red + smile.get_pixel(x + 1, y + 1).red) // 4
                b.green = (p.green + smile.get_pixel(x, y + 1).green +
                           smile.get_pixel(x + 1, y).green + smile.get_pixel(x + 1, y + 1).green) // 4
                b.blue = (p.blue + smile.get_pixel(x, y + 1).blue +
                          smile.get_pixel(x + 1, y).blue + smile.get_pixel(x + 1, y + 1).blue) // 4
            # pixel(0,smile.height-1) will only have 3 neighborhoods
            elif x == 0 and y == smile.height - 1:
                b.red = (p.red + smile.get_pixel(x, y - 1).red +
                         smile.get_pixel(x + 1, y - 1).red + smile.get_pixel(x + 1, y).red) // 4
                b.green = (p.green + smile.get_pixel(x, y - 1).green +
                           smile.get_pixel(x + 1, y - 1).green + smile.get_pixel(x + 1, y).green) // 4
                b.blue = (p.blue + smile.get_pixel(x, y - 1).blue +
                          smile.get_pixel(x + 1, y - 1).blue + smile.get_pixel(x + 1, y).blue) // 4
            # pixel(smile.width-1,0) will only have 3 neighborhoods
            elif x == smile.width - 1 and y == 0:
                b.red = (p.red + smile.get_pixel(x - 1, y).red +
                         smile.get_pixel(x - 1, y + 1).red + smile.get_pixel(x, y + 1).red) // 4
                b.green = (p.green + smile.get_pixel(x - 1, y).green +
                           smile.get_pixel(x - 1, y + 1).green + smile.get_pixel(x, y + 1).green) // 4
                b.blue = (p.blue + smile.get_pixel(x - 1, y).blue +
                          smile.get_pixel(x - 1, y + 1).blue + smile.get_pixel(x, y + 1).blue) // 4
            # pixel(smile.width-1,smile.height-1) will only have 3 neighborhoods
            elif x == smile.width - 1 and y == smile.height - 1:
                b.red = (p.red + smile.get_pixel(x - 1, y).red +
                         smile.get_pixel(x - 1, y - 1).red + smile.get_pixel(x, y - 1).red) // 4
                b.green = (p.green + smile.get_pixel(x - 1, y).green +
                           smile.get_pixel(x - 1, y - 1).green + smile.get_pixel(x, y - 1).green) // 4
                b.blue = (p.blue + smile.get_pixel(x - 1, y).blue +
                          smile.get_pixel(x - 1, y - 1).blue + smile.get_pixel(x, y - 1).blue) // 4
            # pixel(0,y) will only have 5 neighborhoods
            elif x == 0:
                b.red = (p.red + smile.get_pixel(x, y - 1).red + smile.get_pixel(x + 1, y - 1).red +
                         smile.get_pixel(x + 1, y).red + smile.get_pixel(x + 1, y + 1).red + smile.get_pixel(x, y + 1).red) // 6
                b.green = (p.green + smile.get_pixel(x, y - 1).green + smile.get_pixel(x + 1, y - 1).green +
                         smile.get_pixel(x + 1, y).green + smile.get_pixel(x + 1, y + 1).green + smile.get_pixel(x, y + 1).green) // 6
                b.blue = (p.blue + smile.get_pixel(x, y - 1).blue + smile.get_pixel(x + 1, y - 1).blue +
                         smile.get_pixel(x + 1, y).blue + smile.get_pixel(x + 1, y + 1).blue + smile.get_pixel(x, y + 1).blue) // 6
            # pixel(x,0) will only have 5 neighborhoods
            elif y == 0:
                b.red = (p.red + smile.get_pixel(x - 1, y).red + smile.get_pixel(x - 1, y + 1).red +
                         smile.get_pixel(x, y + 1).red + smile.get_pixel(x + 1, y + 1).red + smile.get_pixel(x + 1, y).red) // 6
                b.green = (p.green + smile.get_pixel(x - 1, y).green + smile.get_pixel(x - 1, y + 1).green +
                           smile.get_pixel(x, y + 1).green + smile.get_pixel(x + 1, y + 1).green + smile.get_pixel(x + 1, y).green) // 6
                b.blue = (p.blue + smile.get_pixel(x - 1, y).blue + smile.get_pixel(x - 1, y + 1).blue +
                          smile.get_pixel(x, y + 1).blue + smile.get_pixel(x + 1, y + 1).blue + smile.get_pixel(x + 1, y).blue) // 6
            # pixel(smile.width-1,y) will only have 5 neighborhoods
            elif x == smile.width - 1:
                b.red = (p.red + smile.get_pixel(x, y - 1).red + smile.get_pixel(x - 1, y - 1).red +
                         smile.get_pixel(x - 1, y).red + smile.get_pixel(x - 1, y + 1).red + smile.get_pixel(x, y + 1).red) // 6
                b.green = (p.green + smile.get_pixel(x, y - 1).green + smile.get_pixel(x - 1, y - 1).green +
                           smile.get_pixel(x - 1, y).green + smile.get_pixel(x - 1, y + 1).green + smile.get_pixel(x, y + 1).green) // 6
                b.blue = (p.blue + smile.get_pixel(x, y - 1).blue + smile.get_pixel(x - 1, y - 1).blue +
                          smile.get_pixel(x - 1, y).blue + smile.get_pixel(x - 1, y + 1).blue + smile.get_pixel(x, y + 1).blue) // 6
            # pixel(x,smile.height-1) will only have 5 neighborhoods
            elif y == smile.height - 1:
                b.red = (p.red + smile.get_pixel(x - 1, y).red + smile.get_pixel(x - 1, y - 1).red +
                         smile.get_pixel(x, y - 1).red + smile.get_pixel(x + 1, y - 1).red + smile.get_pixel(x + 1, y).red) // 6
                b.green = (p.green + smile.get_pixel(x - 1, y).green + smile.get_pixel(x - 1, y - 1).green +
                           smile.get_pixel(x, y - 1).green + smile.get_pixel(x + 1, y - 1).green + smile.get_pixel(x + 1, y).green) // 6
                b.blue = (p.blue + smile.get_pixel(x - 1, y).blue + smile.get_pixel(x - 1, y - 1).blue +
                          smile.get_pixel(x, y - 1).blue + smile.get_pixel(x + 1, y - 1).blue + smile.get_pixel(x + 1, y).blue) // 6
            # other pixels in the middle will have 8 neighborhoods.
            else:
                b.red = (p.red + smile.get_pixel(x - 1, y - 1).red + smile.get_pixel(x, y - 1).red +
                         smile.get_pixel(x + 1, y - 1).red + smile.get_pixel(x + 1, y).red + smile.get_pixel(x + 1, y + 1).red
                         + smile.get_pixel(x, y + 1).red + smile.get_pixel(x - 1, y + 1).red + smile.get_pixel(x - 1, y).red) // 9
                b.green = (p.green + smile.get_pixel(x - 1, y - 1).green + smile.get_pixel(x, y - 1).green +
                         smile.get_pixel(x + 1, y - 1).green + smile.get_pixel(x + 1, y).green + smile.get_pixel(x + 1, y + 1).green
                         + smile.get_pixel(x, y + 1).green + smile.get_pixel(x - 1, y + 1).green + smile.get_pixel(x - 1, y).green) // 9
                b.blue = (p.blue + smile.get_pixel(x - 1, y - 1).blue + smile.get_pixel(x, y - 1).blue +
                         smile.get_pixel(x + 1, y - 1).blue + smile.get_pixel(x + 1, y).blue + smile.get_pixel(x + 1, y + 1).blue
                         + smile.get_pixel(x, y + 1).blue + smile.get_pixel(x - 1, y + 1).blue + smile.get_pixel(x - 1, y).blue) // 9
    return blank_smile


def main():
    """
    This program is to blur image. Users can enter the numbers to decide how many times will the blur function works.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    # the number can decide how many times will the blur function works.
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
