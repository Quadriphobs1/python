guess = 0.001

number = int(input("Enter number to find the square-root: "))

while (guess * guess) < number:
    guess = (guess + number / guess) / 2
print("Square root of " + str(number) + " is " + str(int(guess)))
