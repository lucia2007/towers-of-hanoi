# https://www.geeksforgeeks.org/clear-screen-python/
import os
# https://stackoverflow.com/questions/15375368/slow-word-by-word-terminal-printing-in-python
import random
import sys
import time
# https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=You%20can%20use%20Python's%20sleep,pauses%20between%20words%20or%20graphics.
from time import sleep

"""Tower of Hanoi"""

# https://rich.readthedocs.io/en/latest/console.html#justify-alignment
# from rich.console import Console

# Rules taken from Wikipedia

# https://patorjk.com/software/taag/#p=display&h=2&f=Big&t=Towers%20of%20Hanoi


def print_logo():
    print("""
 _______                                  __   _    _                   _
|__   __|                                / _| | |  | |                 (_)
   | | _____      _____ _ __ ___    ___ | |_  | |__| | __ _ _ __   ___  _ 
   | |/ _ \ \ /\ / / _ \ '__/ __|  / _ \|  _| |  __  |/ _` | '_ \ / _ \| |
   | | (_) \ V  V /  __/ |  \__ \ | (_) | |   | |  | | (_| | | | | (_) | |
   |_|\___/ \_/\_/ \___|_|  |___/  \___/|_|   |_|  |_|\__,_|_| |_|\___/|_|\n\n""")


def slow_print(text):
    """
    Prints the text slowly, letter by letter.
    https://stackoverflow.com/questions/15375368/slow-word-by-word-terminal-printing-in-python
    """
    for word in text + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()  # defeat buffering
        time.sleep(random.random() * 0.05)


def welcome():
    """
    This function welcomes the user and explains the rules.
    The text is printed slowly.
    """
    print_logo()
    welcome_text = """
Welcome to the Towers of Hanoi!

Your goal is to move all the disks from the first base to the last base.

Rules:

1. You can only move the top disk from one of the bases.
2. You can place it on an empty base or on other disks on a different base.
3. You may not place the chosen disk on top of a smaller disk.

How to play:

1. Choose the base (# 1, 2, 3) FROM WHICH you want to move the top disk.
2. Choose the base (# 1, 2, 3) ON WHICH you want to place the chosen disk.

Warning: If you take a disk which cannot be placed elsewhere, 
you must put it back on the same base.

Good luck!\n"""
    slow_print(welcome_text)


def validate_number(height):
    """
    This function validates if a number was chosen as opposed to a string.
    It also checks if the number is between 3 and 6.
    """
    try:
        height = int(height)
    except ValueError as error:
        print(f"Invalid data: {error}. You did not choose a number.\n")
        return False
    if height >= 3 and height <= 6:
        return True
    else:
        print("You didn't choose a number between 3 and 6. Try again.\n")
        return False
    return True


def choose_difficulty():
    """
    The user chooses the level of difficulty. The higher the number, the more
    difficult the game. The input is validated.
    The function returns the number of disks the user wants to use.
    """
    print("""How many disks do you want to play with? The more disks, the more
difficult the game.\n""")

    while True:
        sleep(1.5)
        disks = input("""Choose a number between 3 and 6.\n\n""")

        if validate_number(disks):
            break

    return int(disks)


class Pyramid:
    """
    Represents a full pyramid of the given number of disks.
    """

    def __init__(self, height: int) -> None:
        """
        This makes a list of numbers from 0 to (height -1).
        https://pythonexamples.org/python-convert-range-into-a-list/
        """
        self.__list_of_disks = list(range(height))

    def is_empty(self) -> bool:
        """
        Tells if the pyramid is empty.
        """
        if len(self.__list_of_disks) == 0:
            return True
        else:
            return False

    def draw_pyramid_row(self, row: int):
        """
        Draws one row of a pyramid.
        """
        if row < 6 - len(self.__list_of_disks):
            print(23*" ", end=" ")
        else:
            j = self.__list_of_disks[row - (6 - len(self.__list_of_disks))]
            disk = (10-2*j)*" " + (4*j + 3) * "*" + (10-2*j)*" "
            print(disk, end=" ")

    def remove_top_disk(self) -> int:
        """
        Removes the uppermost disk.
        Raises exception if the source pyramid is empty.
        """
        if self.is_empty():
            raise Exception("Cannot take a disk from an empty pyramid.")
        return self.__list_of_disks.pop(0)

    def can_place_disk(self, disk: int) -> bool:
        """
        Checks if a disk may be placed on a pyramid
        The destionation pyramid either has to be empty
        or the top disk must be bigger than the one
        which is being moved.
        """
        if self.is_empty():
            return True
        if disk > self.__list_of_disks[0]:
            return False
        return True

    def add_top_disk(self, disk: int) -> None:
        """
        Adds the uppermost disk to a new stack.
        NOT YET - only if the new disk is smaller than the previous one.
        """
        if not self.can_place_disk(disk):
            raise Exception(
                "You may not place a larger disk on a smaller one.")
        self.__list_of_disks.insert(0, disk)

    def get_top_disk(self) -> int:
        """
        Gets the top disk of a pyramid.
        """
        return self.__list_of_disks[0]

    def is_pyramid_full(self, height: int) -> bool:
        """
        Checks is a pyramid has the height equal to the chosen number of disks.
        """
        if len(self.__list_of_disks) == height:
            if moves == 2**height - 1:
                print(
                    f"You used minimum number of moves which is {2**height-1}! Well done!\n")
            else:
                print(
                    f"Congratulations! You won! You used {moves} moves. Minimum number of moves was {2**height -1}.\n")
            return True
        return False


