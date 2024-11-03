from collections import deque  # 队列的内置模块

q = deque([1, 3])
q.appendleft(5)
print(q)
q.popleft()
print(q)
