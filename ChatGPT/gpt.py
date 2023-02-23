import random
import sys
import nltk

nltk.download('words')
from nltk.corpus import words
from termcolor import colored
from flask import Flask, render_template, request

nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('game.html')


@app.route('/play', methods=['POST'])
def play():
  play_again = ""
  word = random.choice(words_five)
  guesses = []
  for attempt in range(1, 7):
    guess = request.form.get('guess').lower()
    guesses.append(guess)

    for i in range(min(len(guess), 5)):
      if guess[i] == word[i]:
        guesses[i] = colored(guess[i], 'green')
      elif guess[i] in word:
        guesses[i] = colored(guess[i], 'yellow')
      else:
        guesses[i] = guess[i]

    if guess == word:
      message = colored(f"\nCongrats! You got the wordle in {attempt}", 'blue')
      break
    elif attempt == 6:
      message = colored(f"Boohoo! Today's wordle is.. {word}", 'red')
      break

  return render_template('game.html', guesses=guesses, message=message)


if __name__ == '__main__':
  app.run(debug=True)
