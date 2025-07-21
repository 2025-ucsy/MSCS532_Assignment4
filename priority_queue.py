import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, priority, item):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        if self._queue:
            return heapq.heappop(self._queue)[-1]
        raise IndexError("pop from empty priority queue")

    def is_empty(self):
        return len(self._queue) == 0

# Example Task class (if needed)
class Task:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Task({self.name})'
