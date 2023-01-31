def print_items (n):
    """ O(n) = O(2n) function representaion, n equals the number of operations"""
    for  i in range (n):
        print(i)
    
    for  j in range (n):
        print(j)

print_items(10) # in this case, O(n) = 20 
