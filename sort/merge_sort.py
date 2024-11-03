def merge(li, low, mid, high):
    nli = []
    i = low
    j = mid + 1
    while i <= mid and j <= high:
        if li[i] < li[j]:
            nli.append(li[i])
            i += 1
        else:
            nli.append(li[j])
            j += 1
    while i <= mid:
        nli.append(li[i])
        i += 1
    while j <= high:
        nli.append(li[j])
        j += 1
    li[low:high+1] = nli


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1 , high)
        merge(li, low, mid, high)


li = [4, 1, 3, 7, 2, 9, 8, 6, 5]
merge_sort(li, 0, 8)
print(li)