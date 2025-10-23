def parse_input(user_input):
    parts = user_input.split()
    if len(parts) == 0:
        raise ValueError("User input is empty")
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

def show_all(contacts):
    if contacts:
        return "\n".join(f"{n}: {p}" for n, p in contacts.items())
    return None

# def input_error():
