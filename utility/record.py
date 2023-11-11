from utility.name import Name
from utility.phone import Phone
from utility.email import Email
# from utility.birthday import Birthday

class Record:
    """
    Record class represents a single address book record consisting of name, phone list and email list
    """
    def __init__(self, name: Name, phones=[], emails=[], birthday=None) -> None:
        self._name = name
        self._phones = phones
        self._emails = emails
        self._birthday = birthday
        
    # Getter for name
    @property
    def name(self):
        return self._name

    # Getter for phones
    @property
    def phones(self):
        return self._phones

    # Getter for emails
    @property
    def emails(self):
        return self._emails
    
    # Getter for birthday
    @property
    def birthday(self):
        return self._birthday
    
    # Setter name
    @name.setter
    def name(self, name):
        self._name = name
    
    # Setter phones
    @phones.setter
    def phones(self, phones):
        self._phones = phones
       
    # Setter emails
    @emails.setter
    def emails(self, emails):
        self._emails = emails

    # Setter birthday
    @birthday.setter
    def birthday(self, birthday):
        self._birthday = birthday
        
    # Add phone to phones list    
    def add_phone(self, phone: Phone):
        self._phones.append(phone)
    
    # Remove phone from phones list
    def remove_phone(self, phone: Phone):
        self._phones.remove(phone)
    
    # Change phone - add new one and remove old one
    def change_phone(self, old_phone, new_phone):
        index = self._phones.index(old_phone)
        self._phones[index] = new_phone

    # Show return formated string with all phones 
    def show_phones(self):
        phones_str = ""
        i = 1
        for phone in self._phones:
            phones_str += f"{i}) {phone};\n"
            i += 1
        return phones_str
    
    # Add email to emails list
    def add_email(self, email: Email):
        self._emails.append(email)


    # Remove email from emails list
    def remove_email(self, email: Email):
        self._emails.remove(email)
    
    # Change email - add new one an dremove old one
    def change_email(self, old_email, new_email):
        index = self._emails.index(old_email)
        self._emails[index] = new_email    
    
    # Show return formated string with all emails                  
    def show_emails(self):
        emails_str = ""
        i = 1
        for email in self._emails:
            emails_str += f"{i}) {email};\n"
            i += 1
        return emails_str
    
    def __repr__(self) -> str:
        return f"{self._name}"