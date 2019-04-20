t = (2, 'tupple', 4)

print(t[0:1])


# Using tupple to swap values
x = 10
y = 12

(x, y) = (y, x)

print("swapped value", x, y)


def quotient_and_remainder(x, y):
    q = x // y
    r = x % y

    return (q, r)


(quot, rem) = quotient_and_remainder(4, 5)
print("Quotient and remainder of 4 and 5 are ", quot, rem)
