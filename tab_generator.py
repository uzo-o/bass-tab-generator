"""
name: tab_generator.py
author: Uzo Ukekwe
version: python 3.8
purpose: generates a variation on traditional bass tabs
"""

import random

strings = ["E", "A", "D", "G"]


def display_intro():
    """
    Print the greeting and initial instructions
    """
    print("〜♫ Bass Tab Generator ♫〜")
    print()

    print("How To Read the Tab")
    print("-----------")
    print(strings[0]+"  "+strings[1]+"  "+strings[2]+"  "+strings[3])
    print("-- -- -- --")
    print("x  |   |  | (1st note played: xth fret on E string)")
    print("|  x   |  | (2nd note played: xth fret on A string)")
    print("|  |   x  | (3rd note played: xth fret on D string)")
    print("|  |   |  | (...)")
    print("|  |   |  x (Nth note played: xth fret on G string)")

    print("\nTo use the generator, specify the note you would like to add one at a time."
          "\nThe tab will print at the end.\nShall we get started?\n")


def print_tab(numbers):
    """
    Print the finalized tab
    :param numbers: corresponding list of fret #s added to tab
    """
    title = input("\nWhat is this song called? ")
    print()
    print("♪ " + title + " Bass Tab ♪")
    print()
    print("-----------")
    print(strings[0] + "  " + strings[1] + "  " + strings[2] + "  " + strings[3])
    print("-- -- -- --")

    while len(numbers) != 0:
        i = 0
        print(numbers[i] + "  " + numbers[i + 1] + "  " + numbers[i + 2] + "  " + numbers[i + 3])
        numbers.remove(numbers[i])
        numbers.remove(numbers[i])
        numbers.remove(numbers[i])
        numbers.remove(numbers[i])


def edit_row(new_string, new_fret, letters, numbers):
    """
    Add the fret number to its appropriate string
    :param new_string: string of new note
    :param new_fret: fret of new note
    :param letters: list of strings added to tab
    :param numbers: corresponding list of fret #s added to tab
    """
    n = 0
    while n < len(strings):
        if strings[n] != new_string:
            letters.append(strings[n])
            numbers.append("-")
        else:
            letters.append(new_string)
            numbers.append(new_fret)
        n += 1


def random_mode(letters, numbers):
    """
    Create a random tab
    :param letters: list of strings added to tab
    :param numbers: corresponding list of fret #s added to tab
    """
    print("\nYou are in random mode. (Random notes will be generated. "
          "Maybe they'll inspire you?)")

    num_notes = int(input("\nHow many notes will be in this tab? "))

    # limited fret numbers to prevent too many uncommon placements
    fret_options = ["0", "1", "2", "3", "4", "5", "6", "7",
                    "8", "9", "10", "11", "12", "13", "-"]

    for i in range(num_notes):
        chosen_string = random.choice(strings)
        chosen_fret = random.choice(fret_options)
        edit_row(chosen_string, chosen_fret, letters, numbers)

    print_tab(numbers)


def manual_mode(letters, numbers):
    """
    User creates their own tab
    :param letters: list of strings added to tab
    :param numbers: corresponding list of fret #s added to tab
    """
    editing = "yes"

    while editing != "f":
        # user input
        letter_insert = input("\nInsert a string letter: ").upper()
        while letter_insert not in strings:
            letter_insert = input("Insert a string letter (Must be E, A, D, or G): ").upper()

        number_insert = str(input("Insert a fret number: "))
        while int(number_insert) > 20 or int(number_insert) < 0:
            number_insert = str(input("Insert a fret number (Must be between 0 and 20): "))

        # update letter and number lists with user input
        edit_row(letter_insert, number_insert, letters, numbers)

        editing = input("(Enter f to finalize the tab, b to add a blank row, or press any key to continue)")
        if editing == "b":
            for i in range(len(strings)):
                letters.append(strings[i])
                numbers.append("-")

    print_tab(numbers)


def main():
    """
    Create a new bass tab using random mode or manual mode
    """
    display_intro()

    mode = input("You are in manual mode. (You will enter your own notes)\n"
                 "(You can press r to switch to random mode or press any key to continue)\n")

    user_letters = []
    user_numbers = []

    if mode == "r":
        random_mode(user_letters, user_numbers)
    else:
        manual_mode(user_letters, user_numbers)


if __name__ == "__main__":
    main()
