class Book:
    def __init__(self, title, author, isbn, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        return 2025 - self.publication_year

    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"

# Example usage
book1 = Book("Python Basics", "Alice", "1234567890", 2020)
book2 = Book("Advanced Python", "Bob", "0987654321", 2018)

for b in [book1, book2]:
    print(b.title, b.author, b.get_age(), b.get_summary())
