# assume that all numbers are from 0 - 100
import random


def count_sort(li):
    count = [0 for _ in range(max(li) + 1)]
    for i in li:
        count[i] += 1

    li.clear()

    for i, val in enumerate(count):
        for j in range(val):
            li.append(i)


li = list(range(100))
random.shuffle(li)
print(li)
count_sort(li)
print(li)
