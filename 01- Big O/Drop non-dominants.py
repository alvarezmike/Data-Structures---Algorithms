def print_items(n):
    """"Representing O(n^2) with this function"""
    for i in range(n):
        for j in range(n):
            print(i, j)  # In this case the number of operationss is 100

    for k in range(n):
        print(k)  # In this case the number of operations is 10


print_items(10)

"""
The above function is O(n^2 + n), but because n is a small portion, it's simply a drop non-dominant 
and rewritten as O(n^2)
"""
