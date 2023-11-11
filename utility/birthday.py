from datetime import datetime, timedelta
from utility.field import Field

class Birthday(Field):
    def _value_error(func):
        def wrapper(self, value):
            try:
                return func(self, value.strip().replace(".", " ").replace("/", " ").replace("-", " ").replace(".", " "))
            except ValueError:
                raise ValueError
        return wrapper
    
    @_value_error
    def __init__(self, value=None) -> None:
        self._value = datetime.strptime(value.strip().replace(".", " ").replace("/", " ").replace("-", " ").replace(".", " "), '%d %m %Y')
        
        # Getter for value
    @property
    def value(self):
        return self._value 
         
    # Setter for value   
    @value.setter
    @_value_error
    def value(self, value: str):
        self._value = value
        
    # overridden method __repr__    
    def __repr__(self) -> str:
        return self._value.strftime('%A %d-%m-%Y')