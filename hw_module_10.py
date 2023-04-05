from collections import UserDict

dict_of_contacts = {}


class Field:
    def __init__(self, value):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not isinstance(int(value), int):
            raise ValueError("Must be a integer")
        self.value = value


class Record:
    def __init__(self, name: Name, phone=None):
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)

    def add_phone(self, phone: Phone):
        self.phones.append(phone)
        return self.phones

    def change_phone(self, new_phone: Phone):
        self.phones.clear
        self.phones.append(new_phone)
        return self.phones

    def __repr__(self) -> list:
        return self.phones


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record.phones

    def __repr__(self, record) -> str:
        return self.data[record.name.value]

    def __str__(self) -> str:
        return str(self.data)


dict = AddressBook()


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return print("Enter user name")
    return inner


def hello(*args):
    return print("How can I help You?")


def add(*args):
    list_of_param = args[0].split()
    name = Name(list_of_param[0])
    if len(list_of_param) <= 2:
        phone = Phone(list_of_param[1])
        record = Record(name, phone)
    else:
        list_of_param.pop[0]
        record = Record(name)
        for el in list_of_param:
            phone = Phone(el)
            record.add_phone(phone)
    dict.add_record(record)
    return dict


def change(*args):
    list_of_param = args[0].split()
    name = str(list_of_param[0])
    for keys in dict.keys():
        if name == keys:
            phone = Phone(list_of_param[1])
            record = Record(name)
            dict.update({keys: record.change_phone(phone)})
    return dict


@input_error
def phone(*args):

    name = str(args[0])
    for keys in dict.keys():
        if name == keys:
            return print(dict.get(keys))
    if not name:
        raise ValueError("Please write name")


def show_all(*args):
    return print(dict)


def exit(*args):
    return print("Good bye!")


def no_command(*args):
    return print("Unknown command, try again")


COMMANDS = {hello: "hello", add: "add", change: "change", phone: "phone",
            show_all: "show all", exit: ["good bye", "close", "exit"]}


def handler(text):
    for command, kword in COMMANDS.items():
        if type(kword) is str:
            if text.startswith(kword):
                return command, text.replace(kword, "").strip()
        else:
            if text in kword:
                return command, None
    return no_command, None


def main():
    while True:
        user_input = input(">>>")
        command, data = handler(user_input.lower())
        command(data)
        if command == exit:
            break


if __name__ == "__main__":
    main()
