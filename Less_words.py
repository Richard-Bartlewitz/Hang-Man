# AUTHOR: RICHARD BARTLEWITZ
# List Shortener
# getting less words from the words.txt


# makes all_words a list of all words in the file
all_words = []
with open("words.txt") as file:
    for line in file: 
        line = line.strip()
        all_words.append(line)

# makes just_letters a list of all words of all_words that are just letters
just_letters = []
for item in all_words:
    if item.isalpha():
        just_letters.append(item)

# makes not_all_caps a list of all words of just_letters that are not all caps
not_all_caps = []
for item in just_letters:
	if all(x.isupper() for x in item):
		pass
	else:
		not_all_caps.append(item)

# make lower_case a list of all words of not_all_caps that are lowercase
lower_case = []
for item in not_all_caps:
	item = item.lower()
	lower_case.append(item)

# make length_word a list of all worlds of lower_case that are of certain length
length_word = []
for item in lower_case:
	if len(item) >= 3 and len(item) <= 9:
		length_word.append(item)

# make repeat_letter a list of all words of length_word that dont have repeat letters
repeat_letter = []
for item in length_word:
	if all(x == item[0] for x in item):
		pass
	else:
		repeat_letter.append(item)

stripped = open("words_stripped.txt" , "w")
for item in repeat_letter:
	stripped.write(item + "\n")
