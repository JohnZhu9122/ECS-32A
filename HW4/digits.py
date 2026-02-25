#digits.py
#Jiawei Zhu
#
#let the user inputs only take the number

# Prompt the user to enter a phone number
phone = input("Enter phone number:")

#orgional the empty string for take only digitls
num = ''

#Iterate through each character in the input
for char in phone:
    #Check the it is digitls or not
    if char.isdigit():
        #Make the flow after each character until the end 
        num = num + char

#Make the output
print("Digit string:", num)
