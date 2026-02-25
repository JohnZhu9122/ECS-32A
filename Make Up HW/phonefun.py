#phonefun.py
#Jiawei Zhu
#
#The program using the characters than replace some digits

#Change the digit to the string that matches dictionary characters
letter2digit = {
    'A':'2','B':'2','C':'2',
    'D':'3','E':'3','F':'3',
    'G':'4','H':'4','I':'4',
    'J':'5','K':'5','L':'5',
    'M':'6','N':'6','O':'6',
    'P':'7','R':'7','S':'7',
    'T':'8','U':'8','V':'8',
    'W':'9','X':'9','Y':'9'
    }

#Let user get the input
phone = input("Enter a phone number:")

#Convert that letters to digit
converted = ""

for char in phone:
    if char in letter2digit:
        #Replace letter become the digit
        converted = converted + letter2digit[char]
    else:
        #Then keep other stuff like space,sybmols and so on keep same
        converted = converted + char

#Make the output
print(converted)


