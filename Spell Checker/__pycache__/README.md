🪄 Spell Checker (Python)

A simple command-line Spell Checker built in Python using the pyspellchecker
 library.
It reads user input, checks each word, and returns a corrected version of the text — all from your terminal.

🚀 Features

Checks spelling for each word in a sentence

Suggests the most likely correction automatically

Preserves words it can’t recognize

Simple command-line interface (type and correct instantly)

🧰 Requirements

Python 3.8 or above

pyspellchecker library

Install dependencies with:

pip install pyspellchecker

📜 Usage

Clone this repository:

git clone https://github.com/samriddhsaxena/mini-projects.git
cd "mini-projects/Spell Checker"

Run the script:

python main.py


Type any sentence to check spelling.
Type exit to quit.

Example:

--------Spell Checker-----
Enter text: I am lernig Pythn
Corrected text: I am learning Python

Enter text: exit
Goodbye!

🧠 How It Works

Uses the SpellChecker class from pyspellchecker

Splits user input into words

Corrects each word using spell.correction()

If no correction is found, keeps the original word

Joins the words back into a sentence and prints the result

🧑‍💻 Author

Samriddh Saxena
📧 samriddhsaxena@gmail.com


🪶 License

This project is licensed under the MIT License.