def add(x, lst):
    lst += [x]

def remove(x, lst):
    list2 = []
    for i in lst:
        if i != x:
            list2 += [i]
    return list2

def search(x, lst):
    if x in lst:
        print("Found")
    else:
        print("Not found")

def display(lst):
    print("Current List:", lst)
    
def length(lst):
    print(len(lst))
    
def sort(lst):
    lst.sort()
    print(lst)
    
def menu():
    lst = []
    while True:
        print("1. Add Element")
        print("2. Remove Element")
        print("3. Search Element")
        print("4. Display List")
        print("5. No.of items")
        print("6. Sort the items")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            x = int(input("Enter element to add: "))
            add(x, lst)
        elif choice == '2':
            x = int(input("Enter element to remove: "))
            lst = remove(x, lst)
        elif choice == '3':
            x = int(input("Enter element to search: "))
            search(x, lst)
        elif choice == '4':
            display(lst)
        elif choice == '5' :
            length(lst)
        elif choice == '6':
            sort(lst)
        elif choice == '7':
            break
        else:
            print("Invalid choice")

menu()