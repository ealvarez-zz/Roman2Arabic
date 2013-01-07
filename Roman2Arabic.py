class Roman2Arabic(object):
    
    
    def __init__(self):
        pass
    
    
    def transform(self, roman_number):
        raise InvalidRomanNumberException(roman_number)
    


class Roman2ArabicException(Exception):
    pass


class InvalidRomanNumberException(Roman2ArabicException):
    
    def __init__(self, value):
        
        self.msg  = "Invalid roman number character %s" % value
        self.value = value
    