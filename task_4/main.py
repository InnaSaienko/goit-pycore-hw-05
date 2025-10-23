from handlers import parse_input, add_contact, change_contact, show_phone, show_all


def read_input():
    try:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
    except EOFError:
        command, args = "exit", []
    except ValueError:
        return None
    return command, args


def process_command(command, args, contacts):
    print(f"command: {command}")
    match command:
        case "close" | "exit":
            print(f"Goodbye!")
            return False
        case "hello":
            print(f"How can I help you?")
        case "add":
            if len(args) != 2:
                print("Invalid command.")
                return True
            add_contact(args, contacts)
            print("Contact added.")
        case "change":
            if len(args) != 2:
                print("Invalid command.")
                return True
            msg = "Contact updated." if change_contact(args, contacts) else "Contact not found."
            print(msg)
        case "phone":
            if len(args) != 1:
                print("Invalid command.")
                return True
            phone = show_phone(args, contacts)
            msg = phone if phone else "Contact not found."
            print(msg)
        case "all":
            contacts_str = show_all(contacts)
            if contacts_str is None:
                contacts_str = "No contacts found."
            print(contacts_str)
        case _:
            print("Invalid command.")
    return True


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        command, args = read_input()
        if command is None:
            continue
        if process_command(command, args, contacts) is False:
            break

    return


if __name__ == '__main__':
    main()
