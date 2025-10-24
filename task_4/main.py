import sys

from handlers import parse_input, handle_exit, handle_add, handle_welcome, handle_show_phone, handle_change_contact, \
    handle_show_all_contacts

COMMAND_TO_HANDLER = {
    "close": handle_exit,
    "exit": handle_exit,
    "hello": handle_welcome,
    "add": handle_add,
    "change": handle_change_contact,
    "phone": handle_show_phone,
    "all": handle_show_all_contacts,
}


def read_input():
    user_input = None
    try:
        while user_input is None:
            user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
    except EOFError:
        command, args = "exit", []
    return command, args


def process_command(command, args, contacts):
    try:
        handler = COMMAND_TO_HANDLER[command]
    except KeyError:
        print("Invalid command.")
    else:
        return handler(args, contacts)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        try:
            command, args = read_input()
            process_command(command, args, contacts)
        except StopIteration:
            break
    print(f"Goodbye!")


if __name__ == '__main__':
    main()
