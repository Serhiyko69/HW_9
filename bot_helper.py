# Функція для обробки помилок вводу користувача
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found!"
        except ValueError:
            return "Invalid input. Please try again."
        except IndexError:
            return "Invalid input. Please try again."
    return wrapper

contacts = {}


# Функції-обработники команд
@input_error
def add_contact(contact_info):
    name, phone = contact_info.split(' ')
    contacts[name] = phone
    return f"Contact {name} with phone number {phone} has been added."


@input_error
def change_phone(contact_info):
    name, phone = contact_info.split(' ')
    contacts[name] = phone
    return f"Phone number for contact {name} has been changed to {phone}."


@input_error
def show_phone(contact_name):
    return contacts[contact_name]


def show_all_contacts():
    if not contacts:
        return "No contacts found."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


# Функція для обробки введених команд
def handle_command(command):
    command = command.lower()

    if command == 'hello':
        return "How can I help you?"

    elif command.startswith('add'):
        contact_info = command[4:].strip()
        return add_contact(contact_info)

    elif command.startswith('change'):
        contact_info = command[7:].strip()
        return change_phone(contact_info)

    elif command.startswith('phone'):
        contact_name = command[6:].strip()
        return show_phone(contact_name)

    elif command == 'show all':
        return show_all_contacts()

    elif command in ['good bye', 'close', 'exit']:
        return "Good bye!"

    else:
        return "Invalid command. Please try again."


# запуск бота
def main():
    print("Hello! I am your assistant bot.")

    while True:
        user_input = input("Enter command: ")
        response = handle_command(user_input)
        print(response)

        if user_input.lower() in ['good bye', 'close', 'exit']:
            break


if __name__ == "__main__":
    main()
