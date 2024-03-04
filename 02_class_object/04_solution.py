class Book():
    def __init__(self, bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price

    def showBookDetails(self):
        print("Book id:", self.bookid)
        print("Title:", self.title)
        print("Price:", self.price)

b1 = Book(1, "Morning Miracle", 299)
b1.showBookDetails()

b2 = Book(2, "5AM Club", 599)
b2.showBookDetails()