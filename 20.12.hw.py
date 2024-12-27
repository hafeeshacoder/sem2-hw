import re
class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.member_id = self.generate_member_id()

    def generate_member_id(self):
        import uuid
        return f"LIB{uuid.uuid4().int)[:4]}"

    def verify_member_id(self, member_id):
        pattern = r"^LIB\d{4}$"
        return bool(re.match(pattern, member_id, re.IGNORECASE))

    def __str__(self):
        return f"Member ID: {self.member_id}, Name: {self.name}, Email: {self.email}"

class Library(Member):
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book_id, title, author):
        self.books[book_id] = {"title": title, "author": author, "available": True}
        print(f"Book '{title}' added to the library.")

    def register_member(self, name, email):
        member = Member(name, email)
        self.members[member.member_id] = member
        print(f"Member '{name}' registered successfully.")

    def borrow_book(self, member_id, book_id):
        if member_id in self.members and book_id in self.books:
            if self.books[book_id]["available"]:
                self.books[book_id]["available"] = False
                print(f"Book '{self.books[book_id]['title']}' borrowed by member '{self.members[member_id].name}'.")
            else:
                print(f"Book '{self.books[book_id]['title']}' is not available.")
        else:
            print("Invalid member ID or book ID.")

    def return_book(self, book_id):
        if book_id in self.books:
            self.books[book_id]["available"] = True
            print(f"Book '{self.books[book_id]['title']}' returned.")
        else:
            print("Invalid book ID.")

# Example usage
library = Library()
library.add_book("BK001", "Book Title", "Author Name")
library.register_member("John Doe", "johndoe@example.com")
library.borrow_book("LIB1234", "BK001")
library.return_book("BK001")


