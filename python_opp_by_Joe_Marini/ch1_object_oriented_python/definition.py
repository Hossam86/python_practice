# Python Object-Oriented Programming by Joe Marini
# Basic class definition


# TODO: create a basic class
# parentheses are optional  after your class name but they're only really required if you're
# going to indicate that the class inherits from another class. class Book():
class Book:
    def __init__(self, title):
        self.title = title
    pass


# TODO: create instances of the class
b1 = Book("Atomic habits")
b2 = Book("Stop worrying and start living")

# TODO: print the class property
print(b1)
print(b1.title)


