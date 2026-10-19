#!/usr/bin/python3
"""
Defines a text indentation function.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.
    There should be no space at the beginning or at the end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    chars = ['.', '?', ':']
    line = ""
    while i < len(text):
        line += text[i]
        if text[i] in chars:
            print(line.strip())
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            line = ""
            continue
        i += 1

    if line:
        print(line.strip(), end="")
