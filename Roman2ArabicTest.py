from Roman2Arabic import Roman2Arabic, InvalidRomanNumberException
import unittest


class Roman2ArabicTest(unittest.TestCase):
    
    def setUp(self):
        self.roman_2_arabic = Roman2Arabic()
    
    def test_non_roman_chars_as_input(self):    
        
        non_roman_chars = ["T", "i", 3]
        
        for invalid_char in non_roman_chars:
            self.assertRaises(InvalidRomanNumberException, self.roman_2_arabic.transform, invalid_char)
            
            

if __name__ == 'main':
    unittest.main()
    






