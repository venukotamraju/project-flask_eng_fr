import unittest

from translator import english_to_french, french_to_english

class testEnglishToFrench(unittest.TestCase):
    
    def test1(self):
        
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('Bye'), 'Bonjour')



class TestFrenchToEnglish(unittest.TestCase):

    def test1(self):

        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bye')

unittest.main()