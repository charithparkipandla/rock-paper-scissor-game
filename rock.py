import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle the user's choice
def user_choice(choice):
    # Update user label
    user_label.config(text=f"You chose: {choice.capitalize()}")

    # Randomly choose the computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    computer_label.config(text=f"Computer chose: {computer_choice.capitalize()}")

    # Determine the result
    result = determine_winner(choice, computer_choice)
    result_label.config(text=result)

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x400")
root.config(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Rock, Paper, Scissors Game", font=("Helvetica", 18), bg="#f0f0f0", fg="#333")
title_label.pack(pady=20)

# User choice label
user_label = tk.Label(root, text="You chose: ", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
user_label.pack(pady=10)

# Computer choice label
computer_label = tk.Label(root, text="Computer chose: ", font=("Helvetica", 12), bg="#f0f0f0", fg="#333")
computer_label.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 16), bg="#f0f0f0", fg="#333")
result_label.pack(pady=20)

# Create buttons for each choice
rock_button = tk.Button(root, text="Rock 🪨", font=("Helvetica", 14), bg="#4CAF50", fg="white", width=20, command=lambda: user_choice("rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper 📄", font=("Helvetica", 14), bg="#2196F3", fg="white", width=20, command=lambda: user_choice("paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors ✂️", font=("Helvetica", 14), bg="#FF5722", fg="white", width=20, command=lambda: user_choice("scissors"))
scissors_button.pack(pady=5)

# Run the application
root.mainloop()
