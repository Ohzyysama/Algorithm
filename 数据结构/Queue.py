class Queue:
    def __init__(self, size=10):
        self.front = 0
        self.rear = 0
        self.size = size
        self.queue = [0 for _ in range(size)]

    def push(self, n):
        if self.rear + 1== self.size :
            raise IndexError("full!")
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = n

    def pop(self):
        if self.front == self.rear:
            raise IndexError("empty!")
        self.front = (self.front + 1) % self.size
        a =  self.queue.pop(self.front)
        return a

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.size == self.front


q = Queue(6)
for i in range(5):
    q.push(i)
print(q.isFull())
q.pop()
q.pop()
print(q.queue)