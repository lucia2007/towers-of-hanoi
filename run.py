"""Tower of Hanoi"""
# https://dev.to/muhimen123/colored-text-in-terminal-using-python-1nmd#:~:text=In%20colorama%2C%20the%20font%20color,start%20by%20importing%20the%20module.&text=Then%2C%20in%20the%20print%20statement,Just%20like%20this.
from time import sleep
import time
import sys
import random
import os
import colorama
colorama.init()
# https://www.geeksforgeeks.org/clear-screen-python/
# https://stackoverflow.com/questions/15375368/slow-word-by-word-terminal-printing-in-python
# https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=You%20can%20use%20Python's%20sleep,pauses%20between%20words%20or%20graphics.
# https://rich.readthedocs.io/en/latest/console.html#justify-alignment
# from rich.console import Console

# Rules taken from Wikipedia


def print_logo() -> None:
    """
    Prints logo. The ASCII logo was generated using the link below.
    https://patorjk.com/software/taag/#p=display&h=2&f=Big&t=Towers%20of%20Hanoi
    """
    print(r"""
 _______                                  __   _    _                   _
|__   __|                                / _| | |  | |                 (_)
   | | _____      _____ _ __ ___    ___ | |_  | |__| | __ _ _ __   ___  _
   | |/ _ \ \ /\ / / _ \ '__/ __|  / _ \|  _| |  __  |/ _` | '_ \ / _ \| |
   | | (_) \ V  V /  __/ |  \__ \ | (_) | |   | |  | | (_| | | | | (_) | |
   |_|\___/ \_/\_/ \___|_|  |___/  \___/|_|   |_|  |_|\__,_|_| |_|\___/|_|
""")


def slow_print(text) -> None:
    """
    Prints the text slowly, letter by letter.
    https://stackoverflow.com/questions/15375368/slow-word-by-word-terminal-printing-in-python
    """
    for word in text + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()  # defeat buffering
        time.sleep(random.random() * 0.05)


def welcome() -> None:
    """
    This function welcomes the user and explains the rules.
    The text is printed slowly.
    """
    print_logo()
    welcome_text = """
Welcome to the Towers of Hanoi!

Your goal is to move all the disks from the first base to the last base.

Rules:

1. Move the top disk from one of the bases.
2. Place it on an empty base or on other disks on a different base.
3. You may not place the chosen disk on top of a smaller disk.

How to play:

1. Choose the base (# 1, 2, 3) FROM WHICH you want to move the top disk.
2. Choose the base (# 1, 2, 3) ON WHICH you want to place the chosen disk.

Good luck!\n"""

    slow_print(welcome_text)


def validate_number(height_input: str) -> bool:
    """
    This function validates if a number was chosen as opposed to a string.
    It also checks if the number is between 3 and 6.
    """
    try:
        height = int(height_input)
    except ValueError as error:
        print_red(f"Invalid data: {error}. You did not choose a number.\n")
        return False

    if 3 <= height <= 6:
        return True
    print_red("You didn't choose a number between 3 and 6. Try again.\n")
    return False


def choose_difficulty() -> int:
    """
    The user chooses the level of difficulty. The higher the number, the more
    difficult the game. The input is validated.
    The function returns the number of disks the user wants to use.
    """
    sleep(1)
    print("""How many disks do you want to play with? The more disks, the more
difficult the game.
""")

    while True:
        sleep(1)
        num_input = input("Choose a number between 3 and 6.\n\n")

        if validate_number(num_input):
            break

    return int(num_input)


def print_red(message: str) -> None:
    """"
    Prints text in red.
    """
    print(colorama.Fore.RED + message + colorama.Fore.RESET)


class Pyramid:
    """
    Represents a full pyramid of the given number of disks.
    """

    def __init__(self, height: int) -> None:
        """
        This makes a list of numbers from 0 to (height - 1).
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

    def draw_pyramid_row(self, row: int) -> None:
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
                """You may not place a larger disk on a smaller one.
Choose another base or return it.""")
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
            return True
        return False


def winning_message(score: int, height: int) -> None:
    """
    Prints winning message and informs user about number of moves in comparison
    with minimum number of moves.
    https://patorjk.com/software/taag/#p=display&h=2&f=Big&t=You%20won%20!
    """
    # pylint: disable=anomalous-backslash-in-string
    print(r"""
__     __                                 _
\ \   / /                                | |
 \ \_/ /__  _   _  __      _____  _ __   | |
  \   / _ \| | | | \ \ /\ / / _ \| '_ \  | |
   | | (_) | |_| |  \ V  V / (_) | | | | |_|
   |_|\___/ \__,_|   \_/\_/ \___/|_| |_| (_)

""")
    if score == 2**height - 1:
        print(
            f"You used minimum number of moves which is {2**height-1}!"
            " Well done!\n")
    else:
        print(
            f"Congratulations! You used {score} moves."
            " Minimum number of moves was {2**height -1}.\n")


def validate_answer(choice: str) -> bool:
    """
    Validates if the user answered "y" or "n".
    """
    while True:
        choice = choice.upper()
        if choice == "Y" or choice == "N":
            return True
        else:
            print_red("Invalid answer. You did not choose \"Y\" or \"N\".\n")
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


def print_bases() -> None:
    """
    Prints the pyramid bases.
    """
    print(11*"-" + "1" + 11*"-" + " " + 11*"-" +
          "2" + 11*"-" + " " + 11*"-" + "3" + 11*"-" + "\n")


def validate_tower_number_from(num_input: str) -> bool:
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It checks if the tower is not empty.
    """
    try:
        num = int(num_input)
    except ValueError as error:
        print_red(f"Invalid data: {error}. You did not choose a number.\n")
        return False
    if not (1 <= num <= 3):
        print_red("You didn't choose a number between 1 and 3. Try again.\n")
        return False
    if pyramids[num - 1].is_empty():
        print_red(
            "There is no disk on the chosen base. Choose a different base.")
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
        print_red(f"Invalid data: {error}. You did not choose a number.\n")
        return False
    if not 1 <= dst <= 3:
        print_red("You didn't choose a number between 1 and 3. Try again.\n")
        return False
    if pyramids[dst-1].can_place_disk(pyramids[src - 1].get_top_disk()):
        return True
    print_red("""You can't place a bigger disk on a smaller one.
Choose another base or return it.""")
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
            break

    return int(dst)


def draw_pyramids() -> None:
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


            " Well done!\n")
    else:
        print(
            f"Congratulations! You used {score} moves."
            f" Minimum number of moves was {2**height -1}.\n")

welcome()
BASE = int(23)
while True:
    moves = 0  # pylint: disable=invalid-name
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
    winning_message(moves, disks)
    if not play_again():
        break

print("\nThank you for playing. Good bye.\n")
