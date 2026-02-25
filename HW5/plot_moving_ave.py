#plot_moving_ave.py
#Jiawei Zhu
#
#Computes a centered moving average and visualize its trend Matplotlib

import matplotlib.pyplot as plotmoving

#Promopt the user input
filename = input("Temperature anomaly filename:")

#Open the file as reading mode
infile = open(filename, "r")

#Ignore the header
infile.readline()

#Prompt user for window size
size = input("Enter window size:")

#Let size be a letter for convience
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

#Lists to store moving average results for output
ma_years = []
ma_values = []

#Create output and write the information it needed
outfile = open('MovingAve.csv', 'w')
#Write csv header
outfile.write("Year,Value\n")

#Check that the indexs are in the range as expected
for index in range(k, len(values) - k):
    window = values[index - k : index + k + 1]
    ave = sum(window) / len(window)
    #Formated it as the forth demical place
    formatted = "{:.4f}".format(ave)
    year = years[index]
    #Make the output
    outfile.write(str(year) + "," + formatted + "\n")
    #Store of output
    ma_years.append(year)
    ma_values.append(ave)
#Close outout file
outfile.close()

plotmoving.plot(years, values, 'b')
plotmoving.plot(ma_years, ma_values, 'orange')
plotmoving.xlabel('Time')
plotmoving.ylabel('Temperature Anomaly')
plotmoving.title('Plotting SacramentoTemps.csv with Moving Ave k =20')
plotmoving.show()
