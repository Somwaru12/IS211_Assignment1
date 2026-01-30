class Book:
    author: str = ""
    title: str = ""

    def __init__(self, author: str, title: str) -> None:
        self.author = author
        self.title = title

    def display(self) -> None:
        print(f"{self.title}, written by {self.author}")


if __name__ == "__main__":
    b1 = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    b2 = Book("Walter Scott", "Ivanhoe: A Romance")

    b1.display()
    b2.display()
