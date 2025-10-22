import unittest
from delivery import get_riders_wage

class MyTestCase(unittest.TestCase):
	def test_get_riders_wage(self):
		result = get_riders_wage(30)
		self.assertEqual(result,9800)

	def test_that_the_second_check_returns_true(self):
		result = get_riders_wage(51)
		self.assertEqual(result,15200)

	def test_that_the_third_check_returns_true(self):
		result = get_riders_wage(65)
		self.assertEqual(result,21250)

	def test_that_the_last_check_returns_true(self):
		result = get_riders_wage(80)
		self.assertEqual(result,45000)


		