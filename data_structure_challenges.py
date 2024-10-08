def add_book(book, author):
    book = input("Enter the name of the book you would like to add: ")
    author = input("Enter the author of the book: ")
    if not book or not author:  # check if both inputs are provided
        print("You must enter both the book title and the author. Please try again.")
        return
    book_lower = book.lower()
    author_lower = author.lower()
    found = [element for element in library if element[0].lower() == book_lower and element[1].lower() == author_lower]  # Check for duplicates
    if found:
        print(f"The book: {book}, with the author: {author} already exists within the library.")
    elif not found:
        library.append((book, author))  # Add book to library if it doesn't already exist
        print(f"Book: {book}, with the author: {author} has been added to the library.")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

while True:
    print("\n 1. Add new book")
    print(" 2. View library")
    print(" 3. Exit")
    choice = int(input("Please enter the number for what you would like to do: "))

    if choice == 1:
        add_book(None, None)  # pass None or an empty string as arguments
    elif choice == 2:
        print(library)
    elif choice == 3:
        print("Exiting library manager.....See you soon!")
        break
