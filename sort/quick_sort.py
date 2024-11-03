def partition(li, l, r):
    temp = li[l]
    while l < r:
        while l < r and li[r] > temp:
            r -= 1

        li[l] = li[r]

        while l < r and li[l] < temp:
            l += 1

        li[r] = li[l]

    li[l] = temp
    return l
def quick_sort(li, l, r):
    if l < r:
        mid = partition(li, l, r)
        quick_sort(li, l, mid-1)
        quick_sort(li, mid+1, r)



li = [4, 3, 1, 6, 5, 8, 7, 9, 2]
quick_sort(li, 0, 8)
print(li)