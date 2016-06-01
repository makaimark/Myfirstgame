import objects  # level 1 objects
import objects2  # level 2 objects
import objects3  # level 3 objects
import sys
import curses
import random


def main(scr):
    curses.noecho()  # Disable default printing of inputs
    curses.curs_set(0)  # hiding cursor visibility
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)  # Init window object
    win.border(0)  # init window border
    win.keypad(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)

    # win.bkgd(curses.init_pair(1))
    win.refresh()

    index = 0  # init index, what helps to draw the objects line by line
    key = ""
    y_coordinate = 0
    y = 0
    bomb_is_killed = False  # If the bomb killed, change to True
    score = 0           # count the killed bombs
    result = []
    first_turn = False
    score_output = 0
    life = 3
    key_menu = ""

    while True:
        win.clear()
        win.border(0)
        win.addstr(2, 30, str("Kill the Bombs"), curses.A_BOLD)
        win.addstr(3, 22, str("All rights reserved by codecool"))
        win.addstr(5, 3, str("For Stage 1, press 1"))
        win.addstr(6, 3, str("For Stage 2, press 2"))
        win.addstr(7, 3, str("For Stage 3, press 3"))
        win.addstr(8, 3, str("Press SPACE to exit"))
        key_menu = ""
        key_menu = win.getch()

        if key_menu == 49:
            score = 0
        elif key_menu == 50:
            score = 11
        elif key_menu == 51:
            score = 21
        elif key_menu == 32:
            key = 32
            break

        win.refresh()

        while key != 27:            # not Esc is pressed
            win.clear()             # clear screen
            win.border(0)           # draw border
            win.addstr(1, 2, str("Your score:"))
            win.addstr(2, 2, str(score_output))  # draw score
            win.addstr(3, 2, " ❤ " * life, curses.color_pair(1))

            if bomb_is_killed or y_coordinate == 0 or y == 23:   # at the begining of the loop, make a random x coordinate
                y_coordinate = 0                # set y coordinate to 0
                x_coordinate = random.randint(10, 75)  # random x coordinate
                random_object_number = random.randint(0, 4)  # help to choose a level1 object
                result = []  # this makes the result list empty again

            if score >= 0 and score <= 10:  # level 1, between score 0-10
                for index, value in enumerate(objects.level1[random_object_number]):  # responsible for the bomb object drawing
                    list2 = str(value)
                    win.addstr(index+1+y_coordinate, x_coordinate, list2, curses.color_pair(2))  # draw the bomb objects
                if (key == 97 and random_object_number == 0) or (key == 98 and random_object_number == 1) or (key == 99 and random_object_number == 2) or (key == 100 and random_object_number == 3) or (key == 101 and random_object_number == 4):
                    bomb_is_killed = True       # previous line : if the pressed key = the object's letter, kill the bomb
                    # win.addstr(10, 10, " ☠ ")
                    win.refresh()
                    win.timeout(1000)
                    score += 1       # if the bomb killed, add one to the score
                    score_output += 1
                    continue
                else:
                    bomb_is_killed = False  # if the pressed key not the needed, nothing happen

            elif score >= 11 and score <= 20:
                for index, value in enumerate(objects2.level2[random_object_number]):
                    list2 = str(value)
                    win.addstr(index+1+y_coordinate, x_coordinate, list2, curses.color_pair(2))
                if (key == 54 and random_object_number == 0) or (key == 57 and random_object_number == 1) or (key == 56 and random_object_number == 2) or (key == 51 and random_object_number == 3) or (key == 53 and random_object_number == 4):
                    bomb_is_killed = True   # previous line : if the pressed key = the result of the exercise, kill the bomb
                    score += 1       # if the bomb killed, add one to the score
                    score_output += 1
                    win.timeout(250)
                    result = []
                    continue
                else:
                    bomb_is_killed = False  # if the pressed key not the needed, nothing happen

            elif score >= 21 and score <= 30:
                if first_turn is False:
                    result = []
                    first_turn = True
                for index, value in enumerate(objects3.level3[random_object_number]):
                    list2 = str(value)
                    win.addstr(index+1+y_coordinate, x_coordinate, list2, curses.color_pair(2))
                win.addstr(10, 10, str(result))
                if (len(result) == 3 and ((result[0] == 97 and result[1] == 98 and result[2] == 99 and random_object_number == 0) \
                or (result[0] == 100 and result[1] == 101 and result[2] == 102 and random_object_number == 1) \
                or (result[0] == 103 and result[1] == 104 and result[2] == 105 and random_object_number == 2) \
                or (result[0] == 120 and result[1] == 121 and result[2] == 122 and random_object_number == 3) \
                or (result[0] == 104 and result[1] == 117 and result[2] == 104 and random_object_number == 4))):
                    bomb_is_killed = True       # previous line : if the pressed key = the object's letter, kill the bomb
                    win.addstr(5, 5, "Bomb is killed")
                    score += 1       # if the bomb killed, add one to the score
                    score_output += 1
                    win.timeout(250)
                    result = []  # this line makes the list empty again
                    continue
                else:
                    bomb_is_killed = False  # if the pressed key not the needed, nothing happen
                    if key != -1 and key != 32:  # we need this line, because -1-s appear in every loop
                        if len(result) >= 3:  # if the list contains 3 or more element what is not we need, make the list empty again
                            result = []
                        result.append(key)  # append the inputed letters to the list

            elif score >= 31:
                #  win.addstr(12,40,"Victory!!!")
                #  win.timeout(2000)
                win.refresh()
                win.addstr(12, 40, "Press p to play a new game")  # press p to play a new game
                key = win.getch()
                if key == 112:
                    score = 0
                    continue

            if y == 23:
                life = life - 1

            y_coordinate = y_coordinate + 1                # responsible for the y movement
            y = index + 1 + y_coordinate                    # helps to draw the bomb objects line by line

            if life == 0:
                win.clear()
                win.addstr(12, 25, str("You lose! Try again!"))
                win.timeout(2000)
                life = 3
                key_menu = ""
                break

            win.refresh()
            win.timeout(250)        # wait 0,1 sec

            key = win.getch()       # we are waiting for inputs, and put it to the key


curses.wrapper(main)
