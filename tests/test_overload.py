import unittest

from mop.overload import overload


class OverloadTestCase(unittest.TestCase):
    def test_base(self):
        @overload
        def test_func(*args, **kwargs):
            raise NotImplementedError("")

        @test_func.register
        def _(a):
            return a

        @test_func.register
        def _(a, b):
            return a - b

        @test_func.register
        def _(a, b=-1):
            return a + b

        @test_func.register
        def _(a, b, c):
            return [a, b, c]

        test_obj = object()
        self.assertEqual(test_obj, test_func(test_obj))
        self.assertEqual(2, test_func(1, 1))
        self.assertEqual(0, test_func(1, b=-1))
        self.assertEqual([1, 2, 3], test_func(1, b=2, c=3))
        print(test_func.__doc__)


if __name__ == '__main__':
    unittest.main()
