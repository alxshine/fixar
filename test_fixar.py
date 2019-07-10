from fixar import *
import unittest

class TestHelpers(unittest.TestCase):
    def test_BitMask(self):
        self.assertEqual(BitMask(8), 0xff)
        self.assertEqual(BitMask(20)+1, 1<<20)

    def test_BitNot(self):
        self.assertEqual(BitNot(0x01, 8), 0xfe)
        self.assertEqual(BitNot(0x10, 8), 0xef)

class TestFixedInt(unittest.TestCase):
    
        
if __name__ == '__main__':
    unittest.main()
