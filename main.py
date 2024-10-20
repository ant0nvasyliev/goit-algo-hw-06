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


class Record:
    def __init__(self, contact_name) -> None:
        self.name = Name(contact_name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return
        print(f"Phone number {phone_number} not found.")

    def edit_phone(self, old_phone, new_phone):
        if self.find_phone(old_phone):
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError(f"Phone number {old_phone} not found")


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

    def __str__(self) -> str:
        if not self.data:
            return "Phone book is empty."
        return "\n".join(f"Contact name: {record.name.value} - contact number(s) {', '.join(phone.value for phone in record.phones)}" for record in self.data.values())

    # Створення нової адресної книги
book = AddressBook()

# Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")
# book.add_record(john_record)

anton_record = Record('Anton')
anton_record.add_phone('1111111111')
book.add_record(anton_record)
print(book)
anton_record.edit_phone('11111111111', '2222222222')
print(book)

# Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# Виведення всіх записів у книзі



# Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
# book.delete("John")
# print(book)