contacts = {}
def add_contact():
    name = input("enter name: ").strip()
    if name in contacts:
        print(f"'{name}' already exists!")
    else:
        phone = input("enter phone number: ").strip()
        contacts[name] = phone
        print(f"Contact '{name}' added successfully!")


def search_contact():
    name = input("enter name to search: ").strip()
    if name in contacts:
        print(f"found -> {name} : {contacts[name]}")
    else:
        print(f"'{name}' not found!")

def update_contact():
    name = input("enter name to update: ").strip()
    if name in contacts:
        new_phone = input(f"enter new number for {name}: ").strip()
        contacts[name] = new_phone
        print(f"contact '{name}' updated!")
    else:
        print(f"'{name}' not found!")

def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted!")
    else:
        print(f"'{name}' not found!")


def view_contacts():
    if not contacts:
        print("contact book is empty!")
    else:
        print("\n all contacts")
        for name, phone in contacts.items():
            print(f"{name} : {phone}")

def show_menu():
    print("\n contact book menu ")
    print("1. add contact")
    print("2. search contact")
    print("3. update Contact")
    print("4. delete contact")
    print("5. view all contacts")
    print("6. Exit")


while True:
    show_menu()
    choice = input("enter choice (1-6): ")

    if choice == '1':   
        add_contact()
    elif choice == '2': 
        search_contact()
    elif choice == '3': 
        update_contact()
    elif choice == '4': 
        delete_contact()
    elif choice == '5':
        view_contacts()
    elif choice == '6':
        print("exiting contact book. Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
