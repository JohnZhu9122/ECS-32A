#trycat.py
#Jiawei Zhu
#
#Determine wheather or not file in there

while True:
    #Prompt the user for the file it needs
    file_name = input("Enter a file name to open:")
    
    try:
        #Attempt to open the file
        infile = open(file_name, "r")
        
        #Read and print each line
        for line in infile:
            line = line.strip()
            print(line)
        
        #Exit the loop
        break
    #If there is with a useless or none file
    except:
          print("Could not open '"+file_name+"'")




        




