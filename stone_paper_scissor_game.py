def generate_computer_choice():
    import random
    return random.randrange(0,3)
    
def check_win_lose(player_choice,computer_choice):
   
    print(f"Player Choose : {player_choice}\t\tComputer Choice : {computer_choice}")
    if((player_choice==0 and computer_choice == 2)or(player_choice==2 and computer_choice==1)or(player_choice==1 and computer_choice==0)):
        print(f"Player Wins!\n")
    elif(player_choice==computer_choice):
        print(f"It's a tie\n")  
    else:
        print(f"Computer Wins!\n")     


def play():
    
    player_choice = int(input(f"Player 1 turn: Rock(0) Paper(1) Scissor(2)? \n"))
    computer_choice = generate_computer_choice()
    if(player_choice<0 or player_choice>2):
        print("Enter correct choice")
        play()
    else:
        check_win_lose(player_choice,computer_choice)
        

def rock_paper_scissor_game():
    play()
    continuation = input("Do you want to continue[y/n] ")
    if(continuation == "y" or continuation =="Y"):
        rock_paper_scissor_game()
    elif(continuation == "n" or continuation =="N"):
        cont = input("Do you want to exit?\nYes[y]\tNo[n]\n")
        if (cont == "y" or cont == "Y"):
            exit()
        elif(cont == "n" or cont =="N"):
            rock_paper_scissor_game()        
    
# game page starts from here
print("!!!Let's play Rock-Paper-Scissors!!!\n")
rock_paper_scissor_game()
    




