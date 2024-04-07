import unittest

class MergeSortTest(unittest.TestCase):
  def test_merge_sort(self):
    arr = [5, 3, 1, 2, 4]
    sorted_arr = [1, 2, 3, 4, 5]
    result = merge_sort(arr)
    self.assertEqual(result, sorted_arr)

if __name__ == '__main__':
  unittest.main()
