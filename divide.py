#divide.py
#Jiawei Zhu
#
# Simple Division Program
Enter_a_number = int(input("Enter a number:"))
Enter_a_number_to_divide_that_by = int(input("Enter a number to divide that by:"))
#Using the symbol what we learnt in the class using the variable below
divided_result = Enter_a_number // Enter_a_number_to_divide_that_by
#calculate the remainder of divison
remaing_number = Enter_a_number % Enter_a_number_to_divide_that_by
print (f"{Enter_a_number} divided by {Enter_a_number_to_divide_that_by} is {divided_result} with {remaing_number} remaining")
