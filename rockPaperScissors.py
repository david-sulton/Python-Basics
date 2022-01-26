import random

#check if user's choice is rock, paper or scissors

def isChoiceCorrect(choice):

    options = ['rock', 'paper', 'scissors']

    if choice.lower() in options:
        return True
    else:
        return False

#Define question options yes or no
yesNoOptions = ['yes', 'no']

#ask the user if he/she knows how to play
userHow_to = input("\n\nHello! welcome to Rock, paper, Scissors. Do you know how to play?\n\n")

#Check if user's input is yes or no.
while userHow_to not in yesNoOptions:
    userHow_to = input("\n\nPlease write yes or no. Do you know how to play?\n\n")

#Explain instructions to user, or, proceed with game.
if userHow_to.lower() == 'no':
    print("\nYou have to choose and write an option: Rock, Paper or Scissors. Rock wins against scissors; paper wins against rock; and scissors wins against paper!\n ")
else:
    print("\nGreat! Let's play")


#loop game until user does not want to play anymore
while True:
    #take user's choice
    user_choice = input("\nNow, please write your choice:")

    #check if user has selected a valid option
    while True:
        if isChoiceCorrect(user_choice) == True:
            print("\nYou have chosen " + user_choice)
            break
        else:
            user_choice = input("\nYour selection is incorrect. Please choose one of the options:\n\nRock\n\nPaper\n\nScissors\n")
    
    #show user computers choice
    computerChoice = random.choice(['Rock', 'Paper','Scissors'])
    print("\nThe computer has chosen " + computerChoice + "\n")

    #Compare user's choice vs computer's choice
    if user_choice.lower() == computerChoice.lower():
            print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice.lower() == "rock":
        if computerChoice.lower() == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_choice.lower() == "paper":
        if computerChoice.lower() == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_choice.lower() == "scissors":
        if computerChoice.lower() == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    #Ask user if he/she wants to play again
    play = input("\n\nDo you want to keep playing? ")

    #Check if user's input is valid
    while play not in yesNoOptions:
        play = input("\n\nPlease write yes or no. Do you want to keep playing?\n\n")
    
    #stop the game if user does not want to play anymore
    if play.lower() == 'no':
        break
    
        

