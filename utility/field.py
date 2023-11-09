class Field:
    """
    class defining the basic properties of a field
    """
    def __init__(self, value="") -> None:
        self.value = value
    
    # overridden method __str__    
    def __repr__(self) -> str:
        return f"{self._value}"
    
            
    # Getter for value
    @property
    def value(self):
        return self._value
    
    
    # Setter for value
    @value.setter
    def value(self, value):
        self._value = value
        