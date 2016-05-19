import sys

import curses

import objects3

import random


def main(scr):

    curses.noecho()  #Disable default printing of inputs
    curses.curs_set(0) #hiding cursor visibility
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0) # Init window object
    win.border(0)

    list = str(win.getmaxyx())
    win.addstr(0,0,list)

    result = []
    key = ""
    y_coordinate = 0
    y = 0
    bomb_is_killed = False # If the bomb killed, change to True
    score = 0           #count the killed bombs

    while key != 27:            # not Esc is pressed
        win.clear()             # clear screen
        win.border(0)           # draw border
        win.addstr(2,2, str(score))

        if bomb_is_killed or y_coordinate == 0 or y == 23:   # at the begining of the loop, make a random x coordinate
            y_coordinate = 0                # set y coordinate to 0
            x_coordinate = random.randint(5,75) #random x coordinate
            random_object_number = random.randint(0,4)  #help to choose a level1 object
            result = []

        if (len(result) == 3 and ((result[0] == 97 and result[1] == 98 and result[2] == 99 and random_object_number == 0) \
        or ( result[0] == 100 and result[1] == 101 and result[2] == 102 and random_object_number == 1) \
        or ( result[0] == 103 and result[1] == 104 and result[2] == 105 and random_object_number == 2) \
        or ( result[0] == 120 and result[1] == 121 and result[2] == 122 and random_object_number == 3) \
        or ( result[0] == 104 and result[1] == 117 and result[2] == 104 and random_object_number == 4))):
            bomb_is_killed = True       # previous line : if the pressed key = the object's letter, kill the bomb
            win.addstr(5,5,"Bomb is killed")
            score += 1       # if the bomb killed, add one to the score
            win.timeout(500)
            result = []
            continue
        else:
            bomb_is_killed = False
            for index, value in enumerate(objects3.level3[random_object_number]):  # responsible for the bomb object drawing
                list2 = str(value)
                win.addstr(index+1+y_coordinate,x_coordinate,list2)



        y_coordinate =  y_coordinate + 1                # responsible for the y movement
        y = index + 1 + y_coordinate

        win.refresh()
        win.timeout(500)        # wait 0,1 sec

        key = win.getch()
        if key != -1:
            result.append(key)


curses.wrapper(main)