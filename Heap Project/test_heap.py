import unittest
from heap.heap_operations import HeapOperations

class TestMaxHeap(unittest.TestCase):

    def setUp(self):
        """
        Set up a fresh heap for each test.
        """
        self.heap = HeapOperations()

    def test_insert(self):
        self.heap.insert(10)
        self.assertEqual(self.heap.get_heap(), [10])

    def test_extract_max(self):
        self.heap.insert(10)
        self.heap.insert(20)
        self.heap.insert(5)
        max_value = self.heap.extract_max()
        self.assertEqual(max_value, 20)
        self.assertEqual(self.heap.get_heap(), [10, 5])

    def test_empty_extract(self):
        self.assertIsNone(self.heap.extract_max())

    def test_heapify_up(self):
        self.heap.insert(10)
        self.heap.insert(20)
        self.assertEqual(self.heap.get_heap(), [20, 10])

    def test_heapify_down(self):
        self.heap.insert(10)
        self.heap.insert(20)
        self.heap.insert(15)
        self.heap.extract_max()  # Should remove 20
        self.assertEqual(self.heap.get_heap(), [15, 10])

if __name__ == '__main__':
    unittest.main()
