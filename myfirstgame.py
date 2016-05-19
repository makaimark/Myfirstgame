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
    bomb_is_killed = False

    while key != 27:            # not Esc is pressed
        win.clear()             # clear screen
        win.border(0)           # draw border

        if bomb_is_killed or y_coordinate == 0 or y == 23:   # at the begining of the loop, make a random x coordinate
            y_coordinate = 0
            x_coordinate = random.randint(5,75)
            random_object_number = random.randint(0,4)
                  # at the end of the game space, create a new x coordinate

        if (key == 97 and random_object_number == 0) or (key == 98 and random_object_number == 1) or (key == 99 and random_object_number == 2) or (key == 100 and random_object_number == 3) or (key == 101 and random_object_number == 4):
            bomb_is_killed = True
            continue
        else:
            bomb_is_killed = False
            for index, value in enumerate(objects.level1[random_object_number]):  # responsible for the bomb object drawing
                list2 = str(value)
                win.addstr(index+1+y_coordinate,x_coordinate,list2)

        y_coordinate =  y_coordinate + 1                # responsibl for the y movement
        y = index + 1 + y_coordinate

        win.refresh()
        win.timeout(500)        # wait 0,1 sec

        key = win.getch()


curses.wrapper(main)
