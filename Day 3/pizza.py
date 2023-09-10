# This code works out the final bill for a pizza after the user inputs different parameters

print("Welcome to Python Pizza Deliveries!")
SIZE = input("What size pizza do you want? S, M, or L ")
ADD_PEPPERONI = input("Do you want pepperoni? Y or N ")
EXTRA_CHEESE = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


def pizza_bill(pizza_size: str, pizza_pepperoni: str, pizza_cheese: str):
    bill = 0

    if pizza_size == "S":
        bill += 15

        if pizza_pepperoni == "Y":
            bill += 2

    elif pizza_size == "M":
        bill += 20

        if pizza_pepperoni == "Y":
            bill += 3

    else:
        bill += 25

        if pizza_pepperoni == "Y":
            bill += 3

    if pizza_cheese == "Y":
        bill += 1

    return bill


print(f"Your final bill is: ${pizza_bill(SIZE,ADD_PEPPERONI,EXTRA_CHEESE)}.")
