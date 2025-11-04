#carbs.py
#Jiawei Zhu
#
#Get user inputs
item = input("Enter menu item:")
#float Float input for calories and carbs
calories = int(input("Enter calories:"))
carbs = float(input("Enter carbs in grams:"))
#Round calories to the nearest 10
Rounded_calories = round(calories,-1)
#calculate the four crabs, hard using a scentence so that using step by step
step1 = carbs * 4
step2 = (step1 / calories)*100
step3 = round(step2)
#Then last output
print(f"{item} {Rounded_calories} Cals {step3}% Carbs")
