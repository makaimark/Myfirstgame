import sys

import curses

def main(scr):

    curses.noecho()  #Disable default printing of inputs
    curses.curs_set(0) #hiding cursor visibility
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0) # Init window object
    win.border(5)

    key = win.getch()     # get the code of pressed key

    while key != 27:            # not Esc is pressed
        win.timeout(100)        # wait 0.1 sec


        win.refresh()

    win.refresh()

curses.wrapper(main)
