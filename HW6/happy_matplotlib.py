# happy_matplotlib.py
# Jiawei Zhu
#
#Creates a plot in matplotlib with only relevant data

import matplotlib.pyplot as plt

def main():
    happy_dict = make_happy_dict()
    plot_gdp_happiness(happy_dict)

def make_happy_dict():
    #Make the dictionary
    happy_dict = {}
    #Check happiness.csv
    with open("happiness.csv","r") as infile:
        #Ignore the header 
        infile.readline()
        #Loop through each line
        for line in infile:
            #Remove new line after each line
            line = line.strip()
            if not line:
                #Skip empty lines
                continue
            #Split the symbol not necessary
            parts = line.split(",")
            #Check and match correct country
            country = parts[0].strip()
            #Check and match correct Happiness index
            happiness_index = parts[2].strip()
            # Store them in dictionary
            happy_dict[country] = happiness_index
    return happy_dict

def plot_gdp_happiness(happy_dict):
    #Stores required values
    gdp_per_capita = []    
    happiness_scores = []   
    populations = []        
    labels = {}             

    #Check the world_pop_gdp
    with open("world_pop_gdp.tsv","r") as infile:
        #Ignore the header
        infile.readline()
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
            population_value = parts[1].replace(",", "").strip()
            #Convert the population that helps then to use
            population = float(population_value) 
            gdp_per = parts[2].replace("$", "").replace(",", "").strip()
            
            #Determine which happiness index with the correct countries are suitable
            if country in happy_dict and population >= 10:
                happiness_index = float(happy_dict[country])
                
                #Add data to their lists they need
                gdp_per_capita.append(float(gdp_per))
                happiness_scores.append(happiness_index)
                populations.append(population * 0.1)
                
                #Store labels for countries with population over and equal 100 million
                if population >= 100:
                    labels[country] = (float(gdp_per), happiness_index)

    #Make Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(gdp_per_capita, happiness_scores, s=populations, alpha=0.6, edgecolors="k")
    
    #Make Labels for Countries over thant 100 million
    for country, (x, y) in labels.items():
        plt.text(x, y, country, fontsize=10, ha="right")
    
    #Give each label for their name
    plt.xlabel("Country")
    plt.ylabel("Happiness Index")
    plt.title("GDP per Capita, Population in millions and Happiness")
    plt.grid(True)
    plt.show()

#Run the program      
main()
