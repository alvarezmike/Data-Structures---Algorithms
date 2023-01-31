def print_items(n):
    """"Representing O(n^2) with this function"""
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10) # In this case the number of operationss is 100

""" 
It doesn't matter if is O(n^3) or O(n^4) = It's simplified, rewritten as O(n^2)
"""