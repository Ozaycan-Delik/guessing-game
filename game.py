import 

def play_game():
    lower_bound = 1
    upper_bound = 1000
    max_attempts = 10
    secret_number = random.randint(lower_bound, upper_bound)

    def get_guess():
        while True:
            try:
                guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
                if lower_bound <= guess <= upper_bound:
                    return guess
                else:
                    print("Invalid input. Please enter a number within the specified range.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def check_guess(guess, secret_number):
        if guess == secret_number:
            return "Correct"
        elif guess < secret_number:
            return "Too low"
        else:
            return "Too high"

    def
    
