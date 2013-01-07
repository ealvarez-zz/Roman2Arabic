from Roman2Arabic import Roman2Arabic, InvalidRomanNumberException
import unittest


class Roman2ArabicTest(unittest.TestCase):
    
    def setUp(self):
        self.roman_2_arabic = Roman2Arabic()
    
    def test_is_roman_single_non_roman_chars(self):    
        
        
        # Arrange
        non_roman_chars = ["T", "i", "K", 3, "p", 5, "8"]
        actual_values = []
        
        # Act
        [actual_values.append(self.roman_2_arabic.is_roman(char)) for char in non_roman_chars]
        
        # Assert
        for actual in actual_values:
            self.assertFalse(actual)
            
            
    def test_is_roman_single_roman_chars(self):
        
        # Arrange
        roman_chars = ["I", "V", "X", "L", "C", "D", "M"]
        actual_values = []
        
        # Act
        [actual_values.append(self.roman_2_arabic.is_roman(char)) for char in roman_chars]
        
        # Assert
        for actual in actual_values:
            self.assertTrue(actual)
        
    def test_is_roman_string_containing_non_roman_chars(self):
        
        # Arrange
        invalid_roman_strings = ["XTIX", "CCCK", "XVS", "XX1X"]
        actual_values = []
        
        # Act
        [actual_values.append(self.roman_2_arabic.is_roman(char)) for char in invalid_roman_strings]
        
        # Assert
        for actual in actual_values:
            self.assertFalse(actual)
            

if __name__ == 'main':
    unittest.main()
    






