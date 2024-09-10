class PhonebookView:
    def display_contacts(self, contacts):
        print("Contacts:")
        for name, phone in contacts:
            print(f"Name: {name}, Phone: {phone}")
        print("")

    # Format data for adding contact
    def prompt_for_contact_info(self):
        name = input("Name: ")
        phone = input("Phone: ")
        return name, phone

    # Format data for searching contact 
    def prompt_for_contact_name(self):
        return input("Name: ")

    # Fomrat data for update existing contact
    def prompt_for_updated_info(self):
        name = input("New name: ")
        phone = input("New phone: ")
        return name, phone

    # Show message to user
    def show_message(self, message):
        print(message)

    # Format data for choosing 
    def show_menu(self):
        print("1. Show Contacts")
        print("2. Add Contact")
        print("3. Update Contact")
        print("4. Remove Contact")
        print("5. Exit")
        
        return input("Choose one: ")
