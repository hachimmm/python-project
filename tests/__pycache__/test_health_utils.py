import unittest
from health_utils import calculate_bmi, calculate_bmr  # Import absolu

class TestHealthUtils(unittest.TestCase):
    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(1.75, 70), 22.86, places=2)

    def test_calculate_bmr_male(self):
        result = calculate_bmr(175, 70, 30, 'male')
        self.assertAlmostEqual(result, 1695.67, places=2)

    def test_calculate_bmr_female(self):
        result = calculate_bmr(175, 70, 30, 'female')
        self.assertAlmostEqual(result, 1507.13, places=2)

if __name__ == '__main__':
    unittest.main()