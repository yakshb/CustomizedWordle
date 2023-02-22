import random
import sys
from termcolor import colored
import nltk 
nltk.download('words')
from nltk.corpus import words

def print_menu():
  print("\nLet's play Wordle:")
  print("Type a 5 letter word and hit enter!\n")

def read_random_word():
  with open("scratch.txt") as f:
    words = f.read().splitlines()
    return random.choice(words)

nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

play_again = ""
while play_again != "q":
  print_menu()
  ## Second number is exclusive in range()
  
  # word = read_random_word()
  word = random.choice(words_five)
  for attempt in range(1, 7):
    guess = input().lower()
  
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
  
    for i in range( min(len(guess), 5) ):
      if guess[i] == word[i]:
        print(colored(guess[i], 'green'), end="")
      elif guess[i] in word:
        print(colored(guess[i], 'yellow'), end="")
      else:
        print(guess[i], end="")
    print()
  
    if guess == word:
      ## f strings like below -- enable you to put variables inside strings
      print(colored(f"\nCongrats! You got the wordle in {attempt}", 'blue'))
      break
    elif attempt == 6:
      print(colored(f"Boohoo! Today's wordle is.. {word}", 'red'))

    
  play_again = input("Play Again? Type Q to Exit")

    