x = int(input("Enter a number: "))
ans = 0

itersLeft = x

while (itersLeft != 0):
    ans += x
    itersLeft -= 1

print(str(x) + "*" + str(x) + " = " + str(ans))
