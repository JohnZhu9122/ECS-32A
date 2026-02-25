#happy4.py
#Jiawei Zhu
#
#The program helps read file 
#To make a dictionary that let people know about the country population in millions and GDP per capita
#With the readline and without unnecessary symbol such as '$',',' and so on



def main():
    read_gdp_data()


def read_gdp_data():
    #Check the world_pop_gdp
    with open("world_pop_gdp.tsv","r") as infile:
        #Ignore the header
        infile.readline()
        #Make the header 
        print("Country,Population in Millions,GDP per Capita")
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
            population = parts[1].replace(",","").strip()
            gdp_per = parts[2].replace("$","").replace(",","").strip()
            #Make the output
            print(country + "," + population + "," + gdp_per)

#Run the program      
main()
