#run1.py
#Jiawei Zhu
#
#Calculate the average of each time runs

#Make the title
print("Run calculator")

#Set the origional value
total = 0.0
times = 0

while True:
    #let user input the value want
    time = input("Enter time in minutes for a 5 km run:")
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
    #Make the output
    print("Your average 5 km time is",sum1,"minutes.")
