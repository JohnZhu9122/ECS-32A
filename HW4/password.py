#password.py
#Jiawei Zhu
#
# Check the password with length,lower,upper,digit and special symbols
# Prompt the user to enter a password
password = input("Enter password:")

#Chcek that the length of password wheather or not at least 8
has_length = len(password) >= 8
#Origional for different requirements
has_lower = False
has_upper = False
has_digit = False
has_special = False

#Special some symbols that it needs
special_chars = '!@#$%&'


#Check the input wheather or not satisfy these conditions are not
for letter in password:
    #Check it for lower or not
    if letter.islower():
        has_lower = True
    #Check it for upper or not
    if letter.isupper():
        has_upper = True
    #Check it for digit or not
    if letter.isdigit():
        has_digit = True
    #Check it for special chars it mentions beofre
    if letter in special_chars:
        has_special = True

#Make the output if conditios are suitbale
if has_length:
    print("Has length")
if has_lower:
    print("Has lower case")
if has_upper:
    print("Has upper case")
if has_digit:
    print("Has digit")
if has_special:
    print("Has special")
        

        
    
