# Python Object-Oriented Programming by Joe Marini
# Using instance methods and attributes

class Book:
    # the "init" function is called when the instance is created and ready to be initialized

    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self._discount * self.price)
        else:
            return self.price

    def set_discount(self, amount):
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and peace", " Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", " JD Salinger", 234, 29.95)

# TODO: print the price of book 1
print(b2.get_price())

# TODO: try setting the discount
print(b2.get_price())
b2.set_discount(0.25)
print(b2.get_price())

# TODO: properties with double underscores are hidden by the interpreter.
#  python prefixing attribute name that start  with double score with class name as
#  way for hiding them and prevent subclass from access them.
# print(b2.__secret)   # this statement will generate an error
print(b2._Book__secret)
