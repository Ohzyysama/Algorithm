maze1 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]

maze2 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1]
]


dir = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]

from collections import deque
def maze_path_stack(x1, y1, x2, y2):
    stack = [(x1, y1)]
    while len(stack) > 0:
        cur = stack[-1]
        if cur[0] == x2 and cur[1] == y2:
            for p in stack:
                print(p)
            return True
        for i in dir:
            next = i(cur[0], cur[1])
            if maze1[next[0]][next[1]] == 0:
                stack.append(next)
                maze1[next[0]][next[1]] = 2
                break
        else:
            maze1[next[0]][next[1]] = 2
            stack.pop()
    print("No way!")
    return False


def print_r(path):
    cur = path[-1]
    real_path = list()
    while cur[2] != -1:
        real_path.append(cur[0:2])
        cur = path[cur[2]]
    real_path.append(cur[0:2])
    real_path.reverse()
    for i in real_path:
        print(i)


def maze_path_queue(x1, y1, x2, y2):
    q = deque()
    q.append((x1, y1, -1))
    path = []
    while len(q) > 0:
        cur = q.popleft()
        path.append(cur)
        if cur[0] == x2 and cur[1] == y2:
            print_r(path)
            return True
        for i in dir:
            next = i(cur[0], cur[1])
            if maze2[next[0]][next[1]] == 0:
                q.append((next[0], next[1], len(path)-1))
                maze2[next[0]][next[1]] = 2

    print("No way!")
    return False


maze_path_stack(1, 1, 1, 4)

maze_path_queue(1, 1, 1, 4)