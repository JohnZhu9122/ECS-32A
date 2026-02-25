#cash2.py
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
    #Determine the line is start with the dollar sign
    if stripped_line[0] == '$':
        running_count = running_count + 1
        #We only need to count this number
        running_sum = running_sum + float(stripped_line[1:])
    #If it doesn't start with dollat sign
    else:
        continue
        
#End the loop
infile.close()

#Format the file into two decimals
running_sum = "{:.2f}".format(running_sum)

#Make the output
print("File contained", running_count, "items totaling $" + str(running_sum))
