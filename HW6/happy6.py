#happy5.py
#Jiawei Zhu
#
#The program helps read file 
#The difference between happy5 that it needs to determine the country's gdp wheater or not over 100 million
#If it is suitable, then it can make the output
def main():
    happy_dict = make_happy_dict()
    read_gdp_data(happy_dict)

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

def read_gdp_data(happy_dict):
    #Check the world_pop_gdp
    with open("world_pop_gdp.tsv","r") as infile:
        #Ignore the header
        infile.readline()
        #Make the header with one more words "happiness"
        print("Country,Population in Millions,GDP per Capita,Happiness")
        #Loop for each line
        for line in infile:
            #Remove new line after each line
            line = line.strip()
            if not line:
                #Skip the empty line if have
                continue
            #Splict the unnecessary symbols like space, symbol"," and so on
            parts = line.split("\t")
            country = parts[0].strip()
            #And then replace things its need
            population_value = parts[1].replace(",","").strip()
            #Convert the population that helps then to use
            population = float(population_value) 
            gdp_per = parts[2].replace("$","").replace(",","").strip()
            #Match the happiness index with the corrrect country
            happiness_index = happy_dict.get(country)
            #Determine that the country wheater or not in and gdp over 100 million
            if population >= 100 and country in happy_dict:
                #Make the output
                print(country + "," + population_value + "," + gdp_per + "," + happiness_index)

#Run the program      
main()
