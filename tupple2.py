def get_data(aTupple):
    nums = ()
    words = ()

    for t in aTupple:
        nums = nums + (t[0],)

        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)
    unique_words = len(words)
    return (min_n, max_n, unique_words)


test_data = ((1, 'a'), (2, 'b'), (1, 'a'), (7, 'b'))

(min_n, max_n, unique_words) = get_data(test_data)

print("min:", min_n, ", max:", max_n, ", unique word:", unique_words)


# test data with taylor swift songs
tswift = (
    (2014, 'Katy'),
    (2014, 'Harry'),
    (2012, 'Jake'),
    (2010, 'Taylor'),
    (2008, 'Joe'),
)

(tswift_min_year, tswift_max_year, tswift_num_people) = get_data(tswift)

print("From", tswift_min_year, "to", tswift_max_year,
      "Taylor swift wrote songs about", tswift_num_people)
