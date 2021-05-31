import unittest
from reverse import reverse_sent


class TestReverse(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(reverse_sent("My name is Garrett"), "Garrett is name My")

    def test_single(self):
        self.assertEqual(reverse_sent("Name"), "Name")
    
    def test_space(self):
        self.assertEqual(reverse_sent(" "), " ")
    
    def test_empty(self):
        self.assertEqual(reverse_sent(""), "")
    
if __name__ == "__main__":
    unittest.main()