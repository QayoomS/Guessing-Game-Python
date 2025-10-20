import random
r_int = random.randint(1, 5)
guess_left = 3
print('Welcome to the number guessing game')

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