#paint.py
#Jiaweii Zhu
#
#Make a Paint coverage estimator and using slides 3 new things 'if'
print("Paint coverage estimator")
#Get user inputs for room dimensions in inches
Length = int(input("Length of room in inches:"))
Width = int(input("Width of room in inches:"))
Average = int(input("Average height of room in inches:"))
#calculae the 4 walls that to be covered
Area_in_square_inches =2*Average*(Length+Width)
#Change the inches to feets
Area_in_square_feet = Area_in_square_inches / 144
cans = Area_in_square_feet / 100
# First, extract the integer part of the cans_required_decimal
integer_part = int(cans)
# Next, check if the decimal part exists becasue cans can't be dememical
decimal_part = cans - integer_part
# If there is a decimal part (not zero), add 1 to the integer part
if decimal_part > 0:
    cans = integer_part + 1
else:
    cans= integer_part
print(f"You'll want {cans} cans.")
