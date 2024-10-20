from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)



class Name(Field):
    def __init__(self, value):
        if len(value) != 0:
            super().__init__(value)
        else:
            raise ValueError("Name cannot be empty")



class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number")

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Phone):
            return self.value == other.value
        else:
            return False



class Record:
    def __init__(self, contact_name) -> None:
        self.name = Name(contact_name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        if phone_number in self.phones:
            self.phones.remove(phone_number)
        else:
            print(f"Phone number {phone_number} not found.")

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone):
            self.remove_phone(old_phone)
        self.add_phone(new_phone)

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone_number == phone.value:
                return phone
        return None

    def __str__(self) -> str:
        return f"Contact name: {self.name.value}, phones: {[obj.value for obj in self.phones]}"



class AddressBook(UserDict):

    def add_record(self, record_item):
        self.data[record_item.name.value] = record_item

    def find(self, contact_name):
        return self.data.get(contact_name)

    def delete(self, contact_name):
        if contact_name in self.data:
            del self.data[contact_name]