import sys


def parse_input(user_input):
    parts = user_input.split()
    cmd, *args = parts
    cmd = cmd.lower()
    return cmd, args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return True
    return False

def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name)

def show_all(_args, contacts):
    if contacts:
        return "\n".join(f"{n}: {p}" for n, p in contacts.items())
    return None

def handle_exit(_args, _contacts):
    print(f"Goodbye!")
    sys.exit(0)

def handle_welcome(_args, _contacts):
    print(f"How can I help you?")

def handle_add(args, contacts):
    add_contact(args, contacts)
    print("Contact added.")

def handle_change_contact(args, contacts):
    msg = "Contact updated." if change_contact(args, contacts) else "Contact not found."
    print(msg)

def handle_show_phone(args, contacts):
    phone = show_phone(args, contacts)
    msg = phone if phone else "Contact not found."
    print(msg)

def handle_show_all_contacts(contacts):
    contacts_str = show_all(contacts)
    if contacts_str is None:
        contacts_str = "No contacts found."
    print(contacts_str)

def handle_invalid_command():
    print("Invalid command.")