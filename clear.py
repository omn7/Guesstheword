from subprocess import call
from os import name

def clear():
  call("clear" if name == "posix" else "cls", shell=True)
