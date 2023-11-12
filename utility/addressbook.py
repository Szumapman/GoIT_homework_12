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

    # implementation of the iterator method which returns a generator
    def iterator(self, no_of_contacts_to_return=3):
        if len(self.data) > 0:
            current_record_no = 1
            i = 1
            records_info = ""
            for record in self.values():
                records_info += f"{i}. {record.name}"
                if len(record.phones) > 0:
                    records_info += f"\nphones:{record.show_phones()}"
                if len(record.emails) > 0:
                    records_info += f"\nemails:{record.show_emails()}"
                if record.birthday is not None:
                    records_info += (
                        f"\nbirthday:\n{record.birthday}\n{record.days_to_birthday()}"
                    )
                records_info += "\n-------------\n"
                i += 1
                if current_record_no >= no_of_contacts_to_return:
                    yield records_info
                    current_record_no = 1
                    records_info = ""
                    continue
                current_record_no += 1
            yield records_info  # returns the rest if there are no more records and record_no < no_of_contacts_to_return
        else:
            yield "Your addresbook is empty.\n"
