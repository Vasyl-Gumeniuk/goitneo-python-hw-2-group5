def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "The contact does not exist"
        except IndexError:
            return "Enter contact's name"

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return (f"Contact with name '{name}' added.")


@input_error
def change_contact(args, contacts):
    name, phone = args
    old_phone = contacts[name]
    contacts[name] = phone   
    return (f"Contact with name '{name}' was updated and has new number {phone}. The prior phone number was: {old_phone}")

    
@input_error
def show_phone(args, contacts): 
    name = args[0]
    phone = contacts[name]
    return (f"Contact with name '{name}' has phone number '{phone}'.")


@input_error
def show_all(contacts):
    if not contacts:
        raise ValueError
       
    message_all_contacts = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())   
    return message_all_contacts
    

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
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
    


if __name__ == "__main__":
    main()