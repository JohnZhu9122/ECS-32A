#translate.py
#Jiawei Zhu
#
#Let the user input word follows the rules in pig latin

#Prompot the user input
word = input("Enter a word:")

#Convert the input for the lower versioin that looks same
word = word.lower()

#Define the aeiou as a vowel
vowel = ['a','e','i','o','u']

#Check that if the vowel is the first letter or not
if word[0] in vowel:
    #If it is , add "way" at the end of input
    pig_latin = word + "way"
    #Make sure all the lower versioin
    pig_latin = pig_latin.lower()
#If it is not
else:
    #Move the first letter to the end and add "ay"
    pig_latin = word[1:] + word[0] + "ay"
    #Make sure all the lower versioin
    pig_latin = pig_latin.lower()

#Make the output
print(word,"in Pig latin is",pig_latin) 
