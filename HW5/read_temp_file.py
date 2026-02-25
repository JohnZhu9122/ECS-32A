#read_temp_file.py
#Jiawei Zhu
#
#A temperature data reader and make the output as it require

#Promopt the user input
filename = input("Temperature anomaly filename:")
#Open the file in just read mode
infile = open(filename,"r")
#Ignore the header
infile.readline()

#Loop throught each line of the file
for line in infile:
    #Remove new line after each line
    line = line.strip()
    #spilt it to year and temperature on each line
    year, value = line.split(",")
    #Change it to the float number and remove the trailing zeros
    value = str(float(value))
    #Make the output
    print(year,value)

#Quit the loop after it is done 
infile.close()
    
