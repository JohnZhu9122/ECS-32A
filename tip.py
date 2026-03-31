#tip.py
#Jiawei Zhu
#
#Calculate the tips with some rating
#The rate of tips from 15% increasing to the 25%
#Promopt the user name into total number its need
total = float(input("Enter total:"))
#the rating with of origional tip
tip_rate = 0.15
# Loop to calculate and print the rate of tips from 15% increasing to the 25%
# Loop continues until tip_rate reaches 25%
while tip_rate < 0.26: 
    tips = total * tip_rate
    #format the tips with two decimal
    formatted_str = "${:.2f}".format(tips)
    #let the tips transfer to the percntage (tip_rate * 100)
    formatted_pct = "{:.0f}%".format(tip_rate * 100)
    #Make the output
    print("A " + formatted_pct + " tip is " + str(formatted_str))
    #Let the rate increse in 1 % for each,and because it set 25%,won't contions forever
    tip_rate = tip_rate + 0.01

