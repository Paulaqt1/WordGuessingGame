import tkinter as tk
from tkinter import messagebox
import random

class WordGuessingGame:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Python Keyword Guessing Game")
        self.master.geometry("600x600")
        self.master.configure(bg="#4682B4")  # Set background color
        self.show_start_screen()  # Show the start screen

        # Define Python keywords as the game's words and their clues
        self.keywords = {
            "and": "Logical AND operator",
            "as": "Used to create an alias",
            "assert": "Debugging tool",
            "break": "Exits a loop",
            "class": "Defines a class",
            "continue": "Skips remaining loop code",
            "def": "Defines a function",
            "del": "Deletes an object",
            "elif": "Else if condition",
            "else": "Alternative condition",
            "except": "Handles exceptions",
            "False": "Boolean false value",
            "finally": "Executes after try-except",
            "for": "Looping construct",
            "from": "Imports specific parts of a module",
            "global": "Declares a global variable",
            "if": "Conditional statement",
            "import": "Imports a module",
            "in": "Checks for membership",
            "is": "Checks object identity",
            "lambda": "Anonymous function",
            "None": "Represents nothing",
            "nonlocal": "Modifies parent function variable",
            "not": "Logical NOT operator",
            "or": "Logical OR operator",
            "pass": "Null statement",
            "raise": "Raises an exception",
            "return": "Returns a value from function",
            "True": "Boolean true value",
            "try": "Starts exception handling",
            "while": "Looping construct",
            "with": "Simplifies resource handling",
            "yield": "Generates a sequence"
        }

    def show_start_screen(self):
        # Create a frame for the start screen
        self.start_frame = tk.Frame(self.master, bg="#4682B4")
        self.start_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the frame

        # Title label for the game
        title_label = tk.Label(self.start_frame, text="Python Keyword Guessing Game", 
                                font=("Press Start 2P", 18, "bold"), bg="#4682B4", fg="white")
        title_label.pack(pady=10)  # Add padding

        # Start button to begin the game
        start_button = tk.Button(self.start_frame, text="Start", 
                                 font=("Press Start 2P", 14, "bold"), bg="black", fg="white", 
                                 command=self.start_game)
        start_button.pack(pady=20)  # Add padding

    def start_game(self):
        # Destroy the start screen and set up the main game UI
        self.start_frame.destroy()
        self.setup_ui()
        self.new_game()  # Start a new game

    def setup_ui(self):
        # Create the main frame for the game
        self.main_frame = tk.Frame(self.master, bg="#4682B4")
        self.main_frame.pack(expand=True, fill='both')  # Expand to fill the window

        # Title label for the guessing game
        self.title_label = tk.Label(self.main_frame, text="Guess the Python Keyword!", 
                                     font=("Press Start 2P", 18, "bold"), bg="#4682B4", fg="white")
        self.title_label.pack(pady=10)  # Add padding

        # Label to display the word to guess
        self.word_display = tk.Label(self.main_frame, text="", 
                                      font=("Press Start 2P", 24, "bold"), fg="white", bg="#4682B4")
        self.word_display.pack(pady=20)  # Add padding

        # Label to show the clue for the current word
        self.description_label = tk.Label(self.main_frame, text="", wraplength=400, 
                                           font=("Arial", 12, "italic"), bg="#4682B4", fg="white")
        self.description_label.pack(pady=5)  # Add padding

        # Label to show the number of attempts
        self.attempts_label = tk.Label(self.main_frame, text="Attempts: 0/5", 
                                        font=("Press Start 2P", 14), bg="#4682B4", fg="white")
        self.attempts_label.pack()  # Add padding

        # Frame for input elements
        self.input_frame = tk.Frame(self.main_frame, bg="#4682B4")
        self.input_frame.pack(pady=10)  # Add padding

        # Entry field for the user's guess
        self.guess_entry = tk.Entry(self.input_frame, width=25, font=("Arial", 14))
        self.guess_entry.pack(side=tk.LEFT, padx=5)  # Add padding
        self.guess_entry.bind("<Return>", self.process_guess)  # Bind Enter key to process guess

        # Button to submit the guess
        self.guess_button = tk.Button(self.input_frame, text="Guess", command=self.process_guess)
        self.guess_button.pack(side=tk.LEFT)  # Add padding

        # Button to start a new game
        self.new_game_button = tk.Button(self.main_frame, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=10)  # Add padding

    def new_game(self):
        # Start a new game by selecting a random keyword
        self.current_word = random.choice(list(self.keywords.keys()))  # Randomly choose a keyword
        self.guessed_letters = set()  # Reset guessed letters
        self.attempts = 0  # Reset attempts
        self.update_display()  # Update the display

    def update_display(self):
        # Display the word with guessed letters and underscores for the rest
        displayed_word = [letter if letter in self.guessed_letters else "_" for letter in self.current_word]

        # Update word display color based on game state
        if self.attempts >= 5:
            self.word_display.config(fg="red")  # Change color to red if attempts exceed 5
        elif all(letter in self.guessed_letters for letter in self.current_word):
            self.word_display.config(fg="yellow")  # Change color to yellow if the word is guessed
        else:
            self.word_display.config(fg="white")  # Default color

        # Update the displayed word and other labels
        self.word_display.config(text=" ".join(displayed_word))  # Show the current state of the word
        self.attempts_label.config(text=f"Attempts: {self.attempts}/5", fg="white")  # Update attempts label
        self.description_label.config(text=f'Clue: {self.keywords[self.current_word]}')  # Show clue

        # Check for win or loss conditions
        if all(letter in self.guessed_letters for letter in self.current_word):  # Check for correct guess
            messagebox.showinfo("Congratulations!", f"You guessed the word: {self.current_word}")
            self.new_game()  # Start a new game
        elif self.attempts >= 5:  # Check for game over condition
            messagebox.showinfo("Game Over", f"The correct word was: {self.current_word}")
            self.new_game()  # Start a new game

    def process_guess(self, event=None):
        # Process the user's guess
        guess = self.guess_entry.get().strip().lower()  # Get the guess and clean it
        self.guess_entry.delete(0, tk.END)  # Clear the entry field

        # Check if the guess is empty
        if not guess:
            return

        # If the guess is the entire word
        if guess == self.current_word:
            self.guessed_letters.update(set(self.current_word))  # Update the guessed letters
        else:
            # Only increment attempts if the guess is incorrect
            self.attempts += 1

        # Update the display based on the new state
        self.update_display()


# Using all keywords in the code
if __name__ == "__main__":
    try:
        # Creating the root window
        root = tk.Tk()

        # Create an instance of the game
        game = WordGuessingGame(root)
        
        # Start the main loop of the Tkinter GUI
        root.mainloop()

    except Exception as e:
        # Handling any exception that occurs
        print(f"An error occurred: {e}")

    finally:
        # Cleanup actions if needed
        print("Game over or exited")