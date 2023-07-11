import unittest

class TestSum(unittest.TestCase):
  def test_year(self):
    self.assertEqual(diff(current_date, last_service_date), 3)

  def test_diff(self):
    self.assertEqual(diff(current_date,last_service_date), 4)

if __name__ == '__main__':
    unittest.main()
