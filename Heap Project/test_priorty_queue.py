import unittest
from priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        """
        Set up a fresh priority queue for each test.
        """
        self.pq = PriorityQueue()

    def test_add_task(self):
        self.pq.add_task("Task A", 3)
        self.assertEqual(self.pq.get_next_task(), "Task A")

    def test_get_next_task(self):
        self.pq.add_task("Task A", 3)
        self.pq.add_task("Task B", 5)
        self.pq.add_task("Task C", 1)
        self.assertEqual(self.pq.get_next_task(), "Task B")
        self.assertEqual(self.pq.get_next_task(), "Task A")
        self.assertEqual(self.pq.get_next_task(), "Task C")
        self.assertIsNone(self.pq.get_next_task())

if __name__ == '__main__':
    unittest.main()
