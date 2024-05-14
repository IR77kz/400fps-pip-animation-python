import random

__letters = ">><"
__under = "-"

def generate(length, e_chance: int = 2, under_chance: int = 15):
    new = ""
    choice = __letters[0]
    for i in range(length+1):
        new+=choice
        if random.randint(1, 100) <= under_chance:
            choice = __under
        elif random.randint(1, 100) <= e_chance:
            choice = random.choice(__letters)

    return new