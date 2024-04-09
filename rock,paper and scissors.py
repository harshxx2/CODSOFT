import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock,paper,scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose {user_choice} and the computer chose {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == 'user':
            print("You win!")
            user_score += 1
        elif result == 'computer':
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Your score: {user_score}, Computer score: {computer_score}")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            break

if __name__ == "__main__":
    main()