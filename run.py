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

1. Only one shape maybe be moved at a time.
2. Each move consists of taking the uppermost shape from one of the stacks
   and placing it on top of another stack or on an empty rod.
3. No shape may be placed on top of a disk that is smaller than itself.

How to play:

1. Indicate the stack from which you want to move the uppermost shape.
2. Indicate the stack on which you want to place the uppermost shape.

Good luck!\n""")


welcome()
