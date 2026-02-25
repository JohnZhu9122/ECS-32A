#converter.py
#Jiawei Zhu
#
#Convert character to the binary
character = input("Enter a character:")
#Convert the character to its integer 
integer = ord (character)
#Convert the character to its binary 
binary = bin (integer)
print (f"{character} corresponds to the integer {integer} which is {binary} in binary.")

