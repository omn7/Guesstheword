from random import choice
from printf import printf
from get_guess import get_guess
from update_dashes import update_dashes
import nltk

nltk.download("words", quiet=True)

from nltk.corpus import words

words = words.words()

secret_word = choice(words).lower()

dashes = "-" * len(secret_word)
guesses_left = len(secret_word)

BRIGHT_RED = "\u001b[31;1m"
BRIGHT_GREEN = "\u001b[32;1m"

BOLD = "\033[1m"
ITALIC = "\033[3m"

RESET_ALL = "\u001b[0m"
#printf(f"{BRIGHT_GREEN}Hint:" + " Try all the vowels.\n")
while guesses_left > 0 and dashes != secret_word:
    printf(f"{dashes}\n{guesses_left} incorrect guesses left.\n")

    guess = get_guess()

    dashes = update_dashes(secret_word, dashes, guess)

    if guess in secret_word:
        printf(
            f"The letter is {BRIGHT_GREEN}{ITALIC}in{RESET_ALL} the secret word.\n\n", pause=0.025)
    else:
        printf(
            f"The letter is {BRIGHT_RED}{ITALIC}not in{RESET_ALL} the secret word.\n\n", pause=0.025)
        guesses_left -= 1

if guesses_left != 0:
    printf(f"Congrats, you win. The word was {BOLD}{secret_word}{RESET_ALL}.\n")
else:
    printf(f"Sorry, you lost. The word was {BOLD}{secret_word}{RESET_ALL}.\n")
