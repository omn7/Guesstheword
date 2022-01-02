from sys import stdout
from time import sleep

def printf(text, pause=0.05):
  for character in text:
    stdout.write(character)
    stdout.flush()
    sleep(pause)
