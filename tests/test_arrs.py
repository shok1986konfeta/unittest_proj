import unittest
from utils.arrs import get, my_slice


class TestArrayFunctions(unittest.TestCase):
    def test_get_existing_index(self):
        array = [1, 2, 3, 4, 5]
        result = get(array, 2)
        self.assertEqual(result, 3)

    def test_get_nonexistent_index(self):
        array = [1, 2, 3, 4, 5]
        result = get(array, 10, default='Not Found')
        self.assertEqual(result, 'Not Found')

    def test_my_slice_with_positive_indices(self):
        array = [1, 2, 3, 4, 5]
        result = my_slice(array, start=1, end=4)
        self.assertEqual(result, [2, 3, 4])

    def test_my_slice_with_negative_indices(self):
        array = [1, 2, 3, 4, 5]
        result = my_slice(array, start=-3, end=-1)
        self.assertEqual(result, [3, 4])

    def test_my_slice_default_values(self):
        array = [1, 2, 3, 4, 5]
        result = my_slice(array)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_my_slice_end_greater_than_length(self):
        array = [1, 2, 3, 4, 5]
        result = my_slice(array, end=10)
        self.assertEqual(result, [1, 2, 3, 4, 5])




if __name__ == '__main__':
    unittest.main()
