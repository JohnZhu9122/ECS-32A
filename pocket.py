#pocket.py
#Jiawei Zhu
#
#Calculate the total money to transfer into differnt units
#Promot the user name in differnt unit of coin
print ("Compute your pocket change!")

Quarters = int(input("Quarters?"))#Number of Quarters

Dimes =  int(input ("Dimes?"))#Number of Dimes

Nickels = int(input("Nickels?"))#Number of Nickels

Pennies = int(input("Pennies?"))#Pennies


# That definite the value of each unit
Pennie_Value = 1 

Nickel_Value = 5 

Dime_Value = 10 

Quarter_Value = 25 

#Caluclate the value to trasnder the same unit of pennies
total_pennies = (Quarters * Quarter_Value) + (Dimes* Dime_Value) + (Nickels * Nickel_Value) + (Pennies * Pennie_Value)

#Convert the total value from cents to dollars
amount = total_pennies / 100                

#To make sure that the total pennies with two demical
formatted_str = "${:.2f}".format(amount)

#Make the output
print("The total is " + formatted_str)
