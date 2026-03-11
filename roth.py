#roth.py
#Jiawei Zhu
#
#Calcuulate how long does it take that to approach to the double
#Prompt user for input
IRA = int(input("Enter an initial Roth IRA deposit amount:"))
annual_rate = int(input("Enter an annual percent rate of return:"))

#Starting with the origional data
year = 0

#Start with the initial
Value = IRA

# Loop to calculate growth each year and stop when value doubles
while Value  < 2 * IRA:
    #Increase the year count
    year = year + 1
    #The rate that with each year
    interest_rate = Value * (annual_rate / 100)
    #The whole total valie of each year
    Value = Value + interest_rate
    #Format the count with two decimal
    formatted_value = "${:.2f}".format(Value)
    #Make the output
    print("Value after year " + str(year) + ": " + formatted_value)
#Make the output
print("It will take", year, "years to double your investment with a", str(int(annual_rate)) + "% APR.")
