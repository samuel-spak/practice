print("hello world")

print("goodbye world")

class Book():
    def __init__(self, pages, author):
        self.pages = pages
        self.author = author

harryPotter = Book(400, "J.K. Rowling")

print(harryPotter.pages)
