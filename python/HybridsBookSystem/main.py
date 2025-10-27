from hybrids_book import *  

def main():
    books = ["The Hobbit", "The Mystery in Semicolon", "The Brave Hybrid"]  

    while True:
        print("""
Welcome to Hybrids Book Suggestion System!
1. Get Suggestions
2. Add Book
3. Remove Book
4. Update Book
5. Show All Books
6. Exit
""")

        choice = input("Enter operation: ")

        if choice == "1":
            while True:
                print(suggest_book(books))
                again = input("Would you like another suggestion? (yes/no): ").lower()
                if again != "yes":
                    break

        elif choice == "2":
            title = input("Enter the book title: ")
            print(add_book(books, title))

        elif ch=[ce == "3":
            title = input("Enter the book title to remove: ")
            print(remove_book(books, title))

        elif choice == "4":
            old_title = input("Enter the old title: ")
            new_title = input("Enter the new title: ")
            print(update_book(books, old_title, new_title))

        elif choice == "5":
            print(show_books(books))

        elif choice == "6":
            print("Thank you for using Hybrids Book System! ")
            break

        else:
            print("Invalid choice, please try again.")


