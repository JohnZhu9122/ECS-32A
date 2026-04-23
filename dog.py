#dog.py
#Jiawei Zhu
#
#Determine wheather condition
#Prompt the user to enter the weather condition
Enter_weather_condition = input("Enter weather condition (rainy/sunny/snowy/cloudy):")
#Check the weather is sunny
if Enter_weather_condition == "sunny":
    Enter_temperature = int(input("Enter temperature:"))#Determine the temperature
    print("Instructions for the walk:")
#Check the weather is rainy,snowy and cloudy
elif Enter_weather_condition == "rainy" or "snowy" or "cloudy":
    print("Instructions for the walk:")

#Provide the information if weather is rainy
if Enter_weather_condition == "rainy":
    print("The dog should be taken for a short walk with an umbrella.")
#Provide the information if weather is sunny
elif Enter_weather_condition == "sunny":
    #Determine which range of temperature to differnt information
    if 80 <= Enter_temperature <= 114:
        print("The dog should be taken for a walk in the shade and given water.")#range in (80,114)
    elif 45 <= Enter_temperature < 80:
        print("The dog can enjoy a regular walk.")#range in (45,80)
    elif -14 <= Enter_temperature < 45:
        print("Dress the dog warmly for a walk.")#range in (-14,45)
    else:
        print("Invalid weather condition.")#range out of (-14,114)
#Provide the information if weather is snowy
elif Enter_weather_condition == "snowy":
    print("Take the dog for a short walk and ensure they stay warm.")
#Provide the information if weather is cloudy
elif Enter_weather_condition == "cloudy":
    print("Enjoy a regular walk with your dog.")
#Provide the information if weather are not all above information
else:
    print("Invalid weather condition.")
    
