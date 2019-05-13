# Problem Set 4A
# Name: Quadri Adekunle
# Collaborators:
# Time Spent: x:xx


# def swap(arr, idx1, idx2):
#     arr[idx1], arr[idx2] = arr[idx2], arr[idx1]


# def permutate(sequence_list, n):
#     if n == 1:
#         print(''.join(sequence_list))
#         return

#     for i in range(1, n):
#         swap(sequence_list, i, n-1)
#         permutate(sequence_list, n-1)
#         swap(sequence_list, i, n-1)


# def get_permutations(sequence):
#     '''
#     Enumerate all permutations of a given string

#     sequence (string): an arbitrary string to permute. Assume that it is a
#     non-empty string.

#     You MUST use recursion for this part. Non-recursive solutions will not be
#     accepted.

#     Returns: a list of all permutations of sequence

#     Example:
#     >>> get_permutations('abc')
#     ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

#     Note: depending on your implementation, you may return the permutations in
#     a different order than what is listed here.
#     '''

#     if len(sequence) == 1:
#         return sequence
#     else:
#         sequence_list = list(sequence)
#         permutate(sequence_list, len(sequence_list))

def permutate(sequence_list):
    list_len = len(sequence_list)

    if list_len == 0:
        return []

    if list_len == 1:
        return [sequence_list]

    l = []

    for i in range(list_len):
        m = sequence_list[i]

        rem_list = sequence_list[:i] + sequence_list[i+1:]
        for p in permutate(rem_list):
            l.append(''.join(m + ''.join(p)))
    return l


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    sequence_list = list(sequence)
    return permutate(sequence_list)


if __name__ == '__main__':
    #    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)

    example_input = 'amz'
    print('Input:', example_input)
    print('Expected Output:', ['amz', 'azm', 'maz', 'mza', 'zam', 'zma'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'asdf'
    print('Input:', example_input)
    print('Actual Output:', get_permutations(example_input))
