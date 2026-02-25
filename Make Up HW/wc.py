#wc.py
#Jiawei Zhu
#
#Check the files lines,words and characters with more speific details than the last file

#Promopt user input
filename = input("Enter filename:")

#Open the file as the reading mode
infile = open(filename,'r')

#Set the orgional line,word and character in the file
count = 0
word = 0
character = 0

#Loop each line in the file
for line in infile:
    #Increase with each line read
    count = count + 1
    #Splitting line into words
    words = line.split()
    #Count words
    word = word + len(words)
    #Count characters
    character = character + len(line)
    
#Make the output
print("Lines",count)
print("Words",word)
print("Characters",character)
#End the loop
infile.close()
