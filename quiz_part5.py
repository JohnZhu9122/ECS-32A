#quiz_part5.py
#Jiawei Zhu
#
#Check the answer range and coeesponding reply
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


#Adding one more question
#Question 7
#Display the question without answer's options to the user
print ("GENIUS: In ancient Rome, what is L divided by X?")
#prompt the user name to the Enter_your_answer
Enter_your_answer = input("Enter your answer:")
# Correct answers in both "5" and Roman numeral "V" form
if Enter_your_answer == "5" or Enter_your_answer == "V":
    print("Correct!")
    score += 1
#if the answer is not "5" or "V",the answer will be like
else:
    print("Correct answers were 5 or V")


# After all questions, count the total score
print (f"Your final score is {score}")
    

# Provide feedback based on the total score
#When the score is small and equal to 2
if score <= 2 :
    print("You were unlucky!")
#When the socre is 3 and 4
elif score <= 3 or score <= 4:
    print("At least you did better than chance!")
#When the score is 5 and 6
elif score <= 5 or score <= 6:
    print("Excellent!")
#When the score is 7
elif score == 7:
    print("Genius!")


    
