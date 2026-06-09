Morse Code Converter

A Python command-line application that converts plain text to Morse code and Morse code back to plain text.

This project was built as part of my Python learning journey and focuses on user input validation, dictionary lookups, modular code design, and bidirectional data conversion.

Features
Convert text to Morse code
Convert Morse code to text
Support for:
Letters (A-Z)
Numbers (0-9)
Common punctuation
Preserves word boundaries during conversion
Detects and reports unsupported characters
Menu-driven command-line interface
Modular design with separate conversion logic and user interaction
Example Usage
Text to Morse

Input:

HELLO WORLD

Output:

.... . .-.. .-.. --- .-- --- .-. .-.. -..

Morse to Text

Input:

.... . .-.. .-.. --- .-- --- .-. .-.. -..

Output:

HELLO WORLD

Installation

Clone the repository:

git clone https://github.com/erwinsmits-byte/Text-To-Morse-Code-Converter.git

Navigate to the project directory:

cd morse-code-converter

Run the application:

python main.py
Project Structure
morse-code-converter/
│
├── main.py          # User interface and menu system
├── converter.py     # Morse conversion logic
├── logo.py          # ASCII art logo
└── README.md
Supported Characters

Letters:

A-Z

Numbers:

0-9

Punctuation:

, . ? / - ( ) ! : ; " ' @ &
What I Learned

While building this project, I gained experience with:

Dictionaries and dictionary comprehensions
Input validation
Error handling
String manipulation
Refactoring and code organization
Separating business logic from user interface logic
Designing reversible data transformations
Debugging edge cases involving word separation

One particularly interesting challenge was correctly preserving spaces between words when converting Morse code back into text. Solving this required rethinking how Morse code words were represented and parsed.

Future Improvements

Potential enhancements include:

Unit tests using pytest
Audio playback of Morse code
Graphical user interface (GUI)
File import/export support
Additional Morse code symbols
Exception-based error handling
