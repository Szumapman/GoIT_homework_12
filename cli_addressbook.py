import sys
from typing import Callable
from utility.addressbook import AddresBook
from utility.record import Record
from utility.name import Name
from utility.phone import Phone
from utility.email import Email

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
                func(*args)
                break
            except ValueError:
                if func.__name__ == "add_name":
                    print("The name field cannot be empty, try again.")
                if func.__name__ == "add_phone":
                    print("Invalid phone number, try again.")
                if func.__name__ == "add_email":
                    print("Invalid email, try again.")
    return wrapper   

@input_error
def add_name(addresbook):
    while True:
        name = input("Name: ").strip().capitalize()
        if name in addresbook.keys():
            print(F"Contact {name} already exists. Choose another name.")
            continue
        return Name(name)

@input_error
def add_phone():
    return Phone(input("phone: "))

@input_error
def add_email():
    return Email(input("email: "))

# creare record in addresbook
def create_record(addresbook):
    while True:
        name = add_name(addresbook)
        phones = []
        emails = []
        break
    while True:
        answer = input("Type Y (yes) if you want to add phone number: ").strip().upper()
        if answer == "Y":
            while True:
                phones.append(add_phone())                
                answer = input("Type Y (yes) if you want to add another phone number: ").strip().upper()
                if answer == "Y" or answer == "YES":
                    continue
                break
        break
    while True:
        answer = input("Type Y (yes) if you want to add email: ").strip().upper()
        if answer == "Y":
            while True:
                emails.append(add_email())
                answer = input("Type Y (yes) if you want to add another email: ").strip().upper()
                if answer == "Y" or answer == "YES":
                    continue
                break
        break      
    addresbook.add_record(Record(name, phones, emails))

# edit existing name 
def edit_name(addresbook, record):
    while True:
        new_name = input(f"Type new name for contact {record.name}: ")
        if new_name in addresbook.keys():
            print(F"Contact {new_name} already exists. Choose another name.")
            continue
        new_name = Name(new_name)
        addresbook.add_record(Record(new_name, record.phones, record.emails))  
        addresbook.pop(record.name.value)                 
        break

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
        class_object = Phone
        add_type = record.add_phone
    elif type == "email":
        data_list = record.emails
        show = record.show_emails()
        class_object = Email
        add_type = record.add_email
    while True:
        if len(data_list) > 0:
            while True:
                answer = input(f"Contact {record.name} {type}s:\n{show}Do you want change it or add another? 1 chanege, 2 add, 3 delete: ")
                if answer == "1":
                    if len(data_list) == 1:
                        data_list[0] = class_object(input(f"new {type}: "))
                        break
                    else:
                        number_to_change = item_selection(record, data_list, show)
                        if number_to_change == -1:
                            print("Wrong option, try again")
                            break                            
                        data_list[number_to_change] = class_object(input(f"new {type}: "))
                        break 
                elif answer == "2":
                    add_type(input(f"new {type}: "))
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
            add_type(input(f"{type} to add: "))
        break
    
# init function for phone changed
def edit_phone(addresbook, record):
    change_data(record, "phone")

# init function for email changed
def edit_email(addresbook, record):
    change_data(record, "email")
            
# dict for menu edit handler
EDIT_COMMANDS = {
    "1": edit_name,
    "2": edit_phone,
    "3": edit_email,
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
        answer = input('What do you want to edit? Type: 1 name, 2 phone, 3 email, 0 back to main menu: ')
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