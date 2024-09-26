# game for two
while True:
    # handling exceptions https://docs.python.org/3/tutorial/errors.html#handling-exceptions
    try:
        secret = input("Player A enter number")
        secret = int(secret)
        print("This means integer was entered", secret)
        break # this break is only reached when secret was successfully converted
    except ValueError:
        print("not an integer! please try again")
        # so here continue is not required because we are still going back to the start
        # of while loop
    #     continue
    # print("This means integer was entered", secret) # of course in a game setting
    # # secret should not be shown on a screen :)
    # break # so this means we have made a valid secret that means we can break first loop

guess = None
num_guesses = 0

# we start a new loop for second player
while guess != secret: # we keep playing as long as guess is not equal to secret
    guess = input("What is your guess Player B? (q to give up) ")
    if guess == "q" or guess == "Q":  # there are other ways of doing this checking
        print("We give up")
        break
    try:
        guess = int(guess)  # we convert AFTER checking for q
    except ValueError:
        print("not an integer! please try again")
        continue # we back to start of THIS while loop - line 22
    num_guesses += 1 # our gusses counter
    if guess < secret:
        print("Your guess is less than secret")
    elif guess > secret:
        print("Your guess is more than secret")
# this is where the loop is already ended
print("So the secret number was", secret)
print(f"You took {num_guesses} tries")
# this code could always be improved, for example we could track the number of guesses