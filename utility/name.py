from utility.field import Field


class Name(Field):
    """
    class for name object  

    Args:
        Field (class): parent class
    """
    def __init__(self, value: str) -> None:
        self.value = value
        
        
    # function used as a decorator to catch errors when value is setting
    def _value_error(func):
        def inner(self, value):
            while True:
                if not value:
                    value = input("The name field cannot be empty. Try again: ")
                else:
                    return func(self, value)
        return inner
    
    # Getter for value
    @property
    def value(self):
        return self._value
        
    # Setter for value
    @value.setter
    @_value_error
    def value(self, value):
        self._value = value