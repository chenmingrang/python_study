import unittest
from unit_test.mydict import MyDict
class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp....')

    def test_init(self):
        d = MyDict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def tearDown(self):
        print('tearDown...')


"""
    编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
    以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行
"""

"""
    可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
"""

if __name__=='__main__':
    unittest.main()
