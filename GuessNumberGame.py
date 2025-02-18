import random
import tkinter as tk
from tkinter import messagebox

class GuessNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")

        # Initialize game variables
        self.secret_number = None
        self.attempts = 0
        self.max_attempts = 10
        self.previous_guesses = []

        # Creating UI components
        self.label = tk.Label(root, text="Enter the range of numbers:")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.min_label = tk.Label(root, text="Minimum number:")
        self.min_label.grid(row=1, column=0, pady=5)
        self.min_entry = tk.Entry(root)
        self.min_entry.grid(row=1, column=1, pady=5)

        self.max_label = tk.Label(root, text="Maximum number:")
        self.max_label.grid(row=2, column=0, pady=5)
        self.max_entry = tk.Entry(root)
        self.max_entry.grid(row=2, column=1, pady=5)

        self.attempts_label = tk.Label(root, text="How many guesses would you like?")
        self.attempts_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.guesses_entry = tk.Entry(root)
        self.guesses_entry.grid(row=4, column=0, columnspan=2, pady=5)

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Labels that will be hidden before the game starts
        self.guess_label = tk.Label(root, text="")
        self.guess_label.grid(row=6, column=0, columnspan=2, pady=10)

        self.entry = tk.Entry(root)
        self.entry.grid(row=7, column=0, columnspan=2, pady=5)
        self.entry.grid_forget()  # Hide until the game starts
        self.guess_button = tk.Button(root, text="Guess!", command=self.check_guess)
        self.guess_button.grid(row=8, column=0, columnspan=2, pady=10)
        self.guess_button.grid_forget()  # Hide until the game starts

        # Initially hide attempts and previous guesses information
        self.attempts_label_display = tk.Label(root, text="")
        self.attempts_label_display.grid(row=9, column=0, columnspan=2, pady=5)

        self.previous_guesses_label = tk.Label(root, text="")
        self.previous_guesses_label.grid(row=10, column=0, columnspan=2, pady=5)

    def start_game(self):
        """Start the game with user-defined range and attempts."""
        try:
            # Get the range from the user
            min_num = int(self.min_entry.get())
            max_num = int(self.max_entry.get())

            if min_num >= max_num:
                raise ValueError("Minimum number must be less than maximum number.")

            # Get the number of guesses from the user
            try:
                self.max_attempts = int(self.guesses_entry.get())
                if self.max_attempts <= 0:
                    raise ValueError("Please enter a positive number of guesses.")
            except ValueError:
                messagebox.showerror("Error", "Invalid input for number of guesses.")
                return
            
            # Set the secret number within the user-defined range
            self.secret_number = random.randint(min_num, max_num)
            self.attempts = 0
            self.previous_guesses = []
            self.guess_label.config(text=f"Guess the number between {min_num} and {max_num}!")
            self.attempts_label_display.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
            self.previous_guesses_label.config(text="Previous guesses: ")

            # Hide the range inputs and start button
            self.min_entry.grid_forget()
            self.max_entry.grid_forget()
            self.min_label.grid_forget()
            self.max_label.grid_forget()
            self.guesses_entry.grid_forget()
            self.attempts_label.grid_forget()
            self.start_button.grid_forget()

            # Show the guess input and buttons
            self.entry.grid(row=7, column=0, columnspan=2, pady=5)
            self.guess_button.grid(row=8, column=0, columnspan=2, pady=10)

            # Show attempts and previous guesses after starting the game
            self.attempts_label_display.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
            self.previous_guesses_label.config(text="Previous guesses: ")

        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def check_guess(self):
        """Check the user's guess and provide feedback."""
        try:
            # Get the guess from the user
            guess = int(self.entry.get())
            self.attempts += 1
            self.previous_guesses.append(guess)
            self.entry.delete(0, tk.END)

            # Update the UI
            self.attempts_label_display.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")
            self.previous_guesses_label.config(text=f"Previous guesses: {', '.join(map(str, self.previous_guesses))}")

            # Check if the guess is correct and provide hints
            if guess < self.secret_number:
                self.guess_label.config(text="My number is higher!")
            elif guess > self.secret_number:
                self.guess_label.config(text="My number is lower!")
            else:
                self.guess_label.config(text=f"You guessed it! The number was {self.secret_number}.")
                self.show_end_message()
                return

            # Provide additional hint about whether the number is even or odd
            if self.secret_number % 2 == 0:
                self.guess_label.config(text=f"My number is even. {self.guess_label.cget('text')}")
            else:
                self.guess_label.config(text=f"My number is odd. {self.guess_label.cget('text')}")

            # If the user has reached the max attempts
            if self.attempts >= self.max_attempts:
                self.guess_label.config(text="You've reached the maximum number of attempts!")
                self.show_end_message()

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

    def show_end_message(self):
        """End game with a message."""
        response = messagebox.askyesno("Play again?", "Would you like to play again?")
        if response:
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        """Reset the game."""
        # Reset the UI components to their initial state
        self.secret_number = None
        self.attempts = 0
        self.previous_guesses = []

        # Show range inputs and start button again
        self.min_label.grid(row=1, column=0, pady=5)
        self.max_label.grid(row=2, column=0, pady=5)
        self.min_entry.grid(row=1, column=1, pady=5)
        self.max_entry.grid(row=2, column=1, pady=5)
        self.guesses_entry.grid(row=4, column=0, columnspan=2, pady=5)
        self.attempts_label.grid(row=3, column=0, columnspan=2, pady=10)
        self.start_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Hide game-specific UI components
        self.entry.grid_forget()
        self.guess_button.grid_forget()
        self.attempts_label_display.config(text="")
        self.previous_guesses_label.config(text="")
        self.guess_label.config(text="")

        # Remove the extra label that appears after restarting the game
        self.label.grid_forget()

        # Show range inputs and start button again
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

# Create Tkinter window
root = tk.Tk()
game = GuessNumberGame(root)
root.mainloop()
