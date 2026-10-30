
# parsing user input into command and list of remaining arguments
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# adds arguments to contacts dictionary
def add_contact(args, contacts):
    name, phone = args
    name = name.lower()
    if name in contacts:
        return "Contact already exists"
    contacts[name] = phone
    return "Contact added."

# changes contact's phone. if the contact's name is missing, will not create it, just notifies the user
def change_contact(args, contacts):
    name, phone = args
    name = name.lower()
    if name not in contacts:
        return f"Contact {name} is missing"
    
    old_phone = contacts[name]
    contacts[name] = phone
    return f"{name.capitalize()}'s phone number was changed from {old_phone} to {contacts[name]}"

# returns contacts phone number by name. in case name is missing, notifies the user
def show_phone(args, contacts):
    name, = args
    name = name.lower()
    if not name in contacts:
        return f"{name.capitalize()} is not in contacts"
    else:
        return f"{name.capitalize()}'s phone is {contacts[name]}"
    
# returns all contacts with respective phone numbers 
def show_all(contacts):
    if not contacts:
        return "No contacts yet"
    else:
        return "\n".join(f"{name.capitalize()} : {phone}" for name, phone in contacts.items())
    
# exceptions will be handles later with decorators
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        
        if not user_input.strip():
                    continue
        
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
            print(show_phone(args,contacts))
        
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
