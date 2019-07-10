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
    def setUp(self):
        self.v_a = 42
        self.v_b = 13
        self.v_c = 1337
        self.a = FixedInt(self.v_a, 8)
        self.b = FixedInt(self.v_b, 8)
        self.c = FixedInt(self.v_c, 32)
    
    def test_add(self):
        self.assertRaises(TypeError, lambda x, y: a+c)
        v = self.a+self.b
        self.assertEqual(v.value, self.v_a+self.v_b)
        
    def test_sub(self):
        self.assertRaises(TypeError, lambda x, y: a-c)
        v = self.a-self.b
        self.assertEqual(v.value, self.v_a-self.v_b)
        #negatives are tested in test_neg
        
    def test_mul(self):
        self.assertRaises(TypeError, lambda x, y: a*c)
        v = self.a*self.b
        self.assertEqual(v.value, (self.v_a*self.v_b)&0xff)

    def test_div(self):
        self.assertRaises(TypeError, lambda x, y: a/c)
        v = self.a/self.b
        self.assertEqual(v.value, self.v_a//self.v_b)
        
    def test_mod(self):
        self.assertRaises(TypeError, lambda x, y: a%c)
        v = self.a%self.b
        self.assertEqual(v.value, self.v_a%self.v_b)
        
    def test_pow(self):
        self.assertRaises(TypeError, lambda x, y: a**c)
        v = self.a**self.b
        self.assertEqual(v.value, (self.v_a**self.v_b)&0xff)
        
    def test_lt(self):
        self.assertRaises(TypeError, lambda x, y: a<c)
        
    def test_gt(self):
        self.assertRaises(TypeError, lambda x, y: a>c)
        
    def test_le(self):
        self.assertRaises(TypeError, lambda x, y: a<=c)
        
    def test_ge(self):
        self.assertRaises(TypeError, lambda x, y: a>=c)
        
    def test_eq(self):
        self.assertRaises(TypeError, lambda x, y: a==c)
        
    def test_ne(self):
        self.assertRaises(TypeError, lambda x, y: a!=c)
        
    def test_neg(self):
        v = FixedInt(0x22, 8)
        neg_v = (-v).value
        self.assertEqual(neg_v, 0xde)
        
    def test_invert(self):
        self.assertRaises(TypeError, lambda x, y: a+c)
        
    
if __name__ == '__main__':
    unittest.main()
