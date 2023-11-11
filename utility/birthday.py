from datetime import datetime, timedelta
from utility.field import Field

class FutureDateException(Exception):
    pass
    
class Birthday(Field):
         
    def __init__(self, value=None) -> None:
        self._value = self.set_birthdate(value)
        
        # Getter for value
    @property
    def value(self):
        return self._value 
         
    # Setter for value   
    @value.setter
    def value(self, value: str): 
        self._value = self.set_birthdate(value)
        
    # overridden method __repr__    
    def __repr__(self) -> str:
        return self._value.strftime('%A %d-%m-%Y')
    
    def set_birthdate(self, value):
        if value is None:
            return None
        birthday = datetime.strptime(value.strip().replace(".", " ").replace("/", " ").replace("-", " ").replace(".", " "), '%d %m %Y')
        if birthday is not None and birthday > datetime.now():
            raise FutureDateException
        return birthday 