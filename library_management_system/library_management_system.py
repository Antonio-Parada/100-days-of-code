class LibraryManagementSystem:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.borrowed_books = {}
        self.book_id_counter = 0
        self.member_id_counter = 0

    def add_book(self, title, author, quantity):
        self.book_id_counter += 1
        book_id = self.book_id_counter
        self.books[book_id] = {'title': title, 'author': author, 'quantity': quantity, 'available': quantity}
        print(f"Book '{title}' by {author} added with ID {book_id}. Quantity: {quantity}")
        return book_id

    def register_member(self, name):
        self.member_id_counter += 1
        member_id = self.member_id_counter
        self.members[member_id] = {'name': name, 'borrowed_books': []}
        print(f"Member {name} registered with ID {member_id}.")
        return member_id

    def borrow_book(self, book_id, member_id):
        if book_id not in self.books:
            print(f"Book with ID {book_id} not found.")
            return False
        if member_id not in self.members:
            print(f"Member with ID {member_id} not found.")
            return False
        if self.books[book_id]['available'] <= 0:
            print(f"Book '{self.books[book_id]['title']}' is currently not available.")
            return False

        self.books[book_id]['available'] -= 1
        self.members[member_id]['borrowed_books'].append(book_id)
        self.borrowed_books[book_id] = self.borrowed_books.get(book_id, []) + [member_id]
        print(f"Book '{self.books[book_id]['title']}' borrowed by {self.members[member_id]['name']}.")
        return True

    def return_book(self, book_id, member_id):
        if book_id not in self.books:
            print(f"Book with ID {book_id} not found.")
            return False
        if member_id not in self.members:
            print(f"Member with ID {member_id} not found.")
            return False
        if book_id not in self.members[member_id]['borrowed_books']:
            print(f"Member {self.members[member_id]['name']} did not borrow this book.")
            return False

        self.books[book_id]['available'] += 1
        self.members[member_id]['borrowed_books'].remove(book_id)
        self.borrowed_books[book_id].remove(member_id)
        print(f"Book '{self.books[book_id]['title']}' returned by {self.members[member_id]['name']}.")
        return True

    def list_books(self):
        print("\n--- All Books ---")
        if not self.books:
            print("No books in the library.")
            return
        for book_id, book_info in self.books.items():
            print(f"ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}, Available: {book_info['available']}/{book_info['quantity']}")
        print("------------------")

    def list_members(self):
        print("\n--- All Members ---")
        if not self.members:
            print("No members registered.")
            return
        for member_id, member_info in self.members.items():
            borrowed_titles = [self.books[b_id]['title'] for b_id in member_info['borrowed_books'] if b_id in self.books]
            print(f"ID: {member_id}, Name: {member_info['name']}, Borrowed Books: {', '.join(borrowed_titles) if borrowed_titles else 'None'}")
        print("------------------")

if __name__ == "__main__":
    lms = LibraryManagementSystem()
    print("--- Simple CLI Library Management System ---")
    print("Commands: add_book <title> <author> <quantity>, register_member <name>, borrow <book_id> <member_id>, return <book_id> <member_id>, list_books, list_members, exit")

    while True:
        command_input = input("> ").split(maxsplit=3)
        cmd = command_input[0].lower()

        if cmd == "add_book":
            if len(command_input) == 4:
                try:
                    lms.add_book(command_input[1], command_input[2], int(command_input[3]))
                except ValueError:
                    print("Quantity must be a number.")
            else:
                print("Usage: add_book <title> <author> <quantity>")
        elif cmd == "register_member":
            if len(command_input) == 2:
                lms.register_member(command_input[1])
            else:
                print("Usage: register_member <name>")
        elif cmd == "borrow":
            if len(command_input) == 3:
                try:
                    lms.borrow_book(int(command_input[1]), int(command_input[2]))
                except ValueError:
                    print("Book ID and Member ID must be numbers.")
            else:
                print("Usage: borrow <book_id> <member_id>")
        elif cmd == "return":
            if len(command_input) == 3:
                try:
                    lms.return_book(int(command_input[1]), int(command_input[2]))
                except ValueError:
                    print("Book ID and Member ID must be numbers.")
            else:
                print("Usage: return <book_id> <member_id>")
        elif cmd == "list_books":
            lms.list_books()
        elif cmd == "list_members":
            lms.list_members()
        elif cmd == "exit":
            print("Exiting Library Management System.")
            break
        else:
            print("Unknown command.")
