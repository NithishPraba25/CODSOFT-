import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice=='rock' and computer_choice=='scissors') or (player_choice=='scissors' and computer_choice=='paper') or (player_choice=='paper' and computer_choice=='rock'):
         return "You win"
    else:
        return "Computer wins"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")

    player_choice = input("Enter rock, paper, or scissors: ").lower()
    if player_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice Please try again")
        return  

    computer_choice = get_computer_choice()
    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(player_choice, computer_choice)
    print(result)

play_game()
