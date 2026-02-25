#first_ave
#Jiawei Zhu
#
#Moving Average Temperature Calculation
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

#Quit the loop
infile.close()

#Make index as the first vakue
index = k
#Check that the indexs are in the range as expected
if index - k >= 0 and index + k < len(values):
    window = values[index - k : index + k + 1]
    ave = sum(window) / (2 * k + 1)
    #Formated it as the forth demical place
    formated = "{:.4f}".format(ave)
    #Get the correct year with the index
    years = years[index]
    #Make the output
    print(str(years)+","+formated)
