import tkinter as tk
from tkinter import messagebox
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"You chose {user_choice}\nComputer chose {computer_choice}\n\n{result}")

def main():
    window = tk.Tk()
    window.title("Rock Paper Scissors")

    label = tk.Label(window, text="Choose rock, paper, or scissors:", font=("Helvetica", 14))
    label.pack(pady=10)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    def handle_choice(choice):
        play_game(choice)

    rock_button = tk.Button(button_frame, text="Rock", command=lambda: handle_choice('rock'), width=10, height=2, bg='sky blue', fg='black', font=("Helvetica", 12))
    rock_button.grid(row=0, column=0, padx=10)

    paper_button = tk.Button(button_frame, text="Paper", command=lambda: handle_choice('paper'), width=10, height=2, bg='light green', fg='black', font=("Helvetica", 12))
    paper_button.grid(row=0, column=1, padx=10)

    scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: handle_choice('scissors'), width=10, height=2, bg='light coral', fg='black', font=("Helvetica", 12))
    scissors_button.grid(row=0, column=2, padx=10)

    window.mainloop()

if __name__ == "__main__":
    main()
