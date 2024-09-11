from datetime import datetime
from prettytable import PrettyTable
from duplicate_book_id import DuplicateBookIdError
from negative_date import NegativeDateError
class User:

    def show_books(self):
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

    def issue_book(self, student_id, book_id):
        try:
            current_date = datetime.now()
            issue_date = "{}-{}-{}".format(current_date.day, current_date.month, current_date.year)

            with open("books.txt", "r+") as fp:
                books = fp.readlines()
                for i, book in enumerate(books):
                    book_data = book.strip().split(",")
                    if book_data[0] == book_id and book_data[-1] == '1':
                        book_data[-1] = '0'
                        books[i] = ','.join(book_data) + '\n'

                        fp.seek(0)
                        fp.writelines(books)

                        with open("issue.txt", "a") as issue_fp:
                            issue_fp.write(f"{student_id},{book_id},{issue_date}\n")

                        print("Book issued successfully!")
                        return

                print("Book not available or already issued.")
        except FileNotFoundError:
            print("Error: File 'books.txt' or 'issue.txt' not found.")

    def return_book(self, student_id, book_id):
        try:
            return_date_str = input("Enter the return date (DD-MM-YYYY): ")
            return_date = datetime.strptime(return_date_str, "%d-%m-%Y")
            try:
                if return_date < datetime.now():
                    raise NegativeDateError(return_date)
            except NegativeDateError as n:
                print(f"Return date {n} cannot be in the past.")

            with open("issue.txt", "r") as fp:
                issued_books = fp.readlines()

            found = False
            penalty = 0
            with open("issue.txt", "w") as fp:
                for issued_book in issued_books:
                    user, issued_book_id, issue_date_str = issued_book.strip().split(",")
                    if user == str(student_id) and issued_book_id == book_id:
                        found = True
                        issue_date = datetime.strptime(issue_date_str, "%d-%m-%Y")
                        days_difference = (return_date - issue_date).days
                        if days_difference > 7:
                            penalty = 30 * (days_difference - 7)
                        else:
                            penalty = 0
                        continue

                    fp.write(issued_book)

            if not found:
                print("Book not found")
                return
            with open("books.txt", "r+") as fp:
                books = fp.readlines()
                for i, book in enumerate(books):
                    book_data = book.strip().split(",")
                    if book_data[0] == book_id and book_data[-1] == '0':
                        book_data[-1] = '1'
                        books[i] = ','.join(book_data) + '\n'

                        fp.seek(0)
                        fp.writelines(books)

                        break

            if penalty > 0:
                print(f"Book returned successfully with a penalty of {penalty} rupees.")
                print(days_difference)
            else:
                print("Book returned successfully!")
        except FileNotFoundError:
            print("Error: File 'issue.txt' or 'books.txt' not found.")



    def user_register(self):
        try:
            date = datetime.now()
            register_date = "{}-{}-{}".format(date.day, date.month, date.year)
            with open("user_info.txt", "r") as fp:
                fp.readlines()
            name = input("Enter your name: ")
            student_id = input("Enter student ID: ")
            password = input("Set password: ")
            confirm_password = input("Confirm your password: ")

            if password == confirm_password:
                with open("user_info.txt", "r") as fp:
                    for line in fp:
                        if student_id in line:
                            raise DuplicateBookIdError(student_id)
                with open("user_info.txt", "a") as fp:
                    fp.write(f"{student_id},{password},{name},{register_date}\n")
                print("Registration successful.\n")
                return True
            else:
                print("Password do not match. Please try again.")
                return False
        except DuplicateBookIdError as d:
            print(d,"already exists. Please choose a different ID.")


    def user_login(self):
        student_id = input("Enter student ID: ")
        password = input("Enter your password: ")
        with open("user_info.txt", "r") as file:
            for line in file:
                line = line.strip().split(',')
                if student_id == line[0] and password == line[1]:
                    print(f"Login successful. Welcome {line[2]}")
                    return True
        print("Invalid student ID or password.")
        return False



if __name__ == "__main__":
    u = User()
