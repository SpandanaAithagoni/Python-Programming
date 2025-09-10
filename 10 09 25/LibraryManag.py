def add(key, value, dict1):
    dict1[key] = value  

def remove(key, dict1):
    if key in dict1:
        del dict1[key]
    else:
        print("Book ID not found.")

def search(key, dict1):
    if key in dict1:
        return dict1[key] 
    else:
        return "Book ID not found."

def update(key, nvalue, dict1):
    if key in dict1:
        dict1[key] = nvalue
    else:
        print("Book ID not found.")

def display(dict1):
    return dict1.items()

def count(dict1):
    return len(dict1)

def check(value, dict1):
    for k, v in dict1.items():
        if v == value:
            return k, v 


library = {}

while True:
    print("\nMenu:")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book by ID")
    print("4. Update Book Title")
    print("5. Display All Books")
    print("6. Count Books")
    print("7. Check if Title Exists")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        bid = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        add(bid, title, library)
        print("Book added.")

    elif choice == '2':
        bid = input("Enter Book ID to remove: ")
        remove(bid, library)

    elif choice == '3':
        bid = input("Enter Book ID to search: ")
        print("Book Title:", search(bid, library))

    elif choice == '4':
        bid = input("Enter Book ID to update: ")
        new_title = input("Enter new Book Title: ")
        update(bid, new_title, library)

    elif choice == '5':
        print("\nAll Books:")
        for k, v in display(library):
            print(f"ID: {k}, Title: {v}")

    elif choice == '6':
        print("Total books:", count(library))

    elif choice == '7':
        title = input("Enter Book Title to check: ")
        result = check(title, library)
        if result:
            print(f"Title found with Book ID: {result[0]}")
        else:
            print("Title not found.")

    elif choice == '8':
        print("Exiting. Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
