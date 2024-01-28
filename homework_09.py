def input_error(func):
    def wrapper(contacts, *args):
        try:
            return func(contacts, *args)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide both name and phone number."
        except IndexError:
            return "Invalid input. Please provide a name."
    
    return wrapper

@input_error
def handle_hello(contacts):
    return "How can I help you?"

@input_error
def handle_add(contacts, name, phone):
    contacts[name] = phone
    return f'Contact {name} added successfully.'

@input_error
def handle_change(contacts, name, phone):
    contacts[name] = phone
    return f'Phone number for {name} updated successfully.'

@input_error
def handle_phone(contacts, name):
    return f"The phone number for {name} is {contacts[name]}."

@input_error
def handle_show_all(contacts):
    if not contacts:
        return "No contacts available."
    return "\n".join([f'{name}: {phone}' for name, phone in contacts.items()])

def main():
    contacts = {}

    print('Welcome to the Assistant Bot!')
    print('Type "exit" to end the conversation.')

    while True:
        user_input = input("Your command: ").lower()

        if user_input == "exit" or user_input == "good bye" or user_input == "close":
          print("Good bye!")
          break

        elif user_input == "hello":
            print(handle_hello(contacts))

        elif user_input.startswith('add'):
            _, name, phone = user_input.split()
            print(handle_add(contacts, name, phone))

        elif user_input.startswith('change'):
            _, name, phone = user_input.split()
            print(handle_change(contacts, name, phone))

        elif user_input.startswith("phone"):
            _, name = user_input.split()
            print(handle_phone(contacts, name))

        elif user_input == "show all":
            print(handle_show_all(contacts))

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
