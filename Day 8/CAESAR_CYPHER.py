import os
from time import sleep
import art


def main():
    redo = True

    while redo:
        clear_screen()
        init()
        user_action = user_choose_action()

        if user_action == "encode":
            user_word, desired_shift = user_choose_word_and_shift()
            encrypted_word = encrypt_word(user_word, desired_shift)
            print(f"\nThe decoded message is: '{encrypted_word}'.")

        elif user_action == "decode":
            user_word, desired_shift = user_choose_word_and_shift()
            decrypted_word = decrypt_word(user_word, desired_shift)
            print(f"\nThe decoded message is:\n{decrypted_word}")
        else:
            break

        redo_prompt = input(
            "\nWould you like to go again? Yes for yes, No to quit.\n"
        ).lower()

        if redo_prompt == "yes":
            redo = True
        else:
            redo = False

    clear_screen()
    print(art.logo)
    print('Goodbye!')
    sleep(1)
    clear_screen()


def init():
    print(art.logo)

def user_choose_action():
    user_action = input("\nWhat would you like to do? 'Encode' to encrypt, 'Decode' to decrypt, 'Quit' to quit.\n").lower()  # type: ignore
    return user_action


def user_choose_word_and_shift():
    user_word = input("\nType your message:\n")
    word_shift_amount = int(
        input("\nHow many letters would you like to shift your word by?\n")
    )
    return user_word, word_shift_amount


def encrypt_word(word, shift_amount):
    alphabet = [
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
    ]
    encrypted_alphabet = list()

    if shift_amount >= 26:
        shift_amount = shift_amount % 26

    for index, letter in enumerate(alphabet):
        if index + shift_amount > len(alphabet) - 1:
            shifted_letter_index = index + shift_amount - len(alphabet)

        else:
            shifted_letter_index = index + shift_amount

        encrypted_alphabet.append(alphabet[shifted_letter_index])

    encrypted_message = ""

    for letter in word:
        if letter.lower() in encrypted_alphabet:
            if letter.isupper():
                encrypted_message += encrypted_alphabet[
                    alphabet.index(letter.lower())
                ].upper()
            else:
                encrypted_message += encrypted_alphabet[alphabet.index(letter)]

        else:
            encrypted_message += letter

    return encrypted_message


def decrypt_word(word, shift_amount):
    alphabet = [
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
    ]
    encrypted_alphabet = list()

    if shift_amount >= 26:
        shift_amount = shift_amount % 26

    for index, letter in enumerate(alphabet):
        if index + shift_amount > len(alphabet) - 1:
            shifted_letter_index = index + shift_amount - len(alphabet)

        else:
            shifted_letter_index = index + shift_amount

        encrypted_alphabet.append(alphabet[shifted_letter_index])

    decrypted_message = ""

    for letter in word:
        if letter.lower() in encrypted_alphabet:
            if letter.isupper():
                decrypted_message += alphabet[
                    encrypted_alphabet.index(letter.lower())
                ].upper()
            else:
                decrypted_message += alphabet[encrypted_alphabet.index(letter)]

        else:
            decrypted_message += letter

    return decrypted_message


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


main()
