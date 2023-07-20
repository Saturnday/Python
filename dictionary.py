
books = [
    {"name": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "pages": 223},
    {"name": "Moby Dick", "author": "Herman Melville", "pages": 378},
    {"name": "To Kill a Mockingbird", "author": "Harper Lee", "pages": 281},
    {"name": "War and Peace", "author": "Leo Tolstoy", "pages": 1225},
    {"name": "The Great Gatsby", "author": "F. Scott Fitzgerald", "pages": 180}
]


for book in books:
    n=book["pages"]
    if n>300:
        print(book["name"], book["author"], sep=", ")