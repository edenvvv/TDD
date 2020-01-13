import unittest
import bubbleSort


class BubbleSortTest(unittest.TestCase):
    def test_is_array_sorted(self):
        # stub
        stub1 = [10, 5, 7, 4, 2, 12, 4]
        stub2 = [21, -2, 6, -10, 18, 17, 0]
        stub3 = [1, 0, 0, 9, 23, 71, 62]

        # assume
        expected1 = [2, 4, 4, 5, 7, 10, 12]
        expected2 = [-10, -2, 0, 6, 17, 18, 21]
        expected3 = [0, 0, 1, 9, 23, 62, 71]

        # action
        result1 = bubbleSort.bubble_sort(stub1)
        result2 = bubbleSort.bubble_sort(stub2)
        result3 = bubbleSort.bubble_sort(stub3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

    def test_is_array_lost_arg(self):
        def is_arr_lost_arg(arr, other_arr):
            if len(arr) != len(other_arr):
                return False
            for arg in arr:
                if arg not in other_arr:
                    return False
            return True

        # stub
        stub1 = [1, 5, 3, 4, 2]
        stub2 = [2, 1, 5, 4]

        # assume
        expected1 = [1, 4, 12]
        expected2 = bubbleSort.bubble_sort(stub2)

        # action
        result1 = is_arr_lost_arg(stub1, expected1)
        result2 = is_arr_lost_arg(stub2, expected2)

        # confirm length of arrays and values are not lost
        self.assertFalse(result1)
        self.assertTrue(result2)
        # confirms return value
        self.assertIsNotNone(result1)


if __name__ == '__main__':
    unittest.main()
