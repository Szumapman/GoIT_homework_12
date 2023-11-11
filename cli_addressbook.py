import sys
from typing import Callable
from utility.addressbook import AddresBook
from utility.record import Record
from utility.name import Name
from utility.phone import Phone
from utility.email import Email
from utility.birthday import Birthday, FutureDateException

# hendler for main menu
def get_main_handler(command):
    return MAIN_COMMANDS[command]

# hendler for edit menu
def get_edit_handler(command):
    return EDIT_COMMANDS[command]

# exit / close program
def cli_addresbook_exit(*args):
    sys.exit("Good bye!")

def input_error(func: Callable):
    def wrapper(*args):
        while True:
            try:
                return func(*args)
            except ValueError:
                if func.__name__ == "add_name":
                    print("The name field cannot be empty, try again.")
                if func.__name__ == "add_phone":
                    print("Invalid phone number, try again.")
                if func.__name__ == "add_email":
                    print("Invalid email, try again.")
                if func.__name__=="add_birthday":
                    print("Invalid date format, try again.")
            except FutureDateException:
                print("You can't use a future date as a birthday, try again.")
    return wrapper   

@input_error
def add_name(addresbook: AddresBook) -> Name:
    while True:
        name = input("Type name or <<< if you want to cancel: ").strip().capitalize()
        if name in addresbook.keys():
            print(F"Contact {name} already exists. Choose another name.")
            continue
        elif name == "<<<":
            return None
        return Name(name)

@input_error
def add_phone():
    phone = input("Type phone or <<< if you want to cancel: ")
    if phone == "<<<":
        return None
    return Phone(phone)

@input_error
def add_email():
    email = input("Type email or <<< if you want to cancel: ")
    if email == "<<<":
        return None
    return Email(email)

@input_error
def add_birthday():
    birthday = input("Input the date of birth as day month year (e.g. 15-10-1985 or 15 10 1985) or <<< if you want to cancel: ")
    if birthday == "<<<":
        return None
    return Birthday(birthday)

# creare record in addresbook
def create_record(addresbook):
    name = add_name(addresbook)
    if name is not None:
        phones = []
        emails = []
        birthday = None
        while True:
            answer = input("Type Y (yes) if you want to add phone number: ").strip().upper()
            if answer == "Y":
                while True:
                    phone = add_phone()
                    if phone is not None:
                        phones.append(phone)                
                        answer = input("Type Y (yes) if you want to add another phone number: ").strip().upper()
                        if answer == "Y" or answer == "YES":
                            continue
                    break
            break
        while True:
            answer = input("Type Y (yes) if you want to add email: ").strip().upper()
            if answer == "Y":
                while True:
                    email = add_email()
                    if email is not None:
                        emails.append(email)
                        answer = input("Type Y (yes) if you want to add another email: ").strip().upper()
                        if answer == "Y" or answer == "YES":
                            continue
                    break
            break
        answer = input("Type Y (yes) if you want to add birthday: ").strip().upper()
        if answer == "Y":
            birthday = add_birthday()
        addresbook.add_record(Record(name, phones, emails, birthday))
    

# edit existing name
def edit_name(addresbook, record):
    print(f"Type new name for contact {record.name}")
    new_name = add_name(addresbook)
    addresbook.add_record(Record(new_name, record.phones, record.emails))  
    addresbook.pop(record.name.value)                 

# help menu function to choose email or phone 
def item_selection(record, data_list, show):
    print(f"Contact {record.name} {type}s:\n{show}", end="")
    number_to_change = input("Select by typing a number (for example 1 or 2): ")
    try:
        number_to_change = int(number_to_change) - 1
        if number_to_change >= len(data_list) or number_to_change < 0:
            raise ValueError
        return number_to_change
    except ValueError:
        return -1

