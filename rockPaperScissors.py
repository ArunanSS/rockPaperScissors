import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play_game("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play_game("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play_game("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(self.root, text="Score - You: 0 | Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "user"
        else:
            return "computer"

    def play_game(self, user_choice):
        computer_choice = self.get_computer_choice()
        winner = self.determine_winner(user_choice, computer_choice)

        if winner == "tie":
            self.result_label.config(text=f"It's a tie! You both chose {user_choice}.")
        elif winner == "user":
            self.result_label.config(text=f"You win! {user_choice} beats {computer_choice}.")
            self.user_score += 1
        else:
            self.result_label.config(text=f"You lose! {computer_choice} beats {user_choice}.")
            self.computer_score += 1

        self.score_label.config(text=f"Score - You: {self.user_score} | Computer: {self.computer_score}")

        if messagebox.askyesno("Play Again?", "Do you want to play again?") == False:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
