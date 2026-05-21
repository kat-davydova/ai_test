import unittest

from code import is_leap


class TestIsLeap(unittest.TestCase):
    def test_common_year(self):
        self.assertFalse(is_leap(1))

    def test_divisible_by_4(self):
        self.assertTrue(is_leap(4))

    def test_century_not_leap(self):
        self.assertFalse(is_leap(100))
        self.assertFalse(is_leap(1900))
        self.assertFalse(is_leap(2100))

    def test_century_leap(self):
        self.assertTrue(is_leap(400))
        self.assertTrue(is_leap(2000))
        self.assertTrue(is_leap(2400))

    def test_zero_year_raises(self):
        with self.assertRaises(ValueError):
            is_leap(0)

    def test_negative_year_raises(self):
        with self.assertRaises(ValueError):
            is_leap(-4)

    def test_invalid_type_raises(self):
        with self.assertRaises(TypeError):
            is_leap(2024.0)
        with self.assertRaises(TypeError):
            is_leap('2024')
        with self.assertRaises(TypeError):
            is_leap(True)

    def test_recent_years(self):
        self.assertFalse(is_leap(2023))
        self.assertTrue(is_leap(2024))

    def test_large_year(self):
        self.assertTrue(is_leap(100000))
        self.assertFalse(is_leap(100001))


if __name__ == '__main__':
    unittest.main()
