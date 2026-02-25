#moving_ave_csv.py
#Jiawei Zhu
#
#Calculates temperature anomalies using a moving average window and make it not only in python
#Prompt user for the file
filename = input("Temperature anomaly filename:")

#Open file in the reading mode
infile = open(filename, "r")

#Ignore the header
infile.readline()

#Prompt user for window size
size = input("Enter window size:")

#Let size be a letter
k = int(size)

#List the years and temps
years = []
values = []

#Loop throught each line of the file
for line in infile:
    #Remove new line after each line
    line = line.strip()
    #Spilt it to year and temperature on each line
    year, value = line.split(",")
    #Change the years to integar and store it
    years.append(int(year))
    #Change the years to float and store it
    values.append(float(value))
#Close the input file
infile.close()

#Create output and write the information it needed
outfile = open('MovingAve.csv','w')
#Write csv header
outfile.write("Year,Value\n")

#Check that the indexs are in the range as expected
for index in range(k,len(values)-k):
    window = values[index - k : index + k + 1]
    ave = sum(window) / len(window)
    #Formated it as the forth demical place
    formatted = "{:.4f}".format(ave)
    year = years[index]
    #Make the output
    outfile.write(str(year) + "," + formatted + "\n") 
#Close outout file
outfile.close()
