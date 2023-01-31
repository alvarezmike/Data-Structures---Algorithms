def print_items(a, b):
    """Function to represent different terms for inputs """
    for i in range(a):
        print(i)  # this is O(a)

    for j in range(b):
        print(j)  # this is O(b)


"""
In essence, I would write the above function as O(a + b), because it has different terms which are a and b.
"""
# ================================================================
# Example 2


def print_items_times(a, b):
    """Function to represent different terms for inputs """
    for i in range(a):
        for j in range(b):
            print(i, j)


"""
In essence, I would write the above function as O(a * b), because it is nested
and has different terms which are a and b.
"""
