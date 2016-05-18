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

    x_koordinate = random.randint(1,79)

    #while objects.level1.:
    for index, value in enumerate(objects.level1):
        list2 = str(value)
        win.addstr(index+1,x_koordinate,list2)
        #win.refresh()

    while key != 27:            # not Esc is pressed
        win.timeout(100)        # wait 0.1 sec
        win.refresh()
        key = win.getch()     # get the code of pressed key



curses.wrapper(main)
