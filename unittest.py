import unittest


class TestMyFunction(unittest.TestCase):
    def test_addition(self):
        result = add(1, 2)
        self.assertEqual(result, 3)


def add(a, b):
    return a + b


# 使用示例
if __name__ == "__main__":
    unittest.main()
