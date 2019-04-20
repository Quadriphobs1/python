a_list = []

L = [2, 'a', 4, [1, 2]]

print(len(L))

print(L[0])

print(L[2] + 1)

print(L)


# add element to the end of a list
L.append(3)
L.append("4df")


# to mutate a list
L.extend([10, 20])


# Remove element from a list with its first occurence
L.remove('a')

# Remove element from a list using the index
del(L[3])


# Remove element from the end of a list and return the item removed
L.pop()
