import heapq
from collections import deque
from collections import namedtuple

# Min-heap example
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)

print(heapq.heappop(heap))  # Output: 1
print(heapq.heappop(heap))  # Output: 5
print(heapq.heappop(heap))  # Output: 10

# Deque example
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)  # Output: deque([0, 1, 2, 3, 4])

# Namedtuple example
Point = namedtuple('Point', 'x y')
p = Point(10, 20)
print(p.x, p.y)  # Output: 10 20