def validate_answer(choice: str) -> bool:
    """
    Validates if the user answered "y" or "n".
    """
    while True:
        choice = choice.upper()
        if choice == "Y" or choice == "N":
            return True
        else:
            print("Invalid answer. You did not choose \"Y\" or \"N\".\n")
            return False


def play_again() -> bool:
    """
    Asks the player if he wants to play again.
    """
    sleep(1)
    print("Do you want to play again?\n")
    while True:
        sleep(1)
        play = input("Press \"Y\" to play and \"N\" to quit.\n")
        if validate_answer(play):
            if play.upper() == "Y":
                print("\n")
                return True
            return False


def print_bases():
    """
    Prints the pyramid bases.
    """
    print(11*"-" + "1" + 11*"-" + " " + 11*"-" +
          "2" + 11*"-" + " " + 11*"-" + "3" + 11*"-" + "\n")
    # print(71*"-", " \n")


def validate_tower_number_from(num: int) -> bool:
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It checks if the tower is not empty.
    """
    try:
        num = int(num)
    except ValueError as error:
        print(f"Invalid data: {error}. You did not choose a number.\n")
        return False
    if not (num >= 1 and num <= 3):
        print("You didn't choose a number between 1 and 3. Try again.\n")
        return False
    if pyramids[num - 1].is_empty():
        print("There is no disk in the chosen pyramid.")
        return False
    return True


def move_disk_from() -> int:
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It validates - NOT YET - if there is no disk smaller than the chosen one
    on the other towers.
    """
    while True:
        src = input("FROM BASE NUMBER:\n")
        if validate_tower_number_from(src):
            break
    return int(src)


def validate_tower_number_to(dst, src: int) -> bool:
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It checks if the top disk is not bigger than the disk on the chosen stack.
    The user may choose the same tower in case he needs to return the disk.
    """
    try:
        dst = int(dst)
    except ValueError as error:
        print(f"Invalid data: {error}. You did not choose a number.\n")
        return False
    if not (dst >= 1 and dst <= 3):
        print("You didn't choose a number between 1 and 3. Try again.\n")
        return False
    # if dst == src:
    #     print("You can not choose the same tower.")
    #     return False
    if pyramids[dst-1].can_place_disk(pyramids[src - 1].get_top_disk()):
        return True
    print("You can't place a bigger disk on a smaller one.")
    return False


def move_disk_to(src: int) -> int:
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It validates(NOT YET) if there is no disk smaller than the chosen one
    It validates if the the user didn't chose the same tower
    """
    while True:
        dst = input("TO BASE NUMBER:\n")
        if validate_tower_number_to(dst, src):
            # print("You are moving the chosen disk from tower number "
            #       f"{src} to tower number {dst}.\n")
            break

    return int(dst)


def draw_pyramids():
    """
    Draws each pyramid up to height 6.
    Draws pyramids next to each other
    Add a new line after the third pyramid's row is printed.
    If pyramid row is empty, draws an empty line.
    If not empty, draws (6 - number of disks) empty lines
    and the respective number of disks.
    """
    os.system("clear")

    for i in range(6):
        for pyramid in pyramids:
            pyramid.draw_pyramid_row(i)
        print("")


welcome()
BASE = int(23)
while True:
    moves = 0
    disks = choose_difficulty()
    pyramids = [Pyramid(disks), Pyramid(0), Pyramid(0)]
    draw_pyramids()
    print_bases()
    while not pyramids[2].is_pyramid_full(disks):
        from_where = move_disk_from()
        to_where = move_disk_to(from_where)
        top_disk = pyramids[from_where - 1].remove_top_disk()
        pyramids[to_where-1].add_top_disk(top_disk)
        draw_pyramids()
        print_bases()
        moves += 1
    if play_again():
        continue
    else:
        print("\nThank you for playing. Good bye.\n")
        break
