import unittest

class TestSum(unittest.TestCase):
  def test_year(self):
    self.assertEqual(diff(current_mileage, last_service_mileage), 30000)

  def test_diff(self):
    self.assertEqual(diff(current_mileage,last_service_mileage), 60000)

if __name__ == '__main__':
    unittest.main()
