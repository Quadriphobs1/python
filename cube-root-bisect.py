cube = float(input("Enter the number to find the cube root: "))
epsilon = 0.01
num_guesses = 0
low = 0
high = max(1.0, cube)

guess = (high + low)/2.0


def diff(cube, guess):
    guess_cube = abs(guess**3)
    if (cube > guess_cube):
        return (cube - guess_cube)
    else:
        return (guess_cube - cube)


while diff(cube, guess) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1

print('Number of guesses =', num_guesses)
print(guess, ' is close to the cube root of ', cube)
