import random
def player_name():
    name = input("Register your name to play\n")
    print(f"Hi {name}")
    return name
def get_comp_choice():
    computer_choice1 = random.randrange(1,7)
    computer_choice2 = random.randrange(1,7)
    computer_choice = (computer_choice1 or computer_choice2)
    return computer_choice
def get_user_choice():
    player_choice = int(input("Enter your choice: (from 1 - 6)"))
    if (player_choice<1 or player_choice>6):
        print("Wrong input\n")
        get_user_choice()
    return player_choice
def toss():
    print("Let's toss :")
    choices = ["heads","tails"]
    match_choice = ["bat","ball"]
    coin_flip = random.choice(choices)
    player_input = input("Choose [heads/tails] ")
    while player_input not in choices:
        print("Wrong input\n")
        toss()
    if (coin_flip == player_input):
        print("Congratulations! You won the toss...")
        match_choice_user = input("You want to bat or ball?  ")
    else:
        match_choice_user = random.choice(match_choice)  
        print("Srry skipper! Computer won the toss\nYou have to",match_choice_user,"first")
    return match_choice_user
def overs():
    over_entry = int(input("Enter how many overs match do you want to play :\n"))
    return over_entry
def main():
    
    user = player_name()
    over_number = overs()
    a = toss()
    print(f"Let's go to the match\nBest of luck {user}")
    score = 0
    if (a == "bat"):   
        print("You are batting now...")
        wicket1 = 10     
        
        for i in range(over_number):
            for j in range(6):
                if(wicket1>0):
                        
                        player_user_batting = get_user_choice()
                        player_computer_bowling = get_comp_choice()
                        print(f"\nYou played : {player_user_batting}\tComputer played : {player_computer_bowling}")
                        if (player_user_batting == player_computer_bowling):
                            wicket1 -= 1
                            print("Wicket!!")
                            print(f"{wicket1} left")
                        else:
                            score += player_user_batting
                          
            wicket_taken1 = 10 - wicket1
            target = score
            print(f"Your total : {score}/{wicket_taken1}\nOvers : {i+1}")            
        
        print(f"Computer has to  score {score} runs in {over_number}") 
        wicket2 = 10
        print("You are bowling now...")
        for i in range(over_number):
                
                if(i>over_number):
                    chase1 = target - score
                    print(f"You win by {chase1} runs")
                for j in range(6):
                    if(wicket2>0 and score>0):
                        player_user_bowling2 = get_user_choice()
                        player_computer_batting2 = get_comp_choice()
                        print(f"\nComputer played : {player_computer_batting2}\tYou played : {player_user_bowling2}")
                        if (player_computer_batting2 == player_user_bowling2):
                            wicket2 -= 1
                            print("Wicket!!")
                            print(f"{wicket2} left")
                        else:
                            score -= player_computer_batting2
                        wicket_taken2 = 10 - wicket2                    
                        chase = target - score
                           
                    elif(wicket2<=0 or score > 0 ):
                        print(f"Computer's total : {chase}/{wicket_taken2}")
                        print(f"You win by {score} runs")
                        exit()
                    elif(score<=0 and wicket2>0):
                        print(f"Computer's total : {chase}/{wicket_taken2}")
                        print(f"Computer wins by {wicket2} wickets")        
                        exit()
                over_left = over_number - i-1
                if(score>=0):
                    print(f"Computer's total : {chase}/{wicket_taken2}\nComputer needs {score} in {over_left*6} balls")
                elif(score<0):
                    print(f"Computer's total : {chase}/{wicket_taken2}\nComputer needs {score} in {over_left*6} balls")
        if(wicket2<=0 or score > 0 ):
            print(f"You win by {score} runs")
        elif(score<=0 and wicket2>0):
            print(f"Computer wins by {wicket2} wickets")        
        elif(wicket2>0 and score == 1):
            print("Match draw ")    

   
    elif (a == "ball"):
        print("You are bowling now...")
        wicket = 10
        for i in range(over_number):
            for j in range(6):
                
                if(wicket>0):
                    player_computer_batting = get_comp_choice()
                    player_user_bowling = get_user_choice()
                    print(f"\nComputer played : {player_computer_batting}\tYou played : {player_user_bowling}")
                    if (player_computer_batting == player_user_bowling):
                        wicket -= 1
                        print("Wicket!!")
                        print(f"{wicket}left")
                    else:
                        score += player_computer_batting
            wicket_taken = 10 - wicket
            target = score
            print(f"Computer : {score}/{wicket_taken}\nOvers : {i+1}")            
        print(f"You have to score {score} runs in {over_number} overs")
        wicket2 = 10
        print("You are batting now...")
        for i in range(over_number):
                
                if(i>over_number):
                    chase1 = target - score
                    print(f"Computer wins by {chase1} runs")
                for j  in range(6):
                    if(wicket2>0 and score>0):
                        player_user_batting2 = get_user_choice()
                        player_computer_bowling2 = get_comp_choice()
                        print(f"\nYou played : {player_user_batting2}\tComputer played : {player_computer_bowling2}")
                        if(player_computer_bowling2 == player_user_batting2 ):
                            wicket2 -=1
                            print("Wicket!!!")
                            print(f"{wicket2}left")
                        else:
                            score -= player_user_batting2
                        wicket_taken2 = 10 - wicket2
                        chase = target - score
                    elif(wicket2<=0 or score > 0 ):
                        print(f"Your total : {chase}/{wicket_taken2}")
                        print(f"Computer wins by {score} runs")
                        exit()
                    elif(score<=0 and wicket2>0):
                        print(f"Your total : {chase}/{wicket_taken2}")
                        print(f"You win by {wicket2} wickets")  
                        exit()
                        
                over_left = over_number - i -1
                if(score>=0):
                    print(f"Your total : {chase}/{wicket_taken2}\nYou need {score} runs in {over_left*6} balls")  
                elif(score<0):          
                    print(f"Your total : {chase}/{wicket_taken2}\nYou need 0 runs in {over_left*6} balls") 
        if(wicket2<=0 or score > 0 ):
            print(f"Computer wins by {score} runs")
        elif(score<=0 and wicket2>0):
            print(f"You win by {wicket2} wickets") 
        elif(wicket2>0 and score == 1):
            print("Match draw ")       
    play_choice = input("Do you want to play another match? [y/n] ")
    if (play_choice == "y" or play_choice == "Y"):
        main()
    elif(play_choice == "n" or play_choice == "N"):
        print("Pleasure to having you in the PYTHON CRICKET CUP\n")
        exit()



print("***WELCOME TO THE PYTHON CRICKET CUP***")
main()
                    
                    