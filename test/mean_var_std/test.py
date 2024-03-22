import unittest 
from python_repo.src..mean_var_std.util import calculate_statistics

class Testcalculatestatistics(unitTest.TestCase):
  def test_calculate_statistics(self):
    mean,var,std=calculate_statistics()
    actual_input=[[1,2,3],[4,5,6]]
    expected_mean=[2.0,5.0]
    expected_var=[2.0,2.0,2.0]
    expected_std=1.707
    self.asserEqual(actual_input.tolist(),expected_mean)
    self.asserEqual(actual_input.tolist(),expected_var)
    self.asserEqual(actual_input.tolist(),expected_std)
