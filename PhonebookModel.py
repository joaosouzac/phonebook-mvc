from ContactModel import Contact


class PhonebookModel: # Subject
    def __init__(self):
        self.contacts = []
        self.observers = [] # List of subscribed observers

    # Add contact to phonebook
    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        self.notify_observers()

    # Remove contact from phonebook by name
    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]
        self.notify_observers()

    # Update contact's info by name
    def update_contact(self, name, new_name, new_phone):
        for c in self.contacts:
            if c.name == name:
                c.name = new_name
                c.phone = new_phone
        self.notify_observers()

    # View all contacts in phonebook
    def get_contacts(self):
        return [(c.name, c.phone) for c in self.contacts]

    # Add an observer
    def add_observer(self, observer):
        self.observers.append(observer)

    # Remove an observer
    def remove_observer(self, observer):
        self.observers.remove(observer)

    # Notify a change to the observers, forcing them to update their data
    def notify_observers(self):
        for observer in self.observers:
            observer.update_view()
          
