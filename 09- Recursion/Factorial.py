
# A factorial number is : 4! = 4 x 3 x 2 x 1
def factorial(n):
    if n ==1:
        return 1
    return n * factorial(n -1)

print(factorial(4))

