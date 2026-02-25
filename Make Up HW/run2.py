#run2.py
#Jiawei Zhu
#
#Comapre to run1,we have more check the distance and average min per km.

#Make the title
print("Run calculator")

#Let user input the value of the distance
distance = input("Enter distance in km:")

#Set the origional value
total = 0.0
times = 0

while True:
    #Let user input the value want
    time = input("Enter time in minutes for a " + distance + " km run:")
    #Make sure that it is the number
    try:
        time = float(time)
        #The times plus 1
        times = times + 1
        #Count its all value
        total = total + time
        continue
    #Determine that the situation is not float
    except:
        break

if times > 0:
    #Calcualte the average
    sum1 = total / times
    #Keep it for one decmial
    formatted = "{:.1f}".format(sum1)
    #The change it can be used in the formmula becuase it can't used as int str
    distance = float(distance)
    #Keep it for one decmial
    formatted_distance = "{:1.0f}".format(distance)
    #Calculate the km per minutes 
    per_km = sum1 / distance
    #Keep it for one decmial
    formatted_pace = "{:.1f}".format(per_km)
    #Make the output
    print("Your average", formatted_distance ,"km time is",formatted,"minutes.")
    print("Your average pace is,",formatted_pace,"min/km.")
