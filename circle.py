#circle.py
#Jiawei Zhu
#
#calcualte the are of a circle
#The data provide in the question
Enter_radius = float(input("Enter radius:"))
pi = 3.14159
#Using the variable that to transfer to the diameter,circumference and area
diameter = 2 * Enter_radius
circumference = 2 * pi * Enter_radius
area = pi * Enter_radius * Enter_radius
#Then print all the things it need
print (f"Diameter {diameter}")
print (f"Circumference {circumference}")
print (f"Area {area}")
