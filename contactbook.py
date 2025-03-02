contacts = {}

def display_contact():
    print("name\t\tcontact number")
    for key in contacts:
        print("{}\t\t{}".format(key, contacts.get(key)))

while True:
    print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        contacts[name] = phone
    
    elif choice == 2:    
        search_name = input("Enter the contact name: ")
        if search_name in contacts:
            print(search_name, "contact number is", contacts[search_name])
        else:
            print("Name is not found in contact book")
    
    elif choice == 3:
        if not contacts:
            print("empty contact book")
        else:
            display_contact()
    
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited: ")
        if edit_contact in contacts:
            phone = input("enter mobile number: ")  
            contacts[edit_contact] = phone
            print("contact updated")
        else:
            print("Name is not found in the contact book")
    
    elif choice == 5:      
        del_contact = input("Enter the contact to be deleted: ")
        if del_contact in contacts:
            confirm = input("Do you want to delete this account yes/no? ")
            if confirm.lower() == "yes":
                contacts.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in the contact book")
    
    else:
        break
