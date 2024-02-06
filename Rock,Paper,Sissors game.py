import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while True:
            user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
            if user_choice in self.choices:
                return user_choice
            else:
                print("Invalid choice. Please choose rock, paper, or scissors.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            return "user"
        else:
            return "computer"

    def display_result(self, user_choice, computer_choice, winner):
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("Congratulations! You win!")
        else:
            print("Sorry, you lose.")

    def update_scores(self, winner):
        if winner == "user":
            self.user_score += 1
        elif winner == "computer":
            self.computer_score += 1

    def display_scores(self):
        print(f"Your score: {self.user_score}")
        print(f"Computer's score: {self.computer_score}")

    def play_again(self):
        return input("Do you want to play again? (yes/no): ").lower() == "yes"

    def play(self):
        print("Welcome to Rock, Paper, Scissors!")

        while True:
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()
            winner = self.determine_winner(user_choice, computer_choice)
            self.display_result(user_choice, computer_choice, winner)
            self.update_scores(winner)
            self.display_scores()

            if not self.play_again():
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()
