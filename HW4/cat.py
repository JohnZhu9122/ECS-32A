#cat.py
#Jiawei Zhu
#
#Read and print the file as the txt in the same`

#Prompt the user input
file_name = input("Enter a file name to open:")

#Open and just read the file
infile = open(file_name, "r")

#Loop through each line in the file
for line in infile:
    #Removing the leading space
    line = line.strip()
    #Make the output
    print(line)

#Close the file after reading
infile.close()
