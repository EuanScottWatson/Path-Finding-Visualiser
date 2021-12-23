import numpy as np


class AStar:
    def __init__(self, start, w, h) -> None:
        self.visited = []
        self.pqueue = PriorityQueue()
        self.w, self.h = w, h
        self.parents = {}
        self.start = start

        self.pqueue.add(start, 0)

    def step(self, walls, end=None):
        next = self.pqueue.pop()
        if next in self.visited or next in walls:
            return self.step(walls, end)
        self.visited.append(next)

        to_visit = [
            (next[0]+1, next[1]),
            (next[0], next[1]+1),
            (next[0]-1, next[1]),
            (next[0], next[1]-1)
            ]

        for n in to_visit:
            if (n not in self.visited and 
                n not in walls and
                0 <= n[0] <= self.w and 
                0 <= n[1] <= self.h):
                weight = self.distance(n, self.start) + self.distance(n, end)
                self.pqueue.add(n, weight)
                self.parents[n] = next
        
        return self.visited

    def distance(self, a, b):
        return np.linalg.norm(np.array(a) - np.array(b))

    def backtrace(self, end, start):
        path = []
        curr = end
        while curr != start:
            path.append(curr)
            parent = self.parents[curr]
            curr = parent
        
        return path


class PriorityQueue:
    def __init__(self) -> None:
        self.items = []
        self.priorities = []

    def add(self, item, p):
        self.items.append(item)
        self.priorities.append(p)

    def pop(self):
        index = np.argmin(self.priorities)
        self.priorities.pop(index)
        return self.items.pop(index)