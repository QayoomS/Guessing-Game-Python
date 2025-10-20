# import library:
import random
# We can chose the range of number that user can select:
r_int = random.randint(1, 5)

# Let give them 3 chance:
guess_left = 3

# A simple welcome message will be good:
print('Welcome to the number guessing game')

# using loops for the game:
while guess_left >= 1:
    print('Guesses Left: ', guess_left)
    my_int = int(input('Guess a integer between 1 and 5:  '))
    guess_left -= 1
    if r_int == my_int:
        print('congratulatioin, you win!')
        break
    else:
        print('Better Luck next time!')

print('the game is over. Restart the program to play again!')
