#cash_register.py
#Jiawei Zhu
#
#Calculate the sum of cost and how many times to put in
#Make the output of the condition continous and exit
print ("Cash register (press enter to exit)")

#Make the variable
count = 0.00
cash =0

#Loop the calculate the item cost
#Loop to the times user enter in 
while True:
    #Promot the user name of item cost
    enter = input("Enter item cost:")
    #When the user want to exit the loop
    if enter == "":
        break
    count = count + float(enter)
    cash = cash + 1

#Format the count with two decimal
formatted_count = "{:.2f}".format(count)

#Make the output
if cash == 1:
    print("You entered " + str(cash) + " item totaling " + formatted_count)
else:
    print("You entered " + str(cash) + " items totaling $" + formatted_count)
