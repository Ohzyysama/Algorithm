def bucket_sort(li, n=100, max_n=1000):
    buckets = [[] for _ in  range(n)]
    for val in li:
        i = val // (max_n // n)
        buckets[i].append(val)
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break

    li.clear()
    for j in buckets:
        li.extend(j)

import random
li = list(range(1000))
random.shuffle(li)
print(li)
bucket_sort(li)
print(li)