import os
from time import sleep
import art


def main():
    clear_screen()
    print(art.logo)
    print("BLIND AUCTION! WELCOME!")
    sleep(3)

    users_left = True

    bid_dictionary = {}

    while users_left:
        clear_screen()
        bid_dictionary = user_input(bid_dictionary)
        users_left = users_left_input()

    clear_screen()
    highest_bid_user, highest_bid_amount = return_highest_bid(bid_dictionary)
    result_presentation(highest_bid_user, highest_bid_amount)
    sleep(3)
    clear_screen()


def user_input(bid_dictionary):
    user_name = input(f"Enter your name:\n")
    user_bid = int(input(f"Enter your bid:\n$"))
    bid_dictionary[user_name] = user_bid
    return bid_dictionary


def users_left_input():
    users_left_input = input(
        "Are there any users left? Yes for yes, No for no.\n"
    ).lower()

    if users_left_input == "yes":
        users_left = True
    else:
        users_left = False

    return users_left


def return_highest_bid(dictionary):
    highest_bid = 0
    highest_user = "Null"
    for user in dictionary:
        if dictionary[user] > highest_bid:
            highest_bid = dictionary[user]
            highest_user = user

    return highest_user, highest_bid


def result_presentation(user, high_bid):
    print(f"The highest bid was done by {user} at ${high_bid}!")


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


main()
