#car.py
#Jiawei Zhu
#
#Guess the correct price
#Make the output that introduce the information
print("Guess the price and win the prize!")

#Make the input that let user to guess
guess = float(input("Enter your guess:"))

#Definte the correct price
correct_price = 44500

#Make the variable
guessing_time = 0

#loop the guess times and with inequal price
while correct_price != guess:
    #Increase the times of guessing
    guessing_time = guessing_time + 1
    if guess > correct_price:
        print("Too high!")
        guess = float(input("Enter your guess:"))
    elif guess < correct_price:
        print("Too low!")
        guess = float(input("Enter your guess:"))
    #When the price is the same 
    else:
        break

#Becuase the guess of correct also need to be count,if not,it missing one time
guessing_time = guessing_time + 1
    

#When the guessing time get condition of the car
if guessing_time <= 5:
    print("It took " + str(guessing_time) + " guesses.")
    print("You won the car!")
#When the guessing time out of condition of the car
else:
    print("It took " + str(guessing_time) + " guesses.")
    print("Too many guesses!")
