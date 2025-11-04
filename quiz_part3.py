#quiz_part 3.py
#Jiawei Zhu
#
#record the score that how many question did you get the right answer 
#Display the question and the answer's options to the user
#Question 1
print ("ART: Who painted 'The Persistance of Memory'?\na. Dali\nb. Munch\nc. Picasso")
#prompt the user name to the Enter_your_choice
Enter_your_choice= input("Enter your choice:")
#Initialize the score variable
score = 0
#Determine the answer is a or not
#If answer is a,the answer will be like
if Enter_your_choice == "a":
    print ("Correct!")
    score += 1
#if is not a,the answer will be like
else:
    print ("The correct answer was a")



#Question 2
#Display the question and the answer's options to the user
print ("ENTERTAINMENT: How many oscars did Hitchcock win?\na. None\nb. One\nc. Two")
#prompt the user name to the Enter_your_choice
Enter_your_choice = input("Enter your choice:")
#Determine the answer is a or not
#If answer is a,the answer will be like
if Enter_your_choice == "a":
    print ("Correct!")
    score += 1

#if the answer is not a,the answer will be like
else:
    print ("The correct answer was a")

    

#Question 3
#Display the question and the answer's options to the user
print ("SCIENCE: Which dinosaur is most closely related to the pelican?\na. Velociraptor\nb. Stegosaurus\nc. Pterodactyl")
#prompt the user name to the Enter_your_choice
Enter_your_choice = input("Enter your choice:")
#If answer is a,the answer will be like
if Enter_your_choice == "a":
    print ("Correct!")
    score += 1
#if the answer is not a,the answer will be like
else:
    print ("The correct answer was a")



#Question 4
#Display the question and the answer's options to the user
print ("HISTORY: Which of the following was not invented in Baja California?\na. Margaritas\nb. Chocolate\nc. Caesar Salad")
#prompt the user name to the Enter_your_choice
Enter_your_choice = input("Enter your choice:")
#If answer is b,the answer will be like
if Enter_your_choice == "b":
    print ("Correct!")
    score += 1
#if the answer is not b,the answer will be like
else:
    print ("The correct answer was b")

    


#Question 5
#Display the question and the answer's options to the user
print ("SCIENCE AND NATURE: Can pigs swim?\na. Yes\nb. No\nc. Only in salt water")
#prompt the user name to the Enter_your_choice
Enter_your_choice = input("Enter your choice:")
#If answer is a,the answer will be like
if Enter_your_choice == "a":
    print ("Correct!")
    score += 1
#if is not a,the answer will be like
else:
    print ("The correct answer was a")

    


#Question 6
#Display the question and the answer's options to the user
print ("SPORT AND LEISURE: What color is the middle Olympic ring?\na. Red\nb. Blue\nc. Black")
#prompt the user name to the Enter_your_choice
Enter_your_choice = input("Enter your choice:")
#If answer is c,the answer will be like
if Enter_your_choice == "c":
    print ("Correct!")
    score += 1
#if the answer is not c,the answer will be like
else:
    print ("The correct answer was c")

# After all questions, count the total score
print (f"Your total score is {score}")

