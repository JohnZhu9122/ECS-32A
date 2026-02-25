# approx.py
# Jiawei Zhu
#
# Reduce the gaps in data

number1 = float(input("Enter a number:"))
number2 = float(input("Enter a number:"))

# Calculate absolute difference
difference = abs(number1 - number2)

# Check if the two number are exactualy same
if number1 == number2:
    print("Those numbers are identical")
# Check for decimal places is 10
elif difference < 1e-10:
    print("Those numbers are very nearly identical")
# Check for decimal places form 2 to 9 
elif difference < 1e-9:
    print("Those numbers are the same to 9 decimal places")
elif difference < 1e-8:
    print("Those numbers are the same to 8 decimal places")
elif difference < 1e-7:
    print("Those numbers are the same to 7 decimal places")
elif difference < 1e-6:
    print("Those numbers are the same to 6 decimal places")
elif difference < 1e-5:
    print("Those numbers are the same to 5 decimal places")
elif difference < 1e-4:
    print("Those numbers are the same to 4 decimal places")
elif difference < 1e-3:
    print("Those numbers are the same to 3 decimal places")
elif difference < 0.01:
    print("Those numbers are the same to 2 decimal places")
#If all above condition are diffrernt 
else:
    print("Those numbers are different")

