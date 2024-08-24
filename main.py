# Give the class a name
class PersonalAssistant:

  
  # Add an __init__ function here
  def __init__(self):
    self.contacts = {'Ann': 'Marketing Coordinator', 'Chelsea': 'Software Developer', 'Nichole': 'Sales Representative', 'Max': 'Technical Writer'}
    self.todos = []

  # Complete the get_contact function code
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "There's no contact by that name"


# Code to test output of the class
assistant = PersonalAssistant()
# Change name to one from your contacts
print(assistant.get_contact("Chelsea"))