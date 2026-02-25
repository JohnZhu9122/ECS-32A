#cash.py
#Jiawei Zhu
#
#Read the price and count it how many times takes and total value
#Prompt the user to enter the filename
filename = input("Automated cash register\nEnter file of prices:")
#Open the file just in the read mode
infile = open(filename, "r")
#Origional the count and summaeize
running_count = 0
running_sum = 0.0

#Loop each line in the file
for line in infile:
    #Removing the space to another line
    stripped_line = line.strip()
    #Determine the line is empty or not
    if stripped_line:
        running_count = running_count + 1
        running_sum = running_sum + float(stripped_line)
#End the loop
infile.close()

#Format the file into two decimals
running_sum = str("{:.2f}".format(running_sum))

#Make the output
print("File contained", running_count, "items totaling $" + running_sum)
