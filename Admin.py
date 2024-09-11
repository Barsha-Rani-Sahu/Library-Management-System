from prettytable import PrettyTable
from duplicate_book_id import DuplicateBookIdError
from datetime import datetime

class Admin:

    def add_book(self, book_id, book_name, author, status):
        try:
            with open("books.txt", "r") as fp:
                for line in fp:
                    existing_book_id = line.strip().split(',')[0]
                    if existing_book_id == str(book_id):
                        raise DuplicateBookIdError(book_id)
            with open("books.txt", "a") as fp:
                fp.write(f"{book_id},{book_name},{author},{status}\n")
            print("Book added successfully")
        except DuplicateBookIdError as d:
            print(f"Book with ID {d} already exists")


    def display_books(self):
        try:
            with open("books.txt", "r") as fp:
                print("These are the books available in the library:")
                table = PrettyTable(["Book ID", "Book Name", "Author", "Status"])
                for line in fp:
                    if len(line.strip().split(",")) >= 4:
                        book_id, book_name, author, status = line.strip().split(",")
                        table.add_row([book_id, book_name, author, status])
                print(table)
        except FileNotFoundError:
            print("Error: File 'books.txt' not found.")

    def display_issue_books(self):
        try:
            with open("issue.txt", "r") as fp:
                print("These are the books that are issued:")
                table = PrettyTable(["Book ID", "Book Name", "Issue Date"])
                for line in fp:
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        book_id, book_name, issue_date = parts
                        table.add_row([book_id, book_name, issue_date])
                    else:
                        print(f"Invalid data: {line.strip()}")
                print(table)
        except FileNotFoundError:
            print("Error: File 'issue.txt' not found.")

    def search_book(self, book_id):
        try:
            with open("books.txt", "r") as fp:
                for book in fp:
                    book_info = book.strip().split(',')
                    if book_info[0] == str(book_id):
                        print("Book found:", book)
                        return
                print("Book not found")
        except FileNotFoundError:
            print("Error: File 'books.txt' not found.")

    def update_book_details(self, book_id):
        try:
            all_books = []
            found = False
            with open("books.txt", "r") as fp:
                for book in fp:
                    if str(book_id) in book:
                        book = book.strip().split(",")
                        edit = input("Do you want to edit book id (yes/no): ")
                        if edit.lower() == "yes":
                            book[0] = input("Enter new book id: ")
                        edit = input("Do you want to edit book name (yes/no): ")
                        if edit.lower() == "yes":
                            book[1] = input("Enter new book name: ")
                        edit = input("Do you want to edit author name (yes/no): ")
                        if edit.lower() == "yes":
                            book[2] = input("Enter new author name: ")
                        edit = input("Do you want to edit Status (yes/no): ")
                        if edit.lower() == "yes":
                            book[3] = input("Enter new Status: ")
                        book = ",".join(book) + "\n"
                        found = True
                    all_books.append(book)

            if found:
                with open("books.txt", "w") as fp:
                    for book in all_books:
                        fp.write(book)
                print("Book updated successfully!")
            else:
                print("Book you want to edit is not found")
        except FileNotFoundError:
            print("Error: File 'books.txt' not found.")

    def delete_book(self, book_id):
        try:
            all_books = []
            found = False
            with open("books.txt", "r") as fp:
                for book in fp:
                    if str(book_id) not in book:
                        all_books.append(book)
                    else:
                        found = True

            if found:
                with open("books.txt", "w") as fp:
                    for book in all_books:
                        fp.write(book)
                print("Book deleted successfully.")
            else:
                print("Book you want to delete is not present.")
        except FileNotFoundError:
            print("Error: File 'books.txt' not found.")

    def admin_register(self):
        try:
            date = datetime.now()
            register_date = "{}-{}-{}".format(date.day, date.month, date.year)
            with open("admin_info.txt", "r") as file:
                lines = file.readlines()
                if len(lines) > 3:
                    print("Maximum registration limit reached. No more registrations allowed.")
                    return False

            name = input("Enter your name: ")
            admin_id = input("Enter your ID: ")
            password = input("Set password: ")
            confirm_password = input("Confirm your password: ")

            if password == confirm_password:
                with open("admin_info.txt", "r") as fp:
                    for line in fp:
                        if admin_id in line:
                            raise DuplicateBookIdError(admin_id)
                with open("admin_info.txt", "a") as file:
                    file.write(f"{admin_id},{password},{name},{register_date}\n")
                print("Registration successful.\n")
                return True
            else:
                print("Passwords do not match. Please try again.")
                return False
        except DuplicateBookIdError as d:
            print(d,"already exists. Please choose a different ID.")


    def admin_login(self):
        admin_id = input("Enter your admin ID: ")
        password = input("Enter your password: ")
        with open("admin_info.txt", "r") as file:
            for line in file:
                line = line.strip().split(',')
                if admin_id == line[0] and password == line[1]:
                    print(f"Login successful. Welcome {line[2]}")
                    return True
        print("Invalid admin ID or password.")
        return False








if __name__ == "__main__":
    a = Admin()
