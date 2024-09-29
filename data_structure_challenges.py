def add_book(library_data):
    book,author = library_data
    book = input("Enter the name of the book you would like to add: ")
    author = input("Enter the author of the book: ")
    if len(book or author) == 0:
        print("You must enter both the book title and the author. Please try again.")
        found = [element for element in library_data if element[0].lower() and element[1].lower() == book.lower() and author.lower()]
        if found:
            print(f"The book: {book},with the author: {author} already exists within the library.")
        elif not found: 
            library_data.append((book, author))
            print(f"Book: {book},with the author: {author} has been added to the library.")  

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

while True:
    print("\n 1. Add new book")
    print(" 2. View library")
    print(" 3. Exit")
    choice = int(input("Please enter the number for what you would like to do: "))

    if choice == 1:
        add_book(library)
    elif choice == 2:
        print(library)
    elif choice == 3:
        print("Exiting library manager.....See you soon!")
        break