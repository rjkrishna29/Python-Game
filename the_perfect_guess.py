# write a program that generates a random number that generates a random number and asks the user to guess it.
# if the player guess is higher than the actual number, the program displays "lower number please" Similarly if the user's guess  is too low, the program prints  " hiigher number please" 
#when the user guess the correct number, the program displays the no of guesses the player used to arrive at the number
print("***Let's play the guess game***\nComputer has choosen a number between 0 - 9\nNow it's your turn to guess : ")
import random
guess = random.randrange(0,10)
def userInput():
    a = int(input("Guess the number (0-9) "))
    return a
i = 1    
while i>=1:
    user = userInput()
    if (guess>user):
        print("Guess higher number please ")
        i+=1
    elif (guess<user):
        print("Guess lower number please")
        i+=1
    elif(guess == user):
        print(f"You have successfully guess the number in {i} tries")   
        exit()         