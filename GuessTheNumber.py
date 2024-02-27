import json
import random
from datetime import datetime

# Function to log the guess along with the lower and upper bounds
def log_guess(guess, target, lower_bound, upper_bound):   
    now = datetime.now()    
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")     
    # Constructing the data to be logged
    data = {"guess": guess, "target": target, "lower_bound": lower_bound, "upper_bound": upper_bound, "time": current_time}       
    # Appending the data to the log file
    with open("log.json", "a") as file:
        json.dump(data, file)
        file.write("\n")

# Function for guessing game
def guess_number():
    lower_bound = int(input(f"Enter the lower bound for the range: "))      
    upper_bound = int(input(f"Enter the upper bound for the range: "))      
    target_number = random.randint(lower_bound, upper_bound)    # Generating the target number within the given range

    try:
        while True:
            user_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))  # Getting user's guess
            log_guess(user_guess, target_number, lower_bound, upper_bound)  # Logging the guess along with bounds

            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Your guess is out of the range [{lower_bound}, {upper_bound}]. Try again.")  # Out of range message
            elif user_guess < target_number:
                print("Too low! Try a larger number.")  # Guess is too low
            elif user_guess > target_number:
                print("Too high! Try a smaller number.")  # Guess is too high
            else:
                print(f"Congratulations! You guessed the correct number: {target_number}")  # Correct guess message
                break

    except ValueError:
        print("Please enter an integer within the specified range.")  # Error message for non-integer inputs

    except Exception as e:
        print(f"Error: {e}")  # Printing unexpected errors

    finally:
        print("Game over!")  # End of the game

# Function to print the logs from the log file
def print_log():
    try:
        with open("log.json", "r") as file:
            data = file.readlines()
            print("Number guesses logged as follows:")
            for line in data:
                print(line.strip())  # Stripping newline characters and printing each line
    except FileNotFoundError:
        print("Log file not found.")  # Error message if the log file is not found
    except Exception as e:
        print(f"Error: {e}")  # Printing any other unexpected errors

if __name__ == "__main__":
    guess_number()  # Initiating the guessing game
    print_log()  # Printing the log after the game
