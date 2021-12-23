class BFS:
    def __init__(self, start, w, h) -> None:
        self.visited = []
        self.queue = [start]
        self.w, self.h = w, h
        self.parents = {}

    def step(self, walls, end=None):
        next = self.queue.pop(0)
        if next in self.visited or next in walls:
            return self.step(walls)
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
                self.queue.append(n)
                self.parents[n] = next
        
        return self.visited

    def backtrace(self, end, start):
        path = []
        curr = end
        while curr != start:
            path.append(curr)
            parent = self.parents[curr]
            curr = parent
        
        return path
