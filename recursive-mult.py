def mult(a, b):
    if b == 1:
        return a
    else:
        return a + mult(a, b-1)


# Test case

print(mult(2, 3))

print(mult(10, 34))
