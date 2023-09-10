# password Generator Project
import random

LETTERS = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SYMBOLS = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the Pypassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level - Order not randomized:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# Hard Level - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
TOTAL_LEN = nr_letters + nr_symbols + nr_numbers

for _ in range(TOTAL_LEN):

    if nr_letters == 0 and nr_numbers == 0:
        random_pick = 2
    elif nr_letters == 0 and nr_symbols == 0:
        random_pick = 1
    elif nr_numbers == 0 and nr_symbols == 0:
        random_pick = 0
    elif nr_letters == 0:
        random_pick = random.randint(1, 2)
    elif nr_numbers == 0:
        possibilities = range(0, 3, 2)
        random_pick = possibilities[random.randint(0, 1)]
    elif nr_symbols == 0:
        random_pick = random.randint(0, 1)
    else:
        random_pick = random.randint(0, 2)

    if random_pick == 0:
        password += LETTERS[random.randint(0, len(LETTERS) - 1)]
        nr_letters -= 1
    if random_pick == 1:
        password += NUMBERS[random.randint(0, len(NUMBERS) - 1)]
        nr_numbers -= 1
    if random_pick == 2:
        password += SYMBOLS[random.randint(0, len(SYMBOLS) - 1)]
        nr_symbols -= 1

print(password)