# AUTHOR: RICHARD BARTLEWITZ
# Hangman (user guesses comp's word)
# This Script will play a game of hangman with the user

import random

# open txt with all the possible words
# read txt and randomly pick a word from that list
# this word is then defined by chosen_word
lines = open("words_stripped.txt").read()
line = lines[0:]
word_part = line.split()
chosen_word = random.choice(word_part)

# this script works off of taking whatever word is in this dictionary
words = {chosen_word}

# user_guess takes tha users letter guess in and feeds back a statement of if it is in the word or not
def user_guess(current, word):
	print("Current state: " , current)
	guess = input("Letter? ")
	print(" ")
	if guess in word and guess not in current:
		return ''.join(w if w==guess else c for c, w in zip(current, word)), word
	else:
		print("Nope! %s is not in the word." % guess)
		return current, word

# this foor loop is what allows the script to run through each letter that is guessed
# allows for 10 incorrect guesses by user
for word in words:
	current = "*"*len(word)
	remaining = 10
	while remaining:
		old_state = current
		current, word = user_guess(current , word)
		if old_state == current:
			remaining -= 1
			print("Remaining guesses: %d" % remaining)
		if current == word:
			print("You Won! -", word)
			break
	if not remaining:
		print("I Won! -", word)


