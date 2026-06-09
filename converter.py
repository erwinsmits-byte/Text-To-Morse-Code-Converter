# Maps supported characters to their Morse code representations
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '!': '-.-.--',
    ':': '---...', ';': '-.-.-.', '"': '.-..-.',
    "'": '.----.', '@': '.--.-.', '&': '.-...'
}

MORSE_TO_TEXT_DICT = {
    value: key
    for key, value in MORSE_CODE_DICT.items()
}

def text_to_morse(text: str) -> str | None:
    """Convert text to Morse code.

    Returns:
        str: Text to Morse code translation.
        None: If unsupported characters are found.
    """
    invalid_chars = []
    morse_words = []

    for word in text.split():
        morse_chars = []

        for char in word:
            if char in MORSE_CODE_DICT:
                morse_chars.append(MORSE_CODE_DICT[char])
            elif char not in invalid_chars:
                invalid_chars.append(char)

        morse_words.append(" ".join(morse_chars))

    if invalid_chars:
        print(
            f"\nUnsupported characters: {', '.join(invalid_chars)}. Please try again.\n"
        )
        return None

    return "   ".join(morse_words)

def morse_to_text(morse: str) -> str | None:
    """Convert Morse code to text.

    Returns:
        str: Morse code to text translation.
        None: If unsupported Morse code is found.
    """
    invalid_codes = []
    text_words = []

    for word in morse.split("   "):
        text_chars = []

        for code in word.split():
            if code in MORSE_TO_TEXT_DICT:
                text_chars.append(MORSE_TO_TEXT_DICT[code])
            elif code not in invalid_codes:
                invalid_codes.append(code)

        text_words.append("".join(text_chars))

    if invalid_codes:
        print(
            f"\nUnsupported Morse code: {', '.join(invalid_codes)}. Please try again.\n"
        )
        return None

    return " ".join(text_words)