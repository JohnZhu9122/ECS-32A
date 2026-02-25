#phone.py
#Jiawei Zhu
#
#Check the phone number with the correct form

#Promopt the user input
number = input("Enter number as ### ###-####:")

#Count the number's length
vaild = len(number) == 12

#Initialize position counter
letter = 0

#Loop each letter that vaild or invaild with the right set
while vaild and letter < 12:
    #The letter should be count begin as 0, so it is 3. I made the mistake during in here
    if letter == 3:
        vaild = number[letter] == " "
    #The letter in 8th should be "-"
    elif letter == 7:
        vaild = number[letter] == "-"
    #Check others letter is number or not
    else:
        vaild = number[letter].isdigit()
    #And then make the loop to check each letter
    letter = letter + 1

#Make the output if the condition is satisfy or not
if vaild:
    print("Valid")
else:
    print("Invalid")
