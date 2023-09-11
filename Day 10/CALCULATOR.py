import os
from time import sleep
import art


def main():
    """Command line based calculator. Supports multiple sequential operations."""

    # Function to clear the screen
    clear_screen()

    # Function to initialize the calculator
    init()

    # Flag to restart the calculator
    operation_restart = True

    while operation_restart:
        # Initialize the recorded value
        ans = ""

        # Flag to continue with the following operation
        operation_continue = True

        while operation_continue:
            clear_screen()
            print(art.logo)
            # Check if this is not the first operation. If so, print the result from previous operation
            if not type(ans) == str:
                print(f"ANS = {ans}\n")

            # Prompt the user for the operation choice
            operation_choice = input(
                "What operation would you like to perform? '+' or sum, '-' for subtract, '*' for multiply, '/' for divide, 'q' to quit.\n"
            )

            # Check if the operation choice is valid
            if not (
                operation_choice == "+"
                or operation_choice == "-"
                or operation_choice == "*"
                or operation_choice == "/"
                or operation_choice == "q"
            ):
                print(f"WARNING: {operation_choice} is not a valid choice. Try again.")
                sleep(1.5)
                continue

            # If user selects to quit, set flag to close calculator
            elif operation_choice == "q":
                operation_restart = False
                break

            # If the ans exists (an operation has already happened and we are continuing), use it as the first number
            if type(ans) == str:
                num_1, num_2 = user_input()
            else:
                num_1 = ans
                num_2 = float(input("Enter number: "))

            # Perform the operation
            result = operation(operation_choice, num_1, num_2)

            # If user has tried to divide by 0, return an error and restart current operation
            if result == "0div":
                print(f"WARNING: Cannot divide by 0. Restarting...")
                sleep(1.5)
                continue

            # Update the ans with the result
            ans = result

            print(f"\nYour result is: {result}")

            # Prompt the user to continue or start a new operation
            continue_choice = input(
                f"\nWould you like to continue with the operation? 'y' to continue, 'n' for a new operation, 'q' to quit.\n"
            ).lower()

            # If user wants to continue, flag this operation to re-run
            if continue_choice == "y":
                operation_continue = True

            # If the user wants a new operation, flag this operation to stop, but the calculator to still run
            elif continue_choice == "n":
                operation_continue = False

            # Otherwise, flag the calculator to stop
            else:
                operation_continue = False
                operation_restart = False

    # Say bye!
    clear_screen()
    print("Goodbye!")
    sleep(1.5)
    clear_screen()


def operation(choice, num_1, num_2):
    """Performs a mathematical operation based on inputs.

    Args:
        choice (str): Type of operation, "+", "-", "*" or "/".
        num_1 (float): First number.
        num_2 (float): Second number.

    Returns:
        float: Operation result ("0div" if number 2 is 0 and operation is division).
    """
    # Perform the selected operation
    if choice == "+":
        result = add(num_1, num_2)
    elif choice == "-":
        result = subtract(num_1, num_2)
    elif choice == "*":
        result = multiply(num_1, num_2)
    elif choice == "/":
        result = divide(num_1, num_2)
        if result == False:
            result = "0div"
    else:
        result = ""

    return result


def init():
    """Gives welcome print."""
    # Function to initialize the calculator
    print(art.logo)
    print("Welcome to the calculator!\n")
    sleep(3)


def user_input():
    """Prompts user to input 2 numbers.

    Returns:
        float: 1st number, 2nd number.
    """
    # Function to get user input for two numbers
    num_1 = float(input("\nEnter number 1: "))
    num_2 = float(input("Enter number 2: "))
    return num_1, num_2


def add(number_1, number_2):
    """Adds 2 numbers.

    Args:
        number_1 (float): 1st Number.
        number_2 (float): 2nd Number.

    Returns:
        float: Result of addition.
    """
    # Function to add two numbers
    summation = number_1 + number_2
    return summation


def subtract(number_1, number_2):
    """Subtracts 2 numbers.

    Args:
        number_1 (float): 1st Number.
        number_2 (float): 2nd Number.

    Returns:
        float: Result of subtraction.
    """
    # Function to subtract two numbers
    subtraction = number_1 - number_2
    return subtraction


def multiply(number_1, number_2):
    """Multiplies 2 numbers.

    Args:
        number_1 (float): 1st Number.
        number_2 (float): 2nd Number.

    Returns:
        float: Result of multiplication.
    """
    # Function to multiply two numbers
    multiplication = number_1 * number_2
    return multiplication


def divide(number_1, number_2):
    """Divides 2 numbers.

    Args:
        number_1 (float): 1st Number.
        number_2 (float): 2nd Number.

    Returns:
        float: Result of division.
    """
    # Function to divide two numbers
    if number_2 == 0:
        return False

    division = number_1 / number_2
    return division


def clear_screen():
    """Clears screen"""
    # Function to clear the screen
    os.system("cls" if os.name == "nt" else "clear")


# Call the main function to start the calculator
main()
