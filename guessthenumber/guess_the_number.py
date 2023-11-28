import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        guess = int(input("Make a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

    if attempts == max_attempts and guess != number_to_guess:
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_the_number()
