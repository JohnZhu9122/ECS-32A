#spell2.py
#Jiawei Zhu
#
#Determine user's input is correctly or not
#And the vaild words only in the file scrabble.txt

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
        #Prompot user input
        check = input("Enter a sentence to check:")
        #Split the user's input into words
        words= check.split()
        #Check the line on the lop
        #And determine it is in the wordList or not
        for word in words:
                #If it is notin the wordList
                if word not in wordList:
                        #Make the output
                        print(word)
                        
main()
