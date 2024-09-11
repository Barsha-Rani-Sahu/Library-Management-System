from Admin import Admin
from User import User

def main():
    admin = Admin()
    user = User()
    choice = 0
    while choice != 3:
        print("\n====================== Welcome To The Library ======================")
        print("\t\t\t\t\t\t1. Admin")
        print("\t\t\t\t\t\t2. User")
        print("\t\t\t\t\t\t3. Exit")
        print("=====================================================================")

        choice = int(input("Enter your choice:"))
        if choice == 1:
            while True:
                print("\n========================= WELCOME=========================")
                print("\t\t1. Register")
                print("\t\t2. Login")
                print("\t\t3. Logout")
                print("===============================================================")

                admin_choice = int(input("Enter your choice: "))
                if admin_choice == 1:
                    admin.admin_register()
                elif admin_choice == 2:
                    if admin.admin_login():
                        admin_main(admin)
                        break
                elif admin_choice == 3:
                    print("....Logout....")
                    break
                else:
                    print("invalid choice")

        elif choice == 2:
            while True:
                print("\n========================= WELCOME=========================")
                print("\t\t1. Register")
                print("\t\t2. Login")
                print("\t\t3. Logout")
                print("===============================================================")

                user_choice = int(input("Enter your choice: "))
                if user_choice == 1:
                    user.user_register()
                elif user_choice == 2:
                    if user.user_login():
                        user_main(user)
                        break
                elif user_choice == 3:
                    print("....Logout....")
                    break
                else:
                    print("invalid choice")

def admin_main(admin):
    while True:
        print("\n========================= Admin Menu =========================")
        print("\t\t1. Add a book")
        print("\t\t2. Show available books")
        print("\t\t3. Show issued books")
        print("\t\t4. Search book")
        print("\t\t5. Update book")
        print("\t\t6. Delete book")
        print("\t\t7. Logout")
        print("===============================================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = int(input("Enter book id: "))
            book_name = input("Enter book name: ")
            author = input("Enter author name: ")
            status = input("Enter status: ")
            admin.add_book(book_id, book_name, author, status)
        elif choice == "2":
            admin.display_books()
        elif choice == "3":
            admin.display_issue_books()
        elif choice == "4":
            book_id = int(input("Enter book_id to search: "))
            admin.search_book(book_id)
        elif choice == "5":
            book_id = int(input("Enter book id which you want to update: "))
            admin.update_book_details(book_id)
        elif choice == "6":
            book_id = int(input("Enter book id which you want to delete: "))
            admin.delete_book(book_id)

        elif choice == "7":
            print("\n... Logout ...\n")
            break
        else:
            print("Invalid choice... Please enter correct choice")


# User menu
def user_main(user):
    while True:
        print("\n========================= User Menu =========================")
        print("\t\t1. Available Books")
        print("\t\t2. Issue Book")
        print("\t\t3. Return Book")
        print("\t\t4. Logout")
        print("===============================================================")

        choice = input("Enter your choice: ")
        if choice == "1":
            user.show_books()
        elif choice == "2":
            student_id = int(input("Enter your ID: "))
            book_id = input("Enter book id: ")
            user.issue_book(student_id, book_id)
        elif choice == "3":
            student_id = int(input("Enter your ID: "))
            book_id = input("Enter book id: ")
            user.return_book(student_id, book_id)
        elif choice == "4":
            print("\n... Logout ...\n")

            break
        else:
            print("Invalid choice...Please enter correct choice")


if __name__ == "__main__":
    main()
