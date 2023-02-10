"""Tower of Hanoi"""


# Rules taken from Wikipedia


def welcome():
    """
    This function welcomes the user and explains the rules.
    """
    print("""
Welcome to the Towers of Hanoi!

Your goal is to move the disks from the first stack to the last stack.

Rules:

1. Only one disk may be moved at a time.
2. Each move consists of taking the uppermost disk from one of the stacks
   and placing it on top of another stack or on an empty rod.
3. No disk may be placed on top of a disk that is smaller than itself.

How to play:

1. Indicate the stack from which you want to move the uppermost disk.
2. Indicate the stack on which you want to place the chosen disk.

Good luck!\n""")


welcome()


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

    return disks


disks = choose_difficulty()

PLATFORM = int(23)
DISK1LEN = int(23)
DISK2LEN = int(19)
DISK3LEN = int(15)
DISK4LEN = int(11)
DISK5LEN = int(7)
DISK6LEN = int(3)

DISK1 = (round((PLATFORM - DISK1LEN)/2)+1)*" " + DISK1LEN*"#" + (round((PLATFORM - DISK2LEN)/2)+1)*" "
DISK2 = (round((PLATFORM - DISK2LEN)/2)+1)*" " + DISK2LEN*"#" + (round((PLATFORM - DISK2LEN)/2)+1)*" "
DISK3 = (round((PLATFORM - DISK3LEN)/2)+1)*" " + DISK3LEN*"#" + (round((PLATFORM - DISK3LEN)/2)+1)*" "
DISK4 = (round((PLATFORM - DISK4LEN)/2)+1)*" " + DISK4LEN*"#" + (round((PLATFORM - DISK4LEN)/2)+1)*" "
DISK5 = (round((PLATFORM - DISK5LEN)/2)+1)*" " + DISK5LEN*"#" + (round((PLATFORM - DISK5LEN)/2)+1)*" "
DISK6 = (round((PLATFORM - DISK6LEN)/2)+1)*" " + DISK6LEN*"#" + (round((PLATFORM - DISK6LEN)/2)+1)*" "


LISTOFDISKS = [DISK6*3, DISK5*3, DISK4*3, DISK3*3, DISK2*3, DISK1*3]

# class Pyradmids():
#     """
#     This class will be used for drawing and redrawing the number of disks.
#     """


def draw_disks(num):
    """
    Draw.
    """
    for disk in LISTOFDISKS:
        print(disk)
    # print((round((PLATFORM - DISK6LEN)/2)+1)*" ", DISK6LEN*"#", (round((PLATFORM - DISK6LEN)/2)+1)*" ")
    # print((round((PLATFORM - DISK5LEN)/2)+1)*" ", DISK5LEN*"#", (round((PLATFORM - DISK5LEN)/2)+1)*" ")
    # print((round((PLATFORM - DISK4LEN)/2)+1)*" ", DISK4LEN*"#", (round((PLATFORM - DISK4LEN)/2)+1)*" ")
    # print((round((PLATFORM - DISK3LEN)/2)+1)*" ", DISK3LEN*"#", (round((PLATFORM - DISK3LEN)/2)+1)*" ")
    # print((round((PLATFORM - DISK2LEN)/2)+1)*" ", DISK2LEN*"#", (round((PLATFORM - DISK2LEN)/2)+1)*" ")
    # print((round((PLATFORM - DISK1LEN)/2)+1)*" ", DISK1LEN*"#", (round((PLATFORM - DISK2LEN)/2)+1)*" ")
    print(1*" " + PLATFORM*"=" + 1*" " + PLATFORM*"=" + 1*" " + PLATFORM*"=")
    print(79*"-", " \n")


draw_disks(disks)


def validate_tower_number(num):
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It checks - !in the future! - if the tower is not empty
    """
    try:
        num = int(num)
        if num >= 1 and num <= 3:
            print("Input is valid.")
        else:
            print("You didn't choose a number between 1 and 3. Try again.\n")
            return False
    except ValueError as error:
        print(f"Invalid data: {error}. You did not choose a number.")
        return False
    return True


def move_disk_from():
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It validates - NOT YET - if there is no disk smaller than the chosen one
    """
    print("Choose the tower from which you want to move the uppermost disk.")
    while True:
        from_where = input("Choose number 1, 2 or 3.\n")
        if validate_tower_number(from_where):
            print(f"""You are moving the uppermost disk from tower 
number {from_where}.\n""")
            break

    return from_where


from_where = (move_disk_from())


def validate_tower_number_to(num1, num2):
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It checks - NOT YET - if the tower is not empty
    It checks if the user didn't choose the same tower
    """
    try:
        num1 = int(num1)
        num2 = int(num2)
        if num1 >= 1 and num1 <= 3:
            if num1 != num2:
                print("Input is valid.")
            else:
                print("You can not choose the same tower.")
                return False
        else:
            print("You didn't choose a number between 1 and 3. Try again.")
            return False
    except ValueError as error:
        print(f"Invalid data: {error}. You did not choose a number.")
        return False
    return True


def move_disk_to():
    """
    This function validates if a number was chosen as opposed to a string.
    It checks if the number is between 1 and 3.
    It validates (NOT YET) if there is no disk smaller than the chosen one
    It validates if the the user didn't chose the same tower
    """
    print("Choose the tower where you want to place the chosen disk.")
    while True:
        to_where = input("Choose number 1, 2 or 3.\n")
        if validate_tower_number_to(to_where, from_where):
            print(f"""You are moving the chosen disk from tower number 
{from_where} to tower number {to_where}.""")
            break

    return to_where


to_where = move_disk_to()
