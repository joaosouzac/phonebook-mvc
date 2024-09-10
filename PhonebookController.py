class PhonebookController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.model.add_observer(self) # Add Controller as the observer

    # Forces the view to update (For Debug)
    def update_view(self):
        contacts = self.model.get_contacts()
        self.view.display_contacts(contacts)

    # Create a new contact
    def add_contact(self):
        name, phone = self.view.prompt_for_contact_info()
        self.model.add_contact(name, phone)
    
    # Remove a contact from the phonebook
    def remove_contact(self):
        name = self.view.prompt_for_contact_name()
        self.model.remove_contact(name)

    # Update a contact's info
    def update_contact(self):
        name = self.view.prompt_for_contact_name()
        new_name, new_phone = self.view.prompt_for_updated_info()
        self.model.update_contact(name, new_name, new_phone)

    # Start the controller
    def run(self):
        while True:
            choice = self.view.show_menu()

            if choice == "1":
                self.update_view()
            elif choice == "2":
                self.add_contact()
            elif choice == "3":
                self.update_contact()
            elif choice == "4":
                self.remove_contact()
            elif choice == "5":
                break
            else:
                self.view.show_message("Invalid input! Try again.")
              
