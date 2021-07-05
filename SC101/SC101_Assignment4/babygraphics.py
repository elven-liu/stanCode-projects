"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program is to draw the rank lines for users to know what's the rank of the name each year based on the data we
integrate in the 'babynames.py' file.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    number_of_year = len(YEARS)
    gap = width/number_of_year  # The width of one year
    initial_x = GRAPH_MARGIN_SIZE # The first year's x coordinate
    year_list = []
    for i in range(number_of_year):
        initial_x += gap * i  # Calculate the i-th x coordinate
        year_list.append(initial_x)
        initial_x = GRAPH_MARGIN_SIZE

    return year_list[year_index]


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # The top line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width= 1, fill='black')
    # The bottom line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width= 1, fill='black')

    # Draw the line for every year and print the year on the bottom of every line
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH - (GRAPH_MARGIN_SIZE*2), i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width= 1, fill='black')
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE+TEXT_DX, text=YEARS[i], anchor=tkinter.NW, fill='black', font='verdana 15')

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # The y coordinate for 1 rank
    gap_y = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2) / 1000

    # Find the lookup names in the name data list. Then find the years and the rank to print.
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        rank_value = name_data[name]
        for j in range(len(YEARS)-1):
            # The current year's year and rank.
            if str(YEARS[j]) in rank_value:
                year = str(YEARS[j])
                rank = rank_value[year]
            else:
                # If the name is not in the list for this year, the rank will be 1001.
                rank = 1001

            # Next year's year and rank.
            if str(YEARS[j+1]) in rank_value:
                year_1 = str(YEARS[j+1])
                rank_1 = rank_value[year_1]
            else:
                # If the name is not in the list for this year, the rank will be 1001.
                rank_1 = 1001

            # Current year's x and y coordinate
            x = get_x_coordinate(CANVAS_WIDTH - (GRAPH_MARGIN_SIZE * 2), j)
            x_1 = get_x_coordinate(CANVAS_WIDTH - (GRAPH_MARGIN_SIZE * 2), j+1)

            # Next year's x and y coordinate.
            y = GRAPH_MARGIN_SIZE + gap_y*int(rank)
            y_1 = GRAPH_MARGIN_SIZE + gap_y*int(rank_1)
            canvas.create_line(x, y, x_1, y_1, width=LINE_WIDTH, fill=COLORS[i%4])

            if int(rank) <= 1000:
                # When the rank <= 1000, the name and the rank will be displayed.
                canvas.create_text(x+TEXT_DX, y, text=f"{name} {rank}", anchor=tkinter.NW, fill=COLORS[i%4], font='verdana 10')
            else:
                # When the rank = 1001(over 1000 or not on the list), it will display name **
                canvas.create_text(x+TEXT_DX, y, text=f"{name} **", anchor=tkinter.SW, fill=COLORS[i%4], font='verdana 10')

            # To print the last year.
            if j+1 == len(YEARS) - 1:
                if int(rank_1) <= 1000:
                    canvas.create_text(x_1 + TEXT_DX, y_1, text=f"{name} {rank_1}", anchor=tkinter.NW, fill=COLORS[i%4], font='verdana 10')
                else:
                    canvas.create_text(x_1 + TEXT_DX, y_1, text=f"{name} **", anchor=tkinter.SW, fill=COLORS[i%4], font='verdana 10')


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
