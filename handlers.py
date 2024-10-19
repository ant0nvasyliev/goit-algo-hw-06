from decorators import input_error


@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added!"


@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = new_phone
    return f"Contact {name} updated!"


@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts):
    if contacts == {}:
        return "There are no contacts yet!"

    return contacts