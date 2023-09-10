# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
NAME1 = input("What is your name? \n").lower()
NAME2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


def combo_count(name_1: str, name_2: str, let: str):
    return name_1.count(let) + name_2.count(let)


def love_score(name_1: str, name_2: str):
    t = combo_count(name_1, name_2, "t")
    r = combo_count(name_1, name_2, "r")
    u = combo_count(name_1, name_2, "u")
    e = combo_count(name_1, name_2, "e")

    l = combo_count(name_1, name_2, "l")
    o = combo_count(name_1, name_2, "o")
    v = combo_count(name_1, name_2, "v")

    dig_1 = t + r + u + e
    dig_2 = l + o + v + e

    return int(str(dig_1) + str(dig_2))


SCORE = love_score(NAME1, NAME2)

if SCORE < 10 or SCORE > 90:
    print(f"Your score is {SCORE}, you go together like coke and mentos.")
elif SCORE >= 40 and SCORE <= 50:
    print(f"Your score is {SCORE}, you are alright together.")
else:
    print(f"Your score is {SCORE}.")
