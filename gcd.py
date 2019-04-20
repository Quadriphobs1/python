# A simple python program that can find the greatest common divisor of two numbers
# Name: Quadri Adekunle


def gcd(a, b):
    x = min(a, b)

    while x > 1:
        if a % x == 0 and b % x == 0:
            return x
        else:
            x -= 1
    return "Has no gcd"


# test case
exp1 = gcd(12, 18)
print(exp1)

exp2 = gcd(32, 40)
print(exp2)

exp3 = gcd(18, 27)
print(exp3)

exp4 = gcd(18, 18)
print(exp4)

exp5 = gcd(18, 29)
print(exp5)

exp5 = gcd(66554545, 1565454)
print(exp5)
