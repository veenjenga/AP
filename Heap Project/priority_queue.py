 from heap.heap_operations import HeapOperations

class PriorityQueue:
    def __init__(self):
        self.heap = HeapOperations()

    def add_task(self, task, priority):
        """
        Adds a task with a given priority.
        """
        self.heap.insert((priority, task))

    def get_next_task(self):
        """
        Retrieves the next task with the highest priority.
        """
        if not self.heap.get_heap():
            return None
        return self.heap.extract_max()[1]


