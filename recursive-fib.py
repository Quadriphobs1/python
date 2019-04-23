def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


print(fib(34))


def fib_2(n):
    if n <= 3:
        return n
    else:
        return fib_2(n-1) + fib_2(n-2)


print(fib_2(34))


def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans


d = {1: 1, 2: 2, 3: 3, 4: 5}

print(fib_efficient(34, d))
