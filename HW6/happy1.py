#happy1.py
#Jiawei Zhu
#
#The program helps read file and its index
#To make a dictionary that let countries matches happiness index
#And only make the ouput of year and happiness index(key with unique value)

def main():
    #Part 1: Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()
    print_sorted_dictionary(happy_dict)

def make_happy_dict():
    #Make the dictionary
    happy_dict = {}
    #Check the happiness.csv
    with open("happiness.csv","r") as infile:
        #Ignore the header 
        infile.readline()
        #Loop through each line
        for line in infile:
            #Remove new line after each line
            line = line.strip()
            if not line:
                #Skip the empty line if have
                continue
            #Split the symbol not necessary
            parts = line.split(",")
            #Check and match correct country
            country = parts[0].strip()
            #Check and match correct Happiness index
            happiness_index = parts[2].strip()
            #Store them in dictionary
            happy_dict[country] = happiness_index
    #Return to the dictionary
    return happy_dict


def print_sorted_dictionary(D):
    #Determine it the key and value matched
    for key in sorted(D.keys()):
        #Make the output key with unique value
        print(key, D[key])
    return

#Run the program      
main()
