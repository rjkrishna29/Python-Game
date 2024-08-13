import random
def get_comp_choice():
    choices = ["rock","paper","scissors"]
    computer_choice = random.choice(choices)
    return computer_choice
def get_user_choice():
    player_choice = input("Choose rock , paper or scissors: ")
    choices = ["rock","paper","scissors"]
    while player_choice not in choices:
        print("Wrong input\n")
        get_user_choice()
    return player_choice
def play_round():
    user_choice = get_user_choice()
    comp_choice = get_comp_choice()
    print("Your choose :",user_choice,"\nComputer choose : ",comp_choice)
    if (user_choice==comp_choice):
        point = 0
    elif (user_choice == "rock"):
        if (comp_choice == "scissors"):
            point = 1
        else:
            point = -1
    elif(user_choice == "paper"):
        if(comp_choice == "rock"):
            point = 1
        else:
            point = -1
    elif(user_choice=="scissors"):
        if(comp_choice=="paper"):
            point = 1
        else:
            point = -1
    return point
def main():
    point_user = 0
    point_computer = 0
    for i in range(3):
        points = play_round()
        if points == 1:
            point_user+=1
        elif points == -1:
            point_computer+=1
    if (point_user > point_computer):
        print("You win!!!")
    elif(point_user<point_computer):
        print("Computer wins!!!")
    else:
        print("It's a Tie!!!")                    
    print("Your Score: ",point_user,"\nComputer Score: ",point_computer)    


main()
