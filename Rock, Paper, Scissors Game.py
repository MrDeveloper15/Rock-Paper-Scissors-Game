import random
import tkinter as tk

# Game logic
choices = ['Rock', 'Paper', 'Scissors']
score = {'Player': 0, 'Computer': 0}

def play(choice):
    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)
    
    # Display results
    result_label.config(text=f"Player: {choice}, Computer: {computer_choice}\n{result}")
    
    # Update score
    if result == "You win!":
        score['Player'] += 1
    elif result == "You lose!":
        score['Computer'] += 1
    score_label.config(text=f"Player: {score['Player']}, Computer: {score['Computer']}")

def determine_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == 'Rock' and computer == 'Scissors') or \
         (player == 'Scissors' and computer == 'Paper') or \
         (player == 'Paper' and computer == 'Rock'):
        return "You win!"
    else:
        return "You lose!"

# Create main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Display result
result_label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=('Helvetica', 14))
result_label.pack()

# Display score
score_label = tk.Label(window, text="Player: 0, Computer: 0", font=('Helvetica', 14))
score_label.pack()

# Buttons for choices
for choice in choices:
    tk.Button(window, text=choice, command=lambda c=choice: play(c)).pack()

window.mainloop()
