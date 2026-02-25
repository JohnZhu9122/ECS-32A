#hangman.py
#Jiawei
#
#A guess words programs with steps during your process
#And count how many times your guessed

#Set the origional word me need 
word = "mississippi"

#Set a list for account and change with user input
guess_word = ["_"] * len(word)

#Account how many times user guess
guess_time = 0

print("Guess the word game.")

#Constrcut the output
output = ""
for letter in guess_word:
    #Let each characters that in the string
    output = output + letter
print(output)

#Make the loop that let user guess until guess all letters
while "_" in guess_word:
    #Let uer guess the letter want
    guess = input("Guess a letter:").lower()
    #With each time guess, it should be add
    guess_time = guess_time + 1

    #If the user type the correct letter in 
    for i in range(len(word)):
        #Determine that wheater or not it is correct or false
        if word[i] == guess:
            #Replace the "_" with the correct letter
            guess_word[i] = guess

    #Restart the output because of the new correct letter in
    output = ""
    for letter in guess_word:
        #Let each characters that in the string
        output  = output + letter
    #Make the output
    print(output) 

#Make the output
print("It took you", guess_time ,"guesses.")
