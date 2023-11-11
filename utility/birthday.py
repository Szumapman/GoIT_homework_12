from datetime import datetime
from utility.field import Field

class FutureDateException(Exception):
    pass
    
class Birthday(Field):
         
    def __init__(self, value=None) -> None:
        self._value = self._set_birthdate(value)
        
        # Getter for value
    @property
    def value(self):
        return self._value 
         
    # Setter for value   
    @value.setter
    def value(self, value: str): 
        self._value = self._set_birthdate(value)
        
    # overridden method __repr__    
    def __repr__(self) -> str:
        return self._value.strftime('%A %d-%m-%Y')
    
    #
    def _set_birthdate(self, value):
        if value is None:
            return None
        birthday = datetime.strptime(value.strip().replace(".", " ").replace("/", " ").replace("-", " ").replace(".", " "), '%d %m %Y').date()
        if birthday is not None and birthday > datetime.now().date():
            raise FutureDateException
        return birthday 