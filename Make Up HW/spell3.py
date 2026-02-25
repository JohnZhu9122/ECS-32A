#spell3.py
#Jiawei Zhu
#
#Compare spell 2, it has improve to remove some unnecessary symbols and misspelling

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
    #Return the lis
    return wordList


def check_sentence(wordList):
        #Prompot user input
        check = input("Enter a sentence to check:")
        #Split the user's input into words
        words= check.split()
        symbol = '.'
        #Check the line on the lop
        #And determine it is in the wordList or not
        for word in words:
                word = word.lower()
                #Removing the symbol in the beginning
                while len(word) > 0 and word[0] in symbol:
                        word = word[1:]
                 #Removing the symbol in the end
                while len(word) > 0 and word[-1] in symbol:
                        word = word[:-1]
                #If word in the wordList
                if word not in wordList and word != "":
                        #Make the output
                        print(word)
                        
main()
