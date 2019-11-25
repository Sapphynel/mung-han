"""
Hangman script: Terminal Edition
"""
import sys
import urllib.request
import random
# Grab words from local file (test version)

word_file = "/usr/share/dict/words"
words = open(word_file).read().splitlines()

"""
# Grab words and puts them in a list (remote dict)
word_url = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = urllib.request.urlopen(word_url)
long_txt = response.read().decode()

words = long_txt.splitlines()
"""
wins = 0
losses = 0

MAX_TRIES = None
LAST_CHANCE = False

def hangman_config():
    global MAX_TRIES
    global LAST_CHANCE
    print("Configuration")
    print("Number of errors to hang: ")
    while True:
        setting = input("Type a number (1 < x < 10): ")
        try:
            MAX_TRIES = int(setting)
            if MAX_TRIES < 1 or MAX_TRIES > 10:
                print("Not in range!")
            else:
                print("Number of Tries: {0}".format(MAX_TRIES))
                break
        except ValueError:
            print("Invalid input!")

    """
    print("Require repeat guesses to fill in all of a single letter?")
    print("Example: the word 'feet' would require two e guesses")
    while True:
        boolean = input("Repeated Guessing? (Y/N)")
        if boolean == "Y":
            repeats = True
            print("Repeats on")
            break
        elif boolean == "N":
            repeats = False
            print("Repeats off")
            break
        else:
            print("Invalid input!")
            continue
    """

    print("Allow a last chance?")
    print("After running out of attempts, typing the word will count as a win")
    while True:
        boolean = input("Saving Throw? (Y/N) ")
        if boolean == "Y":
            LAST_CHANCE = True
            print("Saving throw on")
            break
        elif boolean == "N":
            LAST_CHANCE = False
            print("Saving throw off")
            break
        else:
            print("Invalid input!")

def hangman():
    target = random.choice(words)
    letter_list = set(target.lower())
    errors = 0
    guessed = set()
    current = " ".join(char if char in guessed else "_" for char in letter_list)

    while (errors < MAX_TRIES):
        print("Current state: " + current)
        print("Errors left: {0}".format(MAX_TRIES - errors))
        guess = input("Guess a letter: ")
        if len(guess) != 1 or guess.isalpha() == False:
            print("Invalid guess!")
            continue
        elif guess in guessed:
            print("Already guessed!")
            continue
        else:
            guessed.add(guess.lower())
            if guess.lower() in letter_list:
                print("Correct!")
            else:
                print("Wrong!")
                errors += 1
            current = " ".join(char if char in guessed else "_" for char in letter_list)


    print("Out of attempts!")
    if LAST_CHANCE == True:
        saving_throw = input("Saving throw! Guess the word: ")
        if saving_throw == target:
            print("Got it!")
            return True
        else:
            print("Failure...")
            return False

    else:
        print("No saving throw; you lose...")
        return False



print("Welcome to Hangman: Terminal Edition!")
hangman_config()

while True:
    result = hangman()
    if result == True:
        print("You win!")
        wins += 1
    else:
        print("You lost.")
        losses += 1

    print("Wins: {0}, Losses: {1}".format(wins, losses))

    next_action = input("Play again?: (Y/N/config) ")
    if next_action == "Y":
        print("Next game starting!")
        continue
    elif next_action == "config":
        print("Changing rules")
        hangman_config()
        continue
    elif next_action == "N":
        print("Thanks for playing!")
        sys.exit()
    else:
        print("")
