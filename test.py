import json
import random
from datetime import datetime

def log_guess(guess, target):   
    now = datetime.now()    
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")     
    data = {"guess": guess, "target": target, "time": current_time}       

    with open("log.json", "a") as file:
        json.dump(data, file)
        file.write("\n")        

def guess_number():
    lower_bound = int(input(f"Enter the lower bound for the range: "))      
    upper_bound = int(input(f"Enter the upper bound for the range: "))      
    target_number = random.randint(lower_bound, upper_bound)    

    try:
        while True:
            user_guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            log_guess(user_guess, target_number)       

            if user_guess < lower_bound or user_guess > upper_bound:
                print(f"Your guess is out of the range [{lower_bound}, {upper_bound}]. Try again.")
            elif user_guess < target_number:
                print("Too low! Try a larger number.")
            elif user_guess > target_number:
                print("Too high! Try a smaller number.")
            else:
                print(f"Congratulations! You guessed the correct number: {target_number}")
                break

    except ValueError:
        print("Please enter an integer within the specified range.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Game over!")

def print_log():
    try:
        with open("log.json", "r") as file:
            data = file.readlines()
            print("Number guesses logged as follows:")
            for line in data:
                print(line.strip())
    except FileNotFoundError:
        print("Log file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    guess_number()
    print_log()