from collections import UserDict

from utility.record import Record


class AddresBook(UserDict):
    """
    The Record class extends the UserDict class by adding the add_record method 
    and checking that the items added to the dictionary are valid (keys and values based on the Record class). 

    Args:
        UserDict (class): parent class
    """
    
    # function used as a decorator to catch errors when item is adding to addresbook
    def _value_error(func):
        def inner(self, record):
            if not isinstance(record, Record):
                raise ValueError
            return func(self, record)
        return inner
    
    # Add record to addresbook
    @_value_error
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    # Return all names (keys) from addresbook as formated string
    def show_names(self):
        names = []
        for key in self.keys():
            names.append(key)
        names.sort()
        return "\n".join(names)
    

    
    