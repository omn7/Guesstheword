from clear import clear
from printf import printf

def get_guess():
	guess = input("Guess: ")

	clear()

	if len(guess) == 1: return guess

	printf("Your guess must have exactly one character.\n")
	return get_guess()
