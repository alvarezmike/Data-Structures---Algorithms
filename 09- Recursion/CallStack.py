def functThree():
    print("Three")

def funcTwo():
    functThree()
    print("Two")

def funcOne():
    funcTwo()
    print("One")


funcOne()

# simple  program to visualize order of call stacks