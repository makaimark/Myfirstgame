import sys
import curses
import random
import string

bomb = ['_____',
        '|...|',
        '|...|',
        '.\./.',
        '..V..']


def function_to_writefile(filename):
    with open(filename, mode='a') as f:
        f.write(name + " " + str(score_output))
        f.write('\n')
        f.close()


def function_to_readfile(filename):
    with open('highscore.txt', mode='r') as f:  # write the name and the result to the txt
        for line in f:
            highscore.append(line)


def name_input():
    name1 = input("Write here your name: ")
    return name1

name = name_input()


def draw_menu(win):
    win.border(0)
    win.addstr(2, 30, str("Kill the Bombs"), curses.A_BOLD)
    win.addstr(3, 22, str("All rights reserved by codecool"))
    win.addstr(5, 3, str("For Stage 1, press 1"))
    win.addstr(6, 3, str("For Stage 2, press 2"))
    win.addstr(7, 3, str("For Stage 3, press 3"))
    win.addstr(8, 3, str("Press SPACE to exit"))


# def menu(key_menu):

def main(scr):
    curses.noecho()  # Disable default printing of inputs
    curses.curs_set(0)  # hiding cursor visibility
    win = curses.newwin(curses.LINES, curses.COLS, 0, 0)  # Init window object
    win.border(0)  # init window border
    win.keypad(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)  # responsible to the colouring of the harts
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLUE)  # responsible to the colouring of the skulls
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    win.bkgd(' ', curses.color_pair(3))
    win.refresh()

    index = 0  # init index, what helps to draw the objects line by line
    key = ""
    y_coordinate = 0
    x_coordinate = 0
    y = 0
    bomb_is_killed = False  # If the bomb killed, change to True
    score = 0           # count the killed bombs
    result = []
    first_turn = False
    score_output = 0
    life = 3
    key_menu = ""
    operands = ['+', '-', '*', '/']
    level2_result = []
    random_character_level3 = []
    rand_char_level1 = ""
    highscore = []

    while True:
        draw_menu(win)
        key_menu = win.getch()

        if key_menu == 49:      # press 1 to stage one
            score = 0
        elif key_menu == 50:    # press 2 to stage two
            score = 11
        elif key_menu == 51:    # press 2 to stage two
            score = 21
        elif key_menu == 32:    # press space to exit
            key = 32
            break

        life = 3

        if key_menu == 49 or key_menu == 50 or key_menu == 51:

            while key != 27:            # not Esc is pressed
                win.clear()             # clear screen
                win.border(0)           # draw border
                win.addstr(1, 2, str("Your score:"))
                win.addstr(2, 2, str(score_output))  # draw score
                win.addstr(3, 2, " ❤ " * life, curses.color_pair(1))  # show your number of lifes

                if bomb_is_killed or y_coordinate == 0 or y == 23:  # begining of the loop, make a random x coordinate
                    if bomb_is_killed:
                        win.addstr(5, 2, " ☠ ", curses.color_pair(1))     # Write a skull if bomb killed
                        curses.beep()
                        win.timeout(3000)
                        win.refresh()

                    y_coordinate = 0                # set y coordinate to 0
                    x_coordinate = random.randint(12, 75)  # random x coordinate
                    random_object_number = random.randint(0, 4)  # help to choose a level1 object
                    result = []  # this makes the result list empty again
                    bomb_is_killed = False
                    random_character_level3 = []

                if score >= 0 and score <= 10:  # level 1, between score 0-10
                    if y_coordinate == 0:
                        rand_char_level1 = random.choice(string.ascii_lowercase)
                        bomb[1] = '|.'+rand_char_level1+'.|'

                    for index, value in enumerate(bomb):  # responsible for the bomb drawing
                        list2 = str(value)
                        win.addstr(index+1+y_coordinate, x_coordinate, list2, curses.color_pair(2))  # draw the bomb
                    if key == ord(rand_char_level1):
                        bomb_is_killed = True      # if the pressed key = the object's letter, kill the bomb
                        score += 1       # if the bomb killed, add one to the score
                        score_output += 1
                        win.timeout(250)
                        win.clear()
                        continue

                elif score >= 11 and score <= 20:
                    if y_coordinate == 0:
                        result_operand = -1
                        while result_operand > 9 or result_operand < 0 or result_operand % 1:
                            rand_num1 = random.choice(list(string.digits))
                            rand_operand = random.choice(operands)
                            rand_num2 = random.choice(list(string.digits))
                            if int(rand_num2) == 0:
                                rand_num2 = random.choice(list(string.digits))
                            bomb[1] = '|'+rand_num1+rand_operand+rand_num2+'|'

                            if rand_operand == '+':
                                result_operand = int(rand_num1) + int(rand_num2)
                            elif rand_operand == '-':
                                result_operand = int(rand_num1) - int(rand_num2)
                            elif rand_operand == '/':
                                result_operand = int(rand_num1) / int(rand_num2)
                            elif rand_operand == '*':
                                result_operand = int(rand_num1) * int(rand_num2)

                    result_operand = int(result_operand)

                    for index, value in enumerate(bomb):            # drowing the omb object
                        list2 = str(value)
                        win.addstr(index+1+y_coordinate, x_coordinate, list2, curses.color_pair(2))

                    if key == ord(str(result_operand)):     # if the key == the ascii number of the result number
                        bomb_is_killed = True
                        score += 1       # if the bomb killed, add one to the score
                        score_output += 1
                        win.timeout(250)
                        continue

                elif score >= 21 and score <= 30:
                    for i in range(0, 3):
                        random_character_level3.append(random.choice(list(string.ascii_lowercase)))     # random char1

                    bomb[1] = '|'+random_character_level3[0]+random_character_level3[1]+random_character_level3[2]+'|'
                    # change the text_box part of the bomb object

                    if first_turn is False:
                        result.append("")       # cheat line^^ :D it is a must, sorry
                        result.append("")       # cheat line 2 ^^ :D
                        first_turn = True

                    for index, value in enumerate(bomb):        # responsible for the bomb drawing
                        list2 = str(value)
                        win.addstr(index+1+y_coordinate, x_coordinate, list2, curses.color_pair(2))

                    if (len(result) == 3 and result[0] == ord(random_character_level3[0]) and result[1] == ord(random_character_level3[1]) and result[2] == ord(random_character_level3[2])):
                        bomb_is_killed = True       # previous: if the pressed buttons are OK, kill the bomb
                        score += 1       # if the bomb killed, add one to the score
                        score_output += 1
                        win.timeout(250)
                        result = []  # this line makes the list empty again
                        continue
                    else:
                        if key != -1 and key != 32:  # we need this line, because -1-s appear in every loop
                            if len(result) >= 3:  # if the list contains 3 or more element what is not we need, empty it
                                result = []
                            result.append(key)  # append the inputed letters to the list

                if score >= 31:
                    win.clear()
                    win.addstr(12, 40, "Victory!!! Press p to play a new game")  # press p to play a new game
                    win.addstr(13, 40, "Press m to reach the menu")
                    function_to_readfile("highscore.txt")

                    highscore.append(name + str(score))     # append the new highscore element

                    function_to_writefile("highscore.txt")

                    win.refresh()
                    key = win.getch()

                    if key == 112:      # press p to play a new game
                        score = 0
                        score_output = 0
                        continue
                    elif key == 109:       # Press m to reach the menu
                        score = 0
                        score_output = 0
                        break

                y_coordinate = y_coordinate + 1                # responsible for the y movement
                y = index + 1 + y_coordinate                    # helps to draw the bomb objects line by line

                if y == 23:                 # if the bomb is in the bottom, minus 1 life
                    life = life - 1

                if life == 0:           # if you are out of lifes
                    function_to_readfile("highscore.txt")

                    highscore.append(name + str(score))

                    function_to_writefile("highscore.txt")

                    win.clear()
                    win.addstr(12, 25, "You lose! Press x to back to the menu!")
                    win.refresh()
                    while key != 120:       # waiting for an X to go back to the menu
                        key = win.getch()
                    else:
                        break               # if we got it, break from this loop

                win.refresh()
                win.timeout(250)        # wait 0,1 sec

                key = win.getch()       # we are waiting for inputs, and put it to the key

                if key == 27:
                    win.clear()
curses.wrapper(main)
