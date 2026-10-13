import random  # I need this to make a random number

random_number = random.randint(1, 10)  # get a random number from 1 to 10
previous_guesses = []  # empty list for the guesses
correct_answer_picked = False  # te player has not won yet

while correct_answer_picked == False:  # keep going til they win
    user_guess = int(input("Enter a number between 1 - 10: "))  # ask for a number and make it an integer

    while user_guess < 1 or user_guess > 10 or user_guess in previous_guesses:  # keep asking if the guess is bad
        if user_guess in previous_guesses:  # check if they already guessed it
            print("You already guessed", user_guess, "!")  # tell them it was already guessed
            print("Choose a different number.")  # tell them to pick another one
            print("Previous guesses:", previous_guesses)  # show the list
        else:  # if not, it must be out of range
            print("Invalid input!")  # tell them it is invalid
        user_guess = int(input("Enter a number between 1 - 10: "))  # ask again

    previous_guesses.append(user_guess)  # the guess is good so add it to the list

    if user_guess == random_number:  # the guess is right
        print("You guessed correctly! The number was", random_number)  # tell them they won
        print("Your guesses:", previous_guesses)  # show all the guesses
        correct_answer_picked = True  # this stops the game loop
    elif user_guess > random_number:  # the guess is too big
        print("Try again! The random number is lower!")  # tell them to go lower
        print("Previous guesses:", previous_guesses)  # show the list
    else:  # the guess is too small
        print("Try again! The random number is higher!")  # tell them to go higher
        print("Previous guesses:", previous_guesses)  # show the list