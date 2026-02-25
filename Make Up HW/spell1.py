#spell1.py
#Jiawei Zhu
#
#Check the file and Account how many words in the file
import string

def main():
	# read the list of correctly spelled words from a file
	wordList = read_word_list()

	print(len(wordList), "words read into spelling dictionary")

	# check sentence
	check_sentence(wordList)

def read_word_list():
    #Intailze that to store for the words
    wordList = []
    #Open the scrabble.txt as reading model 
    with open("scrabble.txt", "r") as infile:
        #Check the line on the loop
        for line in infile:
            #Remove things it does need such as space and so on
            word = line.strip()
            #Add words in the empty list
            wordList.append(word)
    #Return the list
    return wordList


def check_sentence(wordList):
	return

main()
