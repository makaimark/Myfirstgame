import sys

import curses

import objects

import random

def main(scr):

    curses.noecho()  #Disable default printing of inputs
    curses.curs_set(0) #hiding cursor visibility
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0) # Init window object
    win.border(0)

    list = str(win.getmaxyx())
    win.addstr(0,0,list)

    key = ""

    y_coordinate = 0
    y = 0

    while key != 27:            # not Esc is pressed
        win.clear()             # clear screen
        win.border(0)           # draw border
        if y_coordinate == 0:   # at the begining of the loop, make a random x coordinate
            x_coordinate = random.randint(5,75)
        if y == 23:             # at the end of the game space, create a new x coordinate
            y_coordinate = 0
            x_coordinate = random.randint(5,75)

        for index, value in enumerate(objects.level1):  # responsible for the bomb object drawing
            list2 = str(value)
            win.addstr(index+1+y_coordinate,x_coordinate,list2)

        y_coordinate =  y_coordinate + 1                # responsibl for the y movement
        y = index + 1 + y_coordinate
        win.refresh()
        win.timeout(100)        # wait 1 sec
        key = win.getch()     # get the code of pressed key

curses.wrapper(main)
