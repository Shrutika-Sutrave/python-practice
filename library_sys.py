class library:

    def __init__(self, no_of_books, books):
        self.no_of_books = no_of_books
        self.books = books
        print(f"There are total {self.no_of_books} in the library")
        print(f"These are the books:  {self.books} in the library")


no_of_books = int(input("How many number of books you want to enter: "))
books_list = []
for i in range(0, no_of_books):
    book = input("Enter book(s):")
    books_list.append(book)

obj1 = library(no_of_books, books_list)
obj1.check_books()


class lib:

    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.numbooks = len(self.books)

    def show_info(self):
        print(f"the lib has {self.numbooks} books. The books are:")
        for book in self.books:
            print(book)


ob1 = lib()
ob1.add_book("book1")
ob1.add_book("book2")
ob1.add_book("book3")
ob1.show_info()
