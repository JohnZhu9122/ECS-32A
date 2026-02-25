#lc.py
#Jiawei Zhu
#
#Read the file and then to make

#Promopt user input
filename = input("Enter filename:")

#Open the file as the reading mode
infile = open(filename,'r')

#set the orgional lines in the file
count = 0

#Loop each line in the file
for line in infile:
    #Remocing lead space
    line = line.strip()
    #Count after each line loop
    count = count + 1

#Make the output
print("Lines",count)
#End the loop
infile.close()
