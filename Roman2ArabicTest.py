from Roman2Arabic import Roman2Arabic, InvalidRomanNumberException
import unittest


class Roman2ArabicTest(unittest.TestCase):
    
    def setUp(self):
        self.roman_2_arabic = Roman2Arabic()
    
    def test_single_non_roman_chars(self):    
        
        non_roman_chars = ["T", "i", "K", 3, "p", 5, "8"]
        
        for expected_invalid_char in non_roman_chars:
            self.assertRaises(InvalidRomanNumberException, self.roman_2_arabic.transform, expected_invalid_char)
            
            
    def test_single_roman_chars(self):
        
        # Arrange
        roman_chars = ["I", "V", "X", "L", "C", "D", "M"]
        actual_values = []
        expected_value = [1, 5, 10, 50, 100, 500, 1000]
        
        # Act
        [actual_values.append(self.roman_2_arabic.transform(char)) for char in roman_chars]
        actual_values.sort()
        
        # Assert
        self.assertSequenceEqual(actual_values, expected_value)
        

if __name__ == 'main':
    unittest.main()
    






