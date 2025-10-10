contacts = {}

while(True):
    print("1. Add contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contact")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice=='1':
        name = input("Enter name:")
        if name in contacts:
            print("Contact already exists")
        else:
            age = input("Enter age:")
            email = input("Enter email:")
            mobile = input("Enter mobile:")
            contacts[name] = {'age':{age},'email':email,'mobile':{mobile}}
            print("Contact added successfully")

    elif choice=='2':
        name = input("Enter name to view:")
        if name in contacts:
            print("Name:",name)
            print("Age:",contacts[name]['age'])
            print("Email:",contacts[name]['email'])
            print("Mobile:",contacts[name]['mobile'])
        else:
            print("Contact not found")

    elif choice=='3':
        name = input("Enter name to update:")
        if name in contacts:
            age = input("Enter age:")
            email = input("Enter email:")
            mobile = input("Enter mobile:")
            contacts[name] = {'age':{age},'email':email,'mobile':{mobile}}
            print("Contact updated successfully")
        else:
            print("Contact not found")

    elif choice=='4':
        name = input("Enter name to delete:")
        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully")
        else:
            print("Contact not found")

    elif choice=='5':
        name = input("Enter name to search:")
        if name in contacts:
            print("Contact found")
        else:
            print("Contact not found")

    elif choice=='6':
        print("Number of contacts:",len(contacts))

    elif choice=='7':
        break

    else:
        print("Invalid choice")