print("Number Guessing Game")
num = int(input("Guess a number (between 1 and 9): "))

while num != 5:
    if num < 5:
        print("Your guess was too low")
    else:
        print("Your guess was too high")
    num = int(input("Enter your guess: "))

print("Congratulations! You won!")