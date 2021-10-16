"""
name: tab_generator.py
author: Uzo Ukekwe
version: python 3.8
purpose: generates bass tabs from input file
"""

import os.path
import sys
import time

strings = ["E", "A", "D", "G"]    # string names on 4-string bass


def file_error(message):
    """
    Print message about file format error and quit
    :param message: specifics of file error
    """
    print("INVALID FILE FORMAT: " + message)
    time.sleep(5)
    sys.exit()


def char_split(string):
    """
    Split string into list of individual characters
    (empty delimiter, no space requirement between chars)
    :param string: string to split
    :return: list of chars in string
    """
    return [char for char in string]


def parse_file(file_name):
    """
    Parse input file to retrieve string letters and fret numbers
    :param file_name: name of file containing StringLetterFretNumber units
    :return: list of input file tokens
    """
    input_tokens = []

    with open(file_name) as file:
        for line in file:
            need_letter = True
            need_number = False
            sequence = char_split(line.strip())
            while len(sequence) > 0:
                token = sequence.pop(0)

                if need_letter and token in strings:
                    input_tokens.append(token)
                    need_letter = False
                    need_number = True
                elif need_letter and token.isspace():
                    input_tokens.append("-")
                elif need_letter and token not in strings:
                    file_error("only case-sensitive E A D or G strings accepted")
                elif need_number:
                    if not token.isdigit():
                        file_error("missing fret number in sequence")

                    # account for double digit fret numbers
                    if len(sequence) >= 1 and sequence[0].isdigit():
                        token += sequence.pop(0)
                    if int(token) > 20 or int(token) < 0:
                        file_error("fret number out of bounds (0-20 inclusive)")

                    input_tokens.append(token)
                    need_letter = True
                    need_number = False
            if need_number:
                file_error("missing final fret number on line")

    return input_tokens


def make_note_lists(all_notes):
    """
    Transfer fret numbers/rests to appropriate lists
    :param all_notes: input file tokens
    :return: list of all strings, each containing a list of their chosen frets
    """
    e_notes = []
    a_notes = []
    d_notes = []
    g_notes = []
    note_lists = [e_notes, a_notes, d_notes, g_notes]

    while len(all_notes) > 0:
        token = all_notes.pop(0)
        if token == "E":
            fret = all_notes.pop(0)
            e_notes.append(fret)
            a_notes.append("-" * len(fret))
            d_notes.append("-" * len(fret))
            g_notes.append("-" * len(fret))
        elif token == "A":
            fret = all_notes.pop(0)
            a_notes.append(fret)
            e_notes.append("-" * len(fret))
            d_notes.append("-" * len(fret))
            g_notes.append("-" * len(fret))
        elif token == "D":
            fret = all_notes.pop(0)
            d_notes.append(fret)
            e_notes.append("-" * len(fret))
            a_notes.append("-" * len(fret))
            g_notes.append("-" * len(fret))
        elif token == "G":
            fret = all_notes.pop(0)
            g_notes.append(fret)
            e_notes.append("-" * len(fret))
            a_notes.append("-" * len(fret))
            d_notes.append("-" * len(fret))
        elif token == "-":
            for note_list in note_lists:
                note_list.append("-")

    return note_lists


def make_tab():
    """
    User creates their own tab
    """
    file_name = input("Enter the name of your file of string letter-fret number sequences: ")
    while not os.path.exists(file_name):
        file_name = input("Enter a valid file in this directory: ")

    input_tokens = parse_file(file_name)
    note_lists = make_note_lists(input_tokens)

    artist = input("Enter artist's name: ")
    song = input("Enter song's title: ")
    print("\n%s - %s Bass Tab" % (artist, song))

    # print all the notes without going beyond the character per line limit
    while len(note_lists[0]) > 0:
        output_line4 = ["E| "]
        output_line3 = ["A| "]
        output_line2 = ["D| "]
        output_line1 = ["G| "]
        i = 0
        while i < 120:
            output_line1.append(note_lists[3].pop(0))
            output_line2.append(note_lists[2].pop(0))
            output_line3.append(note_lists[1].pop(0))
            output_line4.append(note_lists[0].pop(0))
            if len(note_lists[0]) == 0:
                break
            i += 1
        print("".join(output_line1))
        print("".join(output_line2))
        print("".join(output_line3))
        print("".join(output_line4))
        print()

    new_tab = input("Would you like to make a new tab? (Y/N) ")
    return False if new_tab != "Y" else True


def main():
    """
    Create bass tabs while the program runs
    """
    print("〜♫ Bass Tab Generator ♫〜\n")
    print("file format = StringLetterFretNumber with any number of spaces between each unit\n"
          "(ex. E4   G5 A0A0A0 D1)\n")

    still_going = True
    while still_going:
        still_going = make_tab()


if __name__ == "__main__":
    main()
