"""
Morse Code Converter

Converts text to Morse code and Morse code to text.
Supports letters, digits, and common punctuation.
"""

from logo import logo
from converter import text_to_morse, morse_to_text

def handle_text_conversion():
    text = input(
        "\nPlease enter text to convert to Morse code\n"
    ).strip().upper()

    if not text:
        print("Please enter some text.\n")
        return

    result = text_to_morse(text)

    if result is not None:
        print("\nText converted to Morse code:\n")
        print(result)
        print()

def handle_morse_conversion():
    morse = input(
        "\nPlease enter Morse code to convert to text "
        "(or type 'QUIT' to exit):\n"
    ).strip().upper()

    if not morse:
        print("Please enter some Morse code.\n")
        return

    result = morse_to_text(morse)

    if result is not None:
        print("\nMorse code converted to text:\n")
        print(result)
        print()

def main():
    logo()

    while True:
        morse_or_text = input("Please make a choice:\n1 - Text to Morse\n2 - Morse to Text\nQ - Quit\n").upper()

        if morse_or_text == "1":
            handle_text_conversion()

        elif morse_or_text == "2":
            handle_morse_conversion()

        elif morse_or_text == "Q":
            print("\nThank you for using Morse Code Converter. Goodbye!")
            break

        else:
            print("\nInvalid input, choose option '1' or '2'. Please try again.\n")

if __name__ == "__main__":
    main()
