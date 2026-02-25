#read_temp_stat.py
#Jiawei Zhu
#
#A temperature data reader to check the unnormal temperature in which year

#Promopt the user input
filename = input("Temperature anomaly filename:")
#Open the file in just read mode
infile = open(filename,"r")
#Ignore the header
infile.readline()

#List store current temperature with correct year
current_value = []
current_year = []

#Loop throught each line of the file
for line in infile:
    #Remove new line after each line
    line = line.strip()
    #spilt it to year and temperature on each line
    year, value = line.split(",")
    #Change it to the float number and remove the trailing zeros
    value = float(value)
    #Store current temperature
    current_value.append(value)
    #Store correct year
    current_year.append(year)

#Find the maxminum and minmium temperature
min_value = min(current_value)
max_value = max(current_value)

#Match the correct year with maxminum and minmium temperature
mintemp_year = current_year[current_value.index(min_value)]
maxtemp_year = current_year[current_value.index(max_value)]

#Make the output of maxinum and minumum temperature with correct year
print("Min temp: " + str(min_value) +" in " + mintemp_year)
print("Max temp: " + str(max_value) +" in " + maxtemp_year)

#Quit the loop after it is done
infile.close()
