cube = int(input("Enter a number u want to cube: "))

for guess in range(abs(cube + 1)):
    if guess ** 3 == abs(cube):
        break
if guess ** 3 != abs(cube):
    print(cube, " is not a perfect cube")
else:
    if cube < 0:
        guess = - guess
    print(" CUbe root of ", cube, " is ", guess)
