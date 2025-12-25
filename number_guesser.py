import random  # importing random module this is called module

top_of_range = input("Type a number: ")

# although our number is string, but we can check whether it is a digit or not
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

# r = random.randrange(start, stop)
random_number = random.randrange(top_of_range)
number_of_guesses = 0
while True:
    number_of_guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", number_of_guesses, "guesses")
