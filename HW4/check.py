#check.py
#Jiawei Zhu
#
#Determine the card is vaild or not

#Prompot the user input
card = input("Enter your 8-digit card number:")
#Remove space of user's input
card = card.replace(" ", "")

#Set the origional value
sum_odd = 0
sum_even = 0

#Process the card right to left of each digitl
for i in range(7, -1, -1):
    digit = int(card[i])
    #Check it is even or not
    if i % 2 == 0:
        double = digit * 2
        #If it is even, the way to add the sum
        sum_even = sum_even + double // 10 + double % 10
    #If is odd
    else:
        sum_odd = sum_odd + digit

#Combine the total value
total_sum = sum_odd + sum_even  

#Determine wheater or not the sum of can be multiple of 10
if total_sum % 10 == 0:
    print("Valid")
#If it can't be multiple of 10
else:
    original_check = int(card[7])
    check_digit = (original_check - total_sum) % 10
    print("Invalid\nCheck digit should be " + str(check_digit))

