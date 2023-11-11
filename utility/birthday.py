from datetime import datetime, timedelta
from utility.field import Field

class FutureDateException(Exception):
    pass
    
class Birthday(Field):
        
    def __init__(self, value=None) -> None:
        birthday = datetime.strptime(value.strip().replace(".", " ").replace("/", " ").replace("-", " ").replace(".", " "), '%d %m %Y')
        if birthday is not None and birthday > datetime.now():
            raise FutureDateException 
        self._value = birthday
        
        # Getter for value
    @property
    def value(self):
        return self._value 
         
    # Setter for value   
    @value.setter
    def value(self, value: str):
        birthday = datetime.strptime(value.strip().replace(".", " ").replace("/", " ").replace("-", " ").replace(".", " "), '%d %m %Y')
        if birthday is not None and birthday > datetime.now():
            raise FutureDateException 
        self._value = birthday
        
    # overridden method __repr__    
    def __repr__(self) -> str:
        return self._value.strftime('%A %d-%m-%Y')