#heart.py
#Jiawei Zhu
#
#Set a formula that to calculate the maximum heart rate and target heat rate with higher and lower
#Prompt the user to enter their age
Enter_your_age = int(input("Enter your age:"))
#Calculating the maximum heart rate
maximum_heart_rate = 220 - Enter_your_age
#Calculate the target heart rate range, which is 50% to 85% of the maximum heart rate
target_heart_rate_lower = 0.5*maximum_heart_rate
target_heart_rate_upper = 0.85*maximum_heart_rate
#Then print the value
print(f"Your maximum heart rate is {maximum_heart_rate} bpm")
print(f"Your target heart rate is {target_heart_rate_lower} - {target_heart_rate_upper} bpm")
