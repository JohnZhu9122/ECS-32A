#temp_list.py
#Jiawei Zhu
#
#Read the anoomalies temperatures that make the output as a list

#Prompt user for the file
filename = input("Temperature anomaly filename:")

#Open file in the reading mode
infile = open(filename, "r")

#Ignore the header
infile.readline()

#List the years and temps
value_listed = []

#Loop throught each line of the file
for line in infile:
    #Remove new line after each line
    line = line.strip()
    #Spilt it to year and temperature on each line
    year, value = line.split(",")
    #Convert temperature to float and add to list
    value_listed.append(float(value))
    
#Quit the loop
infile.close()

#Make the output
print(value_listed)