# change of phone or email    
def change_data(record, type):
    if type == "phone":
        data_list = record.phones
        show = record.show_phones()
        add_type = record.add_phone
    elif type == "email":
        data_list = record.emails
        show = record.show_emails()
        add_type = record.add_email
    while True:
        if len(data_list) > 0:
            while True:
                answer = input(f"Contact {record.name} {type}s:\n{show}Do you want change it or add another? 1 chanege, 2 add, 3 delete: ")
                if answer == "1":
                    if len(data_list) == 1:
                        data_to_add = add_email() if type == "email" else add_phone()
                        if data_to_add is not None:
                            data_list[0] = data_to_add
                        break
                    else:
                        number_to_change = item_selection(record, data_list, show)
                        if number_to_change == -1:
                            print("Wrong option, try again")
                            break                            
                        data_to_add = add_email() if type == "email" else add_phone()
                        if data_to_add is not None:
                            data_list[number_to_change] = data_to_add
                        break 
                elif answer == "2":
                    data_to_add = add_email() if type == "email" else add_phone()
                    if data_to_add is not None:
                        add_type(data_to_add)
                    break
                elif answer == "3":
                    if len(data_list) == 1:
                        data_list.clear()
                        break
                    else:
                        number_to_delete = item_selection(record, data_list, show)
                        if number_to_delete == -1:
                            print("Wrong option, try again")
                            break  
                        print(f"{type} no {number_to_delete+1}: {data_list.pop(number_to_delete)} deleted.")
                        break
                else:
                    print("Unrecognized command, try again.")
        else:
            add_type(add_email() if type == "email" else add_phone())
        break
    
# init function for phone changed
def edit_phone(record):
    change_data(record, "phone")

# init function for email changed
def edit_email(record):
    change_data(record, "email")
            
# dict for menu edit handler
EDIT_COMMANDS = {
    "1": edit_name,
    "2": edit_phone,
    "3": edit_email,
    "4": add_birthday
}

# record edit
def edit_record(addresbook: AddresBook):
    while True:
        print(f"Your contacts:\n{addresbook.show_names()}")
        name = input("Type the name of the contact to edit: ").strip().title()
        if name in addresbook.keys():
            record = addresbook[name]
            break
        print("Unknown name, try again")
    while True:
        answer = input('What do you want to edit? Type: 1 name, 2 phone, 3 email, 4, birthday, 0 back to main menu: ')
        if answer in EDIT_COMMANDS.keys():
            handler = get_edit_handler(answer)
            handler(addresbook, record)
            break
        elif answer == "0":
            break   
        else:
            print("Wrong option, try again")

# delete record
def delete_record(addresbook):
    while True:
        print(f"Your contacts:\n{addresbook.show_names()}")
        name = input("Type contact name to delete or <<< if you want to cancel: ").strip().title()
        if name == "<<<":
            break
        if name in addresbook.keys():
            addresbook.pop(name)
            print(f"Contact {name} deleted.")
            break
        print(f'No contact "{name}" in addres book. Try again.')     
        
# show all data in addresbook
def show_all(addresbook):
    if len(addresbook) == 0:
        print("Your addresbook is empty.")
    else:
        i = 1
        for record in addresbook.values():
            print(f"{i}. {record.name}")
            if len(record.phones) > 0:
                print(f"phones:\n{record.show_phones()}")
            if len(record.emails) > 0:
                print(f"emails:\n{record.show_emails()}")
            if record.birthday is not None:
                print(f"birthday: {record.birthday}")
                print(f"Day(s) to next birthday: {record.days_to_birthday()}")
            i += 1           
             
# dict for main menu handler
MAIN_COMMANDS = {
    "0": cli_addresbook_exit,
    "1": create_record,
    "2": edit_record,
    "3": delete_record,
    "4": show_all,    
}


def main():
    adressbook = AddresBook()
    while True:
        print("{:<20} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10}".format("Type command (number): ","1 add", "2 edit", "3 delete", "4 show all", "0 exit"))

        option = input("> ").strip().lower()
        if option in MAIN_COMMANDS.keys():
            handler = get_main_handler(option)
            handler(adressbook)
        else:
            print("Wrong option, try again")       
                

if __name__ == "__main__":
    main()