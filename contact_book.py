class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        if phone in self.contacts:
            print("Contact with this phone number already exists.")
        else:
            self.contacts[phone] = {"name": name, "phone": phone, "email": email, "address": address}
            print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("\nContact List:")
            for phone, details in self.contacts.items():
                print(f"Name: {details['name']}, Phone: {details['phone']}")
        else:
            print("No contacts found.")

    def search_contact(self):
        search = input("Enter name or phone number to search: ")
        found = False
        for phone, details in self.contacts.items():
            if search.lower() in details['name'].lower() or search == phone:
                print(f"\nContact found: Name: {details['name']}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
                found = True
                break
        if not found:
            print("Contact not found.")

    def update_contact(self):
        identifier = input("Enter the phone number of the contact to update: ")
        if identifier in self.contacts:
            print(f"Current details: {self.contacts[identifier]}")
            name = input("Enter new name (leave blank to keep unchanged): ")
            phone = input("Enter new phone number (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            address = input("Enter new address (leave blank to keep unchanged): ")

            if name: self.contacts[identifier]['name'] = name
            if phone:
                self.contacts[phone] = self.contacts.pop(identifier)
                self.contacts[phone]['phone'] = phone
            if email: self.contacts[phone]['email'] = email
            if address: self.contacts[phone]['address'] = address

            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self):
        identifier = input("Enter the phone number of the contact to delete: ")
        if identifier in self.contacts:
            del self.contacts[identifier]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    def menu(self):
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contact List")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.search_contact()
            elif choice == '4':
                self.update_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                print("Exiting Contact Book.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")


contact_book = ContactBook()
contact_book.menu()
