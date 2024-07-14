
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "invalid input"

    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "invalid input"


    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."

    return f"Contact with name {name} not found"

def phone(args, contacts):
    if len(args) != 1:
        return "invalid input"
    name = args[0]

    if name in contacts:
        return contacts[name]

    return f"Contact with name {name} not found"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(phone(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()