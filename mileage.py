#mileage.py
#Jiawei Zhu
#
#Calculates fuel economy by computing
#Display the program title
print("Your Personal Fuel Economy")

#Intalize the original data
total_miles = 0
total_gallons = 0

#Loop continuously to collect user input until the user exits
while True:
    #Prompt the user for the number of miles traveled; exit if input is none
    miles = input("Number of miles traveled (or enter to exit):")
    if miles == "":
        #Exit the loop 
        break
    #Prompt the user for the number of gallons traveled; exit if input is none
    gallons = input("Number of gallons needed:")
    if gallons == "":
        #Exit the loop
        break
    #Convert inputs to floats
    miles = float(miles)
    gallons = float(gallons)

    #Calculate mileage 
    mileage = miles / gallons
    #Format the count with one decimal
    formatted_mileage = "{:.1f}".format(mileage)
    print("Mileage this tank = " + formatted_mileage)

    #Update the value of total miles and total gallons
    total_miles = total_miles + miles
    total_gallons = total_gallons + gallons

if total_gallons > 0:
    average_mileage = total_miles / total_gallons
    #Format the count with one decimal
    formatted_average = "{:.1f}".format(average_mileage)
    #Make the output
    print("Average mileage = " + formatted_average)

