from handlers import parse_input, add_contact, change_contact, show_phone, show_all

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)
        except EOFError:
            command, args = "exit", []
        except ValueError:
            continue

        print(f"command: {command}")
        match command:
            case "close" | "exit":
                print(f"Goodbye!")
                break
            case "hello":
                print(f"How can I help you?")
            case "add":
                if len(args) != 2:
                    print("Invalid command.")
                    continue
                add_contact(args, contacts)
                print("Contact added.")
            case "change":
                if len(args) != 2:
                    print("Invalid command.")
                    continue
                msg = "Contact updated." if change_contact(args, contacts) else "Contact not found."
                print(msg)
            case "phone":
                if len(args) != 1:
                    print("Invalid command.")
                    continue
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
    return


if __name__ == '__main__':
    main()
