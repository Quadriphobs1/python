# Removing duplicate item from a list
def remove_dups(L1, L2):
    L1_copy = L1[:]

    for i in L1_copy:
        if i in L2:
            L1.remove(i)
    return (L1, L2)


# Tests
L1 = [1, 2, 4, 5]
L2 = [1, 3, 2, 5]

(l1, l2) = remove_dups(L1, L2)

print(l1, l2)
