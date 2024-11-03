def sift(li, low, high):
    i = low
    j = 2 * i + 1
    temp = li[low]
    while j <= high:
        if j + 1 <= high and li[j] < li[j + 1]:
            j = j + 1
        if li[j] > temp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = temp
            break
    li[i] = temp


def heap_sort(li):
    l = len(li)
    for i in range((l - 2) // 2, -1, -1):
        sift(li, i, l - 1)

    for i in range(l - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)


li = [4, 1, 2, 7, 9, 8, 5, 3, 6]
heap_sort(li)
print(li)
