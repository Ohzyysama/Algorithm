# an application of heap_sort
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    temp = li[low]
    while j <= high:
        if j + 1 <= high and li[j] > li[j + 1]:
            j = j + 1
        if li[j] < temp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = temp
            break
    li[i] = temp


def topk(li, k):
    heap = li[0:k]
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)

    for i in range(k, len(li)):
        if li[i] > heap[0]:
            li[i], heap[0] = heap[0], li[i]
            sift(heap, 0, k-1)

    for i in range(k-1, -1, -1):
        heap[0], heap[i]= heap[i], heap[0]
        sift(heap, 0, i-1)

    return heap


li = [4, 1, 3, 7, 9, 8, 6, 5, 2]
print(topk(li, 3))
