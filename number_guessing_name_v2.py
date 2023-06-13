"""
Name: Matthew
Date Created: 5/18/2023
Description: Create a game that a user tries to guess the number
1) User selects number range (100 or greater)
2) Game randomly decides a number
3) Player is given 7 attempts
4) Tell the user if they are hot or cold -- Go to number_guessing_game_v2.py

Project URL: https://www.geeksforgeeks.org/number-guessing-game-in-python/
Python Projects: Beginner to Expert: https://www.geeksforgeeks.org/python-projects-beginner-to-advanced/
"""
#%%
# Imports

# 'random' is for the random number generator
import random

# Game beginning
intro = """
Hello and welcome to the number guessing game of the century!

Pick the range you want to guess from, can't do less than 100.
You then have seven guesses to figure out what the number is.

Enjoy
"""
# Print what we just wrote so that the user can be introduced to the game
print(intro)

# User input

# Let's create an input for the range the player wants to be guessing from
range = input("What range do you want to guess, 0 to ...")
# 'input' is a string, but we want an integer variable. We can use int(range) to do this
range_int = int(range)

"""
But what if the gamer wants to only have five numbers to choose from, guaranteeing
that they will win the game. We can't have that, so we make it so they can't have a
range smaller than 100. We can do this with a 'while' loop, so that as long as the 
inputted range is less than 100, the user will keep being asked to input a range
until it is above 100.
"""
while range_int < 100:
    print("You have inputted an invalid range. Please enter a number over 100")
    range_int = int(input("Please re-enter:"))

# Generating a random number

"""
Here is where we use the random number generator (random.random())
The randomly generated number is between 0 and 1, so we need to tell it to be 
between 0 and the user choosen range, which we do by multiplying the range by the 
randomly generated number. So now, instead being between 0 and 1, the random number
is between 0 and whatever the chosen range is. If the user chose 7,523, then the
random can be anything between 0 and 7,523.
As it stands, the number is going to be some floating-point, so 10.2361708087, but
we want a nice, round integer, 10 or 11. We can use 'int()' again, but instead of 
turning a string into an integer, we are turning a floating-point number into an
integer.
"""
rand_num = int(random.random() * range_int)
print(rand_num)

# Guessing time
guess = int(input("What is your first guess?"))

# Now let's compare the user's guess to the randomly generated number

# Set a value for 'i'
"""
Originally I had 'i' count up to 6, but then I need to create another variable
that counts down to show how many guesses are correct. So instead, I realized 
I can just have 'i' count down by setting it equal to the amount of guesses I 
wanted the gamer to have and then set the while loop to stop when 'i' reaches
0. The 'else' statement for when the user guesses incorrectly then subtracts 
1 from 'i' so that everytime a wrong guess is made, the amount of chances that 
someone can guess are reduced by one.
"""
i = 6

while i > 0:
    if guess == rand_num:
        print("Congradulations, you found the random number. Please play again soon.")
        break
    # If guess is 5 or less greater than rand_num then tell the close
    # '>=' greater than or equal to, '<=' less than or equal to
    if 0 < (guess - rand_num) <= 5:
        guess = int(input(f"You were close, but you were a little too high. You have {i} "
                          + "guesses left, please try again:"))
        i = i - 1
        
    if 4 < (guess - rand_num) <= 25:
        guess = int(input(f"Your guess was too high. You have {i} "
                          + "guesses left, please try again:"))
        i = i - 1

    if 24 < (guess - rand_num) <= 50:
        guess = int(input(f"You guessed way too high. You have {i} "
                          + "guesses left, please try again:"))
        i = i - 1

    if (guess - rand_num) > 50:
        guess = int(input("You guess was catestrophically high. For all that is good in this world, "
                          + f"please try agian and don't mess up as badly for your next {i} guesses:"))
        i = i - 1

    if 0 > (guess - rand_num) >= -5:
        guess = int(input(f"You were close, but you were a little too low. You have {i} "
                          + "guesses left, please try again:"))
        i = i - 1

    if 4 > (guess - rand_num) >= -25:
        guess = int(input(f"Your guess was too low. You have {i} "
                          + "guesses left, please try again:"))
        i = i - 1

    if -24 > (guess - rand_num) >= -50:
        guess = int(input(f"You guessed way too low. You have {i} "
                          + "guesses left, please try again:"))
        i = i - 1

    if (guess - rand_num) < -50:
        guess = int(input("You guess was astronomically low. For all that is holy, please "
                          + f"try agian and don't mess up as badly for your next {i} guesses:"))
        i = i - 1

    """else:
        # Tell the user they guessed incorrectly and to try again.
        # Use 'f' before a string and {} within that string to input a variable into that string
        guess = int(input(f"Sorry, you have not found the answer, {i} guesses remaining. Try again:"))
        # Add 1 to i so that it counts the amount of times
        i = i - 1"""
        
# Final statement to let the user know that they lost and to play again.
if guess != rand_num:
    print("You have used up all of your guesses. Please either restart the game, or exit.")

