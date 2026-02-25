#moving_ave
#Jiawei Zhu
#
#Applies a moving average with specified window and year trend and make it in the python
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


#Check that the indexs are in the range as expected
for index in range(k,len(values)-k):
    window = values[index - k : index + k + 1]
    ave = sum(window) / len(window)
    #Formated it as the forth demical place
    formated = "{:.4f}".format(ave)
    year = years[index]
    #Make the output
    print(str(year)+","+formated)
