from collections import UserDict



class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)



class Name(Field):
    pass



class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:    
            raise ValueError("The phone number must consist of 10 digits")
        


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        self.phones.append(Phone(phone))


    def remove_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                self.phones.remove(i)
                print(f'The number "{i}" was succesfuly removed!')


    def edit_phone(self, old_phone, new_phone):
        for i in self.phones:
            if i.value == old_phone:
                i.value = new_phone
                print(f'The number "{old_phone}" was succesfuly updated to "{new_phone}"!')


    def find_phone(self, phone):
        for i in self.phones:
            if i.value == phone:
                print(f'Success! The number "{phone}" in your contacts!')
                return i
        return print(f'The number "{phone}" does not exist!')
       

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"




class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


    def find(self, name):
        return self.data.get(name)


    def delete(self, name):
        if self.data.get(name):
            self.data.pop(name)
            print(f'The record with name: "{name}" was succesfuly deleted!')
        else:
            print(f'The record with name: "{name}" not found!')
