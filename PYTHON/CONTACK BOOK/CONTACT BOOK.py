contact_list=[]

def display_contact(contact):
    print(f"Name: {contact['name']}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}\n")
    
while True:
    print("\nContact Book Application")
    print("1. View All Contacts")
    print("2. Add a Contact")
    print("3. Search a Contact")
    print("4. Update a Contact")
    print("5. Delete a Contact")
    print("6. Exit")

    choice=input("Choose an option (1/2/3/4/5/6): ")

    if choice=='1':
        if contact_list:
            print("\nContact List:")
            for i, contact in enumerate(contact_list, 1):
                print(f"{i}. {contact['name']} - {contact['phone']}")
        else:
            print("\nYour contact list is empty")
    
    elif choice=='2':  
        name=input("\nEnter Name: ")
        phone=input("Enter Phone Number: ")
        email=input("Enter Email: ")
        address=input("Enter Address: ")
        contact_list.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        print(f"Contact for '{name}' added successfully")

    elif choice=='3': 
        search_query=input("\nEnter the name or phone number to search: ").lower()
        found=False
        for contact in contact_list:
            if search_query in contact['name'].lower() or search_query in contact['phone']:
                print("\nContact found:")
                display_contact(contact)
                found=True
                break
        if not found:
            print("No matching contact found")
    
    elif choice=='4':
        search_query=input("\nEnter the name or phone number of the contact to update: ").lower()
        found=False
        for contact in contact_list:
            if search_query in contact['name'].lower() or search_query in contact['phone']:
                print("\nUpdating Contact:")
                display_contact(contact)
                contact['name']=input("Enter new name (leave blank to keep current): ") or contact['name']
                contact['phone']=input("Enter new phone number (leave blank to keep current): ") or contact['phone']
                contact['email']=input("Enter new email (leave blank to keep current): ") or contact['email']
                contact['address']=input("Enter new address (leave blank to keep current): ") or contact['address']
                print("Contact updated successfully")
                found=True
                break
        if not found:
            print("No matching contact found")

    elif choice=='5': 
        search_query = input("\n Enter the name or phone number of the contact to delete: ").lower()
        found = False
        for contact in contact_list:
            if search_query in contact['name'].lower() or search_query in contact['phone']:
                print("\nDeleting Contact:")
                display_contact(contact)
                confirm=input("Are you sure you want to delete this contact? (yes/no): ").lower()
                if confirm=='yes':
                    contact_list.remove(contact)
                    print("Contact deleted successfully.")
                found=True
                break
        if not found:
            print("No matching contact found.")
    
    elif choice=='6':
        print("THANK YOU")
        break

    else:
        print("Invalid option Please choose again")
