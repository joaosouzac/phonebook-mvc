from PhonebookModel import PhonebookModel
from PhonebookView import PhonebookView
from PhonebookController import PhonebookController


# Ensure code runs only if not imported
if __name__ == "__main__":
    model = PhonebookModel()
    view = PhonebookView()
    controller = PhonebookController(model, view)

    controller.run()
