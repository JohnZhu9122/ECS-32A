#happy3.py
#Jiawei Zhu
#
#The program helps read file and its index
#To make a dictionary that let countries matches happiness index
#Let user can check only the coutry with happiness index they want


def main():
    #Part 1: Build dictionary mapping countries to happiness index
    happy_dict = make_happy_dict()
    look_happiness_by_countary(happy_dict)


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


def look_happiness_by_countary(happy_dict):
    while True:
        #Let user type the index they want
        country = input("Enter a country to lookup or 'done' to exit:").strip()
        #If the user type input done,skip the loop
        if country.lower() == "done":
            break
        #If the user type input country that can be found in dictionary
        elif country in happy_dict:
            #Make the output that the happines index with the input
            print(happy_dict[country])
         #If the user type input country that can't be found in dictionary
        else:
            #Make the output that the error without happines index
            print(country,"not found")




#Run the program      
main()
