"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return img: SimpleImage,
    """
    big = SimpleImage(filename)
    small = SimpleImage.blank(big.width // 2, big.height // 2)

    for x in range(small.width):
        for y in range(small.height):
            # small pixel
            s = small.get_pixel(x, y)
            # big pixel
            b = big.get_pixel(2 * x, 2 * y)

            s.red = b.red
            s.green = b.green
            s.blue = b.blue
    return small


def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()




if __name__ == '__main__':
    main()
