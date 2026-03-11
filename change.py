#change.py
#Jiawei Zhu
#
#Calculate the minmium number of coins
#Promot the user to enter the cents they want 
Enter_cent = int(input("Enter cents:"))
print ("The minimum coins for" ,Enter_cent , "cents are:")

#Calculate the number of quarters and Each quarter worth 25 cents
#Make sure that how much quarter on the Enter_cent
Quarter_Value = Enter_cent // 25
#renew the remaininng cents after minus quarters
Enter_cent %= 25

#Calculate the number of Dimes and Each Dime worth 10 cents
#Make sure that how much Dime on the Enter_cent
Dime_Value = Enter_cent // 10
#renew the remaininng cents after minus Dimes
Enter_cent %= 10

#Calculate the number of Nickels and Each Nickel worth 5 cents
#Make sure that how much Nickel on the Enter_cent
Nickel_Value = Enter_cent // 5
#renew the remaininng cents after minus Nickels
Enter_cent %= 5

#Calculate the number of Pennies and Each Nickel worth 1 cents
#It does not need renew because the value of pennie and cent are the same
Pennie_Value = Enter_cent


#Display the minimum number of each type of coin
print(Quarter_Value, "Quarters")
print(Dime_Value, "Dimes")
print(Nickel_Value, "Nickels")
print(Pennie_Value, "Pennies")
       
