class Cookie:
    def __init__(self, color):
        self.color = color
# code above is the constructor

# code below are the methods
    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


# creating two objecs of Cookie
cookie_one = Cookie("green")
cookie_two = Cookie("red")

print("Cookie one is ", cookie_one.get_color())
print("Cookie two is ", cookie_two.get_color())


# Now will change the color of cookie_one with set_color function
cookie_one.set_color("yellow")
print("Now the color of cookie_one is", cookie_one.get_color())
