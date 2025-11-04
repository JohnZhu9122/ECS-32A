#bmi.py
#Jiawei Zhu
#
#A program that calculate the bmi
#Prompt the user to enter their height in inches and convert it to a float
height_in_inches = float(input("Enter height in inches:"))
#Prompt the user to enter their weight in pounds and convert it to a float
weight_in_pounds = float(input("Enter weight in pounds:"))
#The formula that used what typed before for calculate the bmi
BMI = (weight_in_pounds / (height_in_inches * height_in_inches)) * 703
print(f"BMI: {BMI}")
