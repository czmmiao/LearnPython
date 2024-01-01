from collections import deque

class Queue():
    def __init__(self):
        self._elements = deque()

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self._elements) >0:
            yield self.dequeue()
    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()

class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()



fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")
# print(fifo.dequeue())
# print(fifo.dequeue())
# print(fifo.dequeue())


lifo = Stack()
lifo.enqueue("1st")
lifo.enqueue("2nd")
lifo.enqueue("3rd")

for element in fifo:
    print(element)

for element in lifo:
    print(element)


from heapq import heappush, heappop
from itertools import count
class PriorityQueue:
    def __init__(self):
        self._elements = []
        self._count = count()

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self._elements) >0:
            yield self.dequeue()
    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._count), value)
        heappush(self._elements, element)
    def dequeue(self):
        return heappop(self._elements)[-1]

messages = PriorityQueue()
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1
messages = PriorityQueue()
messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")
print(messages.dequeue())


for element in messages:
    print(element)