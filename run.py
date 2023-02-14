"""Tower of Hanoi"""

# https://rich.readthedocs.io/en/latest/console.html#justify-alignment
# from rich.console import Console

# Rules taken from Wikipedia


def welcome():
    """
    This function welcomes the user and explains the rules.
    """
    print("""
Welcome to the Towers of Hanoi!

Your goal is to move the disks from the first base to the last base.

Rules:

1. Only one disk may be moved at a time.
2. Each move consists of taking the uppermost disk from one of the stacks
   and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a disk that is smaller than itself.

How to play:

1. Indicate the stack from which you want to move the uppermost disk.
2. Indicate the stack on which you want to place the chosen disk.

Good luck!\n""")


def validate_number(num):
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 3 and 6.
    """
    try:
        num = int(num)
        if num >= 3 and num <= 6:
            print("Input is valid.")
        else:
            print("You didn't choose a number between 3 and 6. Try again.\n")
            return False
    except ValueError as error:
        print(f"Invalid data: {error}. You did not choose a number.\n")
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
        disks = input("""Choose a number between 3 and 6.\n""")

        if validate_number(disks):
            print(f"The chosen number of disks is {disks}.\n")
            break

    return int(disks)


class Pyramid:
    """
    Represents a full pyramid of the given number of disks.
    """

    def __init__(self, height: int) -> None:

        # This makes a list of number from 0 to height -1
        # https://pythonexamples.org/python-convert-range-into-a-list/
        self.__list_of_disks = list(range(height))

    def draw(self) -> None:
        """
        Draws the pyramid.
        """
        # 1st pyramid
        for i in self.__list_of_disks:
            disk = (10-2*i)*" " + (4*i + 3) * \
                str(i) + (10-2*i)*" "
            print(disk)
        print(BASE*"=")

    def remove_top_disk(self) -> int:
        """
        Removes the uppermost disk.
        Raises exception when the pyramid is empty.
        """
        if self.is_empty():
            raise Exception("Cannot take a disk from an empty pyramid.")
        return self.__list_of_disks.pop(0)

    def can_place_disk(self, disk: int) -> bool:
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

    def is_empty(self) -> bool:
        """
        Tells if the pyramid is empty.
        """
        if len(self.__list_of_disks) == 0:
            return True
        else:
            return False


def print_bases():
    """
    Prints the pyramid bases.
    """
    # print(BASE*"=" + 1*" " + BASE*"=" + 1*" " + BASE*"=")
    print(71*"-", " \n")


def validate_tower_number_from(num: int) -> bool:
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It checks - !in the future! - if the tower is not empty
    """
    if not (num >= 1 and num <= 3):
        print("You didn't choose a number between 1 and 3. Try again.\n")
        return False
    if pyramids[num - 1].is_empty():
        print("There is no disk in the chosen pyramid.")
        return False
    print("Input is valid.")
    return True


def move_disk_from() -> int:
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It validates - NOT YET - if there is no disk smaller than the chosen one
    """
    print("Choose the tower from which you want to move the uppermost disk.")
    while True:
        src = int(input("Choose number 1, 2 or 3.\n"))
        if validate_tower_number_from(src):
            print(f"""You are moving the uppermost disk from tower
number {src}.\n""")
            break

    return src


def validate_tower_number_to(dst: int, src: int) -> bool:
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It checks - NOT YET - if the uppermost disk is not bigger than the disk on the chosen stack.
    It checks if the user didn't choose the same tower.
    """
    if not (dst >= 1 and dst <= 3):
        print("You didn't choose a number between 1 and 3. Try again.")
        return False

    if dst == src:
        print("You can not choose the same tower.")
        return False

    if pyramids[dst-1].can_place_disk(pyramids[src - 1].get_top_disk()):
        print("You can move the disk.")
        return True

    print("You can't place a bigger disk on a smaller one.")
    return False


def move_disk_to(src: int) -> int:
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It validates (NOT YET) if there is no disk smaller than the chosen one
    It validates if the the user didn't chose the same tower
    """
    print("Choose the tower where you want to place the chosen disk.")
    while True:
        dst = int(input("Choose number 1, 2 or 3.\n"))
        if validate_tower_number_to(dst, src):
            print("You are moving the chosen disk from tower number "
                  f"{src} to tower number {dst}.\n")
            break

    return dst


welcome()
BASE = int(23)
disks = choose_difficulty()
pyramids = [Pyramid(disks), Pyramid(0), Pyramid(0)]
pyramids[0].draw()
moves = 0
while True:
    from_where = move_disk_from()
    to_where = move_disk_to(from_where)
    top_disk = pyramids[from_where - 1].remove_top_disk()
    # for pyramid in pyramids:
    #     pyramid.draw()
    pyramids[to_where-1].add_top_disk(top_disk)
    for pyramid in pyramids:
        pyramid.draw()
    moves = +1



