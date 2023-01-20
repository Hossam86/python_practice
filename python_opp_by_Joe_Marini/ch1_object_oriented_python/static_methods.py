# Python object Oriented Programming by Joe Marini
# using class-level and static methods

class Book:
    # TODO: Properties defined at class level are shared by all instance
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", " EBOOK")

    # TODO double underscore properties are hidden from other classes
    __booklist = None

    # TODO create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance

    def set_title(self, new_title):
        self.title = new_title

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not avalid book type")
        else:
            self.booktype = booktype


# TODO access the class attribute
print("Book types : ", Book.getbooktypes())

# TODO: create some book instances
b1 = Book("title 1", "HARDCOVER")
b2 = Book("title 2", "PAPERBACK")

# TODO: use the static method to access a singleton object

thebooks = Book.getbooklist()
thebooks.append(b1);
thebooks.append(b2)
print(thebooks)