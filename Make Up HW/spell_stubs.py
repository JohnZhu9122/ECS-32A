
# spell_checker.py
import string

def main():
	# read the list of correctly spelled words from a file
	wordList = read_word_list()

	print(len(wordList), "words read into spelling dictionary")

	# check sentence
	check_sentence(wordList)

def read_word_list():
    wordList = []  
    with open("scrabble.txt", "r") as infile:
        for line in infile:
            word = line.strip()
            wordList.append(word)
    return wordList


def check_sentence(wordList):
	return

main()
