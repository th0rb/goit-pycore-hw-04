def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif  command in ["hi", "hello"]:
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":  
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))
            
        elif command == "all":
            print(show_all(contacts))

        elif command == "help":
            print("add|change|phone|all")   

        else:
            print("Invalid command.")


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return f"The name {name} already exists in contacts"
        else:
            contacts[name] = phone
            return "Contact added."
    except ValueError as ve:
        return str(ve)   

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return f"The name {name} is unknown"
    except ValueError as ve:
        return str(ve)       

def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else: 
            return f"The name {name} is not on your contacts."
    except ValueError as ve:
        return str(ve)       
    
def show_all(contacts):
    res = ""  

    if len(contacts) == 0:
        return "Your contact list is empty."
    else:
        for name, phone in contacts.items():
            res += f"{name}: {phone}\n"
        return res

if __name__ == "__main__":
    main()