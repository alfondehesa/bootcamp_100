import os
import random
from time import sleep
import hangman_resources


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


def main():
    play_again = "y"

    while play_again == "y":
        word, score, win_condition, mistake, guess, guesses = init()

        while win_condition == False and mistake < 6:
            # Prints the current 'score' (list of blanks and letters), then prints a ASCII hanged man based on the amount of errors, then gives a message of the amount of letters based guessed based on the previous guess.
            display(word, score, guess, mistake, guesses)

            # Prompts the user to make new guess.
            guess = input(f"{bcolors.OKBLUE}Enter a letter: {bcolors.OKCYAN}").upper()

            # Checks if guess is viable (if already guessed or not a letter)
            if not guess.isalpha():
                os.system("cls")
                print(f"{bcolors.FAIL}{guess} is not a valid character, try again!")
                sleep(2)
                guess = 0
                os.system("cls")
                continue
            elif len(guess) > 1:
                os.system("cls")
                print(f"{bcolors.FAIL}{guess} has more than one character, try again!")
                sleep(2)
                guess = 0
                os.system("cls")
                continue
            elif guess in guesses:
                os.system("cls")
                print(f"{bcolors.FAIL}You have already guessed {guess}, try again!")
                sleep(2)
                guess = 0
                os.system("cls")
                continue
            else:
                guesses.append(guess)

            # Updates the score string and the amount of mistakes.
            score, mistake = update_score(str(guess), score, word, mistake)

            # Checks if we have won or lost.
            win_condition = check_win(score, mistake, word)

        os.system("cls")
        play_again = input(
            f"{bcolors.OKBLUE}Play again? Y for yes, N for no:\n{bcolors.OKCYAN}"
        ).lower()
        os.system("cls")

    print(f"{bcolors.OKBLUE}Thanks for playing!{bcolors.ENDC}")
    sleep(2)
    os.system("cls")


def init():
    os.system("cls")
    print(f"{bcolors.WARNING}{hangman_resources.logo}")
    print(f"{bcolors.OKBLUE}Welcome to Hangman!")
    sleep(2)
    os.system("cls")

    win_condition = False
    mistake = 0
    word, score = random_word()
    guess = 0
    guesses = []

    return word, score, win_condition, mistake, guess, guesses


def display(word, score, guess, mistake, guesses):
    os.system("cls")
    delimiter = " "
    print(f"{bcolors.HEADER}{delimiter.join(score)}")
    print(f"{bcolors.WARNING}{hangman_resources.stages[mistake]}")
    if guess == 0:
        print(f"")
    elif guess in word:
        print(
            f"{bcolors.OKGREEN}Success! There are {word.count(guess)} {guess}s in the word!"
        )
    else:
        print(f"{bcolors.FAIL}Oh no! There are no {guess}s in this word.")

    print(
        f"\n{bcolors.OKBLUE}Already guessed: {bcolors.OKCYAN}{delimiter.join(guesses)}"
    )


def random_word():
    word = list(
        hangman_resources.word_list[
            random.randint(0, len(hangman_resources.word_list) - 1)
        ].upper()
    )
    score = [""]

    counter = 0
    while counter != len(word):
        score.append("_")
        counter += 1

    score = score[1:]

    return word, score


def update_score(guess: str, score, word, mistake):
    new_mistake = 1

    for position in range(len(word)):
        if guess == word[position]:
            score[position] = guess
            new_mistake = 0

    mistake += new_mistake

    return score, mistake


def check_win(score, mistake, word):
    win_condition = False

    if not "_" in score:
        delimiter = " "
        os.system("cls")
        print(f"{bcolors.OKGREEN}{delimiter.join(word)}")
        print(f"{bcolors.OKGREEN}{hangman_resources.win}")
        print(f"{bcolors.OKGREEN}CONGRATULATIONS!!! YOU WIN!!!")
        sleep(3.5)
        win_condition = True
        os.system("cls")
    elif not (mistake < 6):
        delimiter = " "
        os.system("cls")
        print(f"{bcolors.FAIL}{delimiter.join(word)}")
        print(f"{bcolors.FAIL}{hangman_resources.stages[mistake]}")
        print(f"{bcolors.FAIL}GAME OVER, YOU LOST!")
        sleep(3.5)
        os.system("cls")

    return win_condition


main()
