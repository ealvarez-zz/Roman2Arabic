class Roman2Arabic(object):

    roman_values = {"I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000}
    
    def __init__(self):
        pass
    
    def transform(self, roman_number):
        
        if(not self.is_roman(roman_number)):
            raise InvalidRomanNumberException(roman_number)
        else:
            return self._get_value(roman_number)
    
    def _get_value(self, roman):
        return self.roman_values[roman]

    def is_roman(self, char):
        roman_chars = self.roman_values.keys()
        return (char in roman_chars)

class InvalidRomanNumberException(Exception):
    
    def __init__(self, value):
        
        self.msg  = "Invalid roman number character %s" % value
        self.value = value
    