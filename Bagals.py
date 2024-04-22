import random

# Set constant variables
NUMBER_DIGIT = 2
MAX_GUESSES = 12

def get_secret_num():
    # Generate a random secret number.
    numbers = list(range(10))
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUMBER_DIGIT):
        secret_num += str(numbers[i])
    return secret_num

def get_clues(guess, secret_num):
    # Generate clues based on the guess and the secret number.
    if guess == secret_num:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if not clues:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)

def main():
    prompt = f"""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {NUMBER_DIGIT}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say: That means:
Fermi One digit is correct and in the right position.
Pico One digit is correct but in the wrong position.
Bagels No digit is correct.

For example, if the secret number was 62 and your guess was 23, the clues would be Pico.
"""
    print(prompt)

    while True:
        secret_num = get_secret_num()
        print('I have thought of a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess = input('Guess #{}: '.format(num_guesses))
            if len(guess) != NUMBER_DIGIT or not guess.isdecimal():
                print('Please enter a {}-digit number.'.format(NUMBER_DIGIT))
                continue

            clues = get_clues(guess, secret_num)
            print(clues)

            if guess == secret_num:
                print('Congratulations! You guessed the number.')
                break
            num_guesses += 1
        else:
            print('Sorry, you ran out of guesses. The secret number was {}.'.format(secret_num))

        play_again = input('Do you want to play again? (yes or no) ').strip().lower()
        if play_again != 'yes':
            print('Thanks for playing!')
            break
# If the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()
