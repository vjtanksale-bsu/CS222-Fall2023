import unittest
def BinarySearch(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False
class TestBinarySearch(unittest.TestCase):
    def test_Found(self):
        numbers = [2, 5, 10, 20, 50, 100]
        target = 5
        result = BinarySearch(numbers, target)
        self.assertTrue(result)
    def test_NotFound(self):
        numbers = list(range(0, 2000))
        target = 5000
        result = BinarySearch(numbers, target)
        self.assertFalse(result)
    def test_FoundLongList(self):
        numbers = list(range(0, 2000))
        target = 1000
        result = BinarySearch(numbers, target)
        self.assertTrue(result)
if __name__ == "__main__":
    unittest.main()