num1 = 11
num2 = num1

print("Before num 2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))


num2 = 22

print("\nAfter num 2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)


print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

"""
Integers are immutable, which means they cannot be changed, once you put number 11 into
a particular space in memory it cannot be changed. Hence when num2 is changed to another integer
it's id points to another memory space but at first it was potining to the same id as num1 
because num2 value was equal to num1.
"""
