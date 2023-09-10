ROW1 = ["⬜️", "️⬜️", "️⬜️"]
ROW2 = ["⬜️", "⬜️", "️⬜️"]
ROW3 = ["⬜️️", "⬜️️", "⬜️️"]
MAP = [ROW1, ROW2, ROW3]
print(f"{ROW1}\n{ROW2}\n{ROW3}")
POSITION = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
FIRST_INDEX = int(POSITION[1]) - 1
SECOND_INDEX = int(POSITION[0]) - 1

MAP[FIRST_INDEX][SECOND_INDEX] = "X"

row1 = MAP[0]

row2 = MAP[1]

row3 = MAP[2]


# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
