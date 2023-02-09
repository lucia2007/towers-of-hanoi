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
    It checks if the number is between 3 and 8.
    """
    try:
        num = int(num)
        if num >= 3 and num <= 8:
            print("Input is valid.")
        else:
            print("You didn't choose a number between 3 and 8. Try again.\n")
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
        disks = input("""Choose a number between 3 and 8.\n""")

        if validate_number(disks):
            print(f"The chosen number of disks is {disks}.")
            break

    return disks

disks = choose_difficulty()

def draw_disks():
    print(12*" ", 1*"#") 
    print(11*" ", 3*"#") 
    print(10*" ", 5*"#") 
    print(8*" ", 9*"#") 
    print(6*" ", 13*"#") 
    print(4*" ", 17*"#") 
    print(2*" ", 21*"#")
    print(1*" ", 23*"#", 1*" ", 23*"#", 1*" ", 23*"#")
    print(79*"_", " \n")


draw_disks()

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
