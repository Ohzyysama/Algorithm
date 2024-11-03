import random
def insert_sort_changed(li, gap):
    l = len(li)
    for i in range(gap, l):
        temp = li[i]
        j = i - gap
        while j >= 0 and li[j] > temp:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = temp


def shell_sort(li):
    gap = len(li) // 2
    while gap > 0:
        insert_sort_changed(li, gap)
        gap = gap // 2


li = list(range(100))
random.shuffle(li)
print(li)
shell_sort(li)
print(li)