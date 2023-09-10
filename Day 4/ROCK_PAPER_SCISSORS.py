import os
import random
from time import sleep


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# Write your code below this line 👇


# Repeats the play procedure as long as the player does not say no to playing again.
def main():
    replay = "y"
    streak = 0
    user_wins = 0
    computer_wins = 0
    # Repeat game as long as the player says yes to replay.
    while replay == "y":
        # Establishes both picks:
        user = user_pick()
        computer = str(computer_pick(user))

        # Displays each choice:
        user_display(user)
        computer_display(computer)

        # Evaluates the winner:
        result = game_trial(user, computer)

        # update Scores:
        if result == True:
            user_wins += 1
            streak += 1
        else:
            computer_wins += 1
            streak = 0

        # Display Scores:
        sleep(1)
        print(
            f"\n{bcolors.OKBLUE}SCORES:\n",
            f"{bcolors.HEADER}You: {bcolors.OKGREEN}{user_wins}\n",
            f"{bcolors.HEADER}Computer: {bcolors.FAIL}{computer_wins}",
            sep="",
        )
        if computer_wins == 0:
            print(f"{bcolors.HEADER}Win rate: {bcolors.OKCYAN}{(1):.0%}")
        else:
            print(
                f"{bcolors.HEADER}Win rate: {bcolors.OKCYAN}{(user_wins/(user_wins+computer_wins)):.0%}"
            )
        print(f"{bcolors.HEADER}STREAK: {bcolors.WARNING}{streak}\n")

        # Proposes to play again:
        sleep(3)
        replay = input(
            f"{bcolors.OKBLUE}Play again? {bcolors.HEADER}Y for yes or N for no: {bcolors.OKCYAN}"
        ).lower()
        os.system("cls")

    # Resets color and says bye to the user:
    print(f"Thanks for playing!")
    print(bcolors.ENDC)
    sleep(1)
    os.system("cls")


# Returns a ASCII string depending on pick:
def graphical_pick(choice: str):
    rock = """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    """

    paper = """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """

    scissors = """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """

    if choice.lower() == "rock":
        return rock
    elif choice.lower() == "paper":
        return paper
    elif choice.lower() == "scissors":
        return scissors
    else:
        raise Exception(f"{choice} is not a valid entry.")


# Asks user to make a pick:
def user_pick():
    os.system("cls")
    user_pick = input(
        f"{bcolors.OKBLUE}Rock, Paper or Scissors?{bcolors.OKCYAN}\n"
    ).lower()
    os.system("cls")
    if user_pick not in ["rock", "paper", "scissors"]:
        raise Exception(f"{user_pick} is not a valid entry.")
    return user_pick


# Prompts computer to make a pick (other than user's):
def computer_pick(user_pick: str):
    possibility = ["rock", "paper", "scissors"]
    computer_pick = 0

    while computer_pick == user_pick or computer_pick == 0:
        computer_pick = possibility[random.randint(0, 2)]

    return computer_pick


# Displays user's pick:
def user_display(user_pick: str):
    os.system("cls")
    print(f"{bcolors.OKBLUE}You choose: ", end="")
    sleep(1.5)
    print(f"{bcolors.WARNING}{user_pick.capitalize()}\n{graphical_pick(user_pick)}\n\n")


# Displays computer's pick:
def computer_display(computer_pick: str):
    print(f"{bcolors.OKBLUE}Computer chooses: ", end="")
    sleep(1.5)
    print(
        f"{bcolors.WARNING}{computer_pick.capitalize()}\n{graphical_pick(computer_pick)}\n\n"
    )


# Runs a test for who won and returns a formatted string:
def game_trial(user_pick: str, computer_pick: str):
    if user_pick == "rock":
        if computer_pick == "paper":
            sleep(1.5)
            print(f"{bcolors.FAIL}YOU LOOSE!")
            return False
        else:
            sleep(1.5)
            print(f"{bcolors.OKGREEN}YOU WIN!")
            return True
    if user_pick == "paper":
        if computer_pick == "scissors":
            sleep(1.5)
            print(f"{bcolors.FAIL}YOU LOOSE!")
            return False
        else:
            sleep(1.5)
            print(f"{bcolors.OKGREEN}YOU WIN!")
            return True
    if user_pick == "scissors":
        if computer_pick == "rock":
            sleep(1.5)
            print(f"{bcolors.FAIL}YOU LOOSE!")
            return False
        else:
            sleep(1.5)
            print(f"{bcolors.OKGREEN}YOU WIN!")
            return True


main()
