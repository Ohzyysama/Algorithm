def radix_sort(li):
    max_num = max(li)
    count = 0
    while 10 ** count <= max_num:
        buckets = [[] for _ in range(10)]
        for val in li:
            i = (val // (10 ** count)) % 10
            buckets[i].append(val)
        li.clear()
        for bucket in buckets:
            li.extend(bucket)
        count += 1


li = list(range(100))
import random
random.shuffle(li)
print(li)
radix_sort(li)
print(li)