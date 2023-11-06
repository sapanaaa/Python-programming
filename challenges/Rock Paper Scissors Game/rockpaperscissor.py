import random

#user's choice part
def get_userchoice():
   while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
           

#computer's choice part
def get_compchoice():
    choices=['rock','paper','scissors']
    return random.choice(choices)

#game part
def winner(user_choice, computer_choice):
    if( user_choice==computer_choice): return "its a tie"
    
    elif( 
        (user_choice=='rock'and computer_choice=='scissors') or
        (user_choice=='scissors'and computer_choice=='paper' )or
        (user_choice=='paper'and computer_choice=='rock')
        ): return "congrats, you win"
    
    else: return "oops, computer won"
    



#main part
def main():
    print("!!ROCK PAPER & SCISSORS!!")
while True: 
    user_choice=get_userchoice() 
    computer_choice=get_compchoice()   

    print(f"your choice is :{user_choice}")
    print(f"computer's choice is:{computer_choice}" )

    result= winner(user_choice,computer_choice)
    print(result)

    playAgain= input("Do you want to play again?(yes/no):").strip().lower()
    if (playAgain !='yes'): break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
