#pi.py
#Jiawei Zhu
#
#approximate the value of pi using a series expansio
#Import the math module that get the value of pi
import math

#Prompt the user for the number of terms 
num = int(input("Number of terms:"))

#Set the origional value of pi
pi_estimate = 0.0

#loop the series that calculate the pi
for i in range(num):
    term = ((-1) ** i) / (2 * i + 1)
    pi_estimate = pi_estimate + term

#Finalize the approximation with times 4
pi_estimate = pi_estimate * 4  

#Calculate the error 
error = math.pi - pi_estimate

#Format the output to 9 decimal places
pi_str = "{:.9f}".format(pi_estimate)
error_str = "{:.9f}".format(error)

#Make the output
print("Estimate of pi: " + pi_str)
print("Error: " + error_str)  

