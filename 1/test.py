import unittest
from dict_compare import DictCompare1
from dict_compare2 import DictCompare2
from dict_compare3 import DictCompare3


class Test(unittest.TestCase):
    def setUp(self):
        self.a:dict = {'a': {'a1': 1}, 'b': {'b1': 1}}
        self.b:dict = {'a': {'a1': 2}, 'b': {'b1': 2}}

    def test_compare1(self):
        res1:dict = DictCompare1.compare(self.a,self.b)
        self.assertTrue(res1, {})


    def test_compare2(self):
        res2:dict = DictCompare2.compare(self.a,self.b)
        self.assertTrue(res2, {})

    def test_compare3(self):
        res3:dict = DictCompare3.compare(self.a,self.b)
        self.assertTrue(res3, {})



if __name__ == '__main__':
    unittest.main()
