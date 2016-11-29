import unittest
from app.foo import Foo

class TestFoo(unittest.TestCase):

    def test_contextual_bar(self):
        test_string = 'baz'
        f = Foo(test_string)
        self.assertEqual(f.bar_context(), 'From bar class - this is bar: baz')

if __name__ == '__main__':
    unittest.main()
