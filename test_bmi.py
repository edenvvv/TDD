import unittest
from bmi import bmi_calc, bmi_status


class MyTestCase(unittest.TestCase):
    def test_bmi(self):
        result = bmi_calc(1.89, 90)
        self.assertEqual(result, 25.2)
        result = bmi_calc(1.48, 95)
        self.assertEqual(result, 43.37)
        result = bmi_calc(0, 95)
        self.assertEqual(result, "cant divide by 0")
        result = bmi_calc(-1, 59)
        self.assertEqual(result, "unacceptable values")
        result = bmi_calc(-11, -549)
        self.assertEqual(result, "unacceptable values")
        result = bmi_calc(61, -5)
        self.assertEqual(result, "unacceptable values")

    def bmi_status(self):
        result = bmi_status(0)
        self.assertEqual(result, "unacceptable values")
        result = bmi_status(17)
        self.assertEqual(result, "Underweight")
        result = bmi_status(20)
        self.assertEqual(result, "Normal weight")
        result = bmi_status(28)
        self.assertEqual(result, "Overweight")
        result = bmi_status(31)
        self.assertEqual(result, "Obesity Rank 1")
        result = bmi_status(37)
        self.assertEqual(result, "Obesity Rank 2")
        result = bmi_status(45)
        self.assertEqual(result, "Obesity Rank 3")


if __name__ == '__main__':
    unittest.main()
