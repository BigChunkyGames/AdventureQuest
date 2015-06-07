# Rock paper scissors game

from random import randint
from time import sleep

guess = 4
print("Let's play rock paper scissors!")
print("play 1 for rock, 2 for paper, and 3 for scissors.")
guess = input()
while guess != 1 and guess != 2 and guess != 3:
    print ("Either pick 1, 2, or 3.")
    guess = input()
if guess == 1:
    name = "rock"
elif guess == 2:
    name = "paper"
elif guess == 3:
    name = "scissors"
print("You chose %s!") % name
sleep(.8)
opponent = randint(1,3)
if opponent == 1:
    opname = "rock"
elif opponent == 2:
    opname = "paper"
elif opponent == 3:
    opname = "scissors"
print("I picked %s.") % opname
sleep(.8)
if opponent == guess:
    print("We both picked %s.") % name
    print("Tie game!")
elif opponent == 1 and guess == 2:
   print("Paper covers rock!")
   print("You win!")
   win = 0
elif opponent == 1 and guess == 3:
   print("Rock beats scissors!")
   print("You lost!")
   win = 0
elif opponent == 2 and guess == 1:
   print("Paper covers rock!")
   print("You lost!")
   win = 0
elif opponent == 2 and guess == 3:
   print("Scissors beats paper!")
   print("You win!")
   win = 1
elif opponent == 3 and guess == 1:
   print("Rock beats scissors!")
   print("You win!")
   win = 1
elif opponent == 3 and guess == 2:
   print("Scissors beats paper!")
   print("You lost!")
   win = 0
else:
    print("Something broke!")
