#!/usr/bin/python3
"""text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text: text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    txt = 0
    while txt < len(text) and text[txt] == ' ':
        txt += 1

    while txt < len(text):
        print(text[txt], end="")
        if text[txt] == "\n" or text[txt] in ".?:":
            if text[txt] in ".?:":
                print("\n")
            txt += 1
            while txt < len(text) and text[txt] == ' ':
                txt += 1
            continue
        txt += 1

