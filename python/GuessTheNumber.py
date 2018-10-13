import random
min = 0
max = input('Generate number between 0 and ?')
SecretInterger = random.randint(min, max)

UserGuess = 'number'

while UserGuess != SecretInterger:
    print('Guess a number between 0 and')
    print (max)
    UserGuess = int(input('Your Guess?'))
    if UserGuess == SecretInterger:
        print('Wow! You guessed correctly!')
    elif UserGuess < SecretInterger:
        print('You guessed too low. Try Again')
    elif UserGuess > SecretInterger:
        print('You guessed too high. Try Again')
