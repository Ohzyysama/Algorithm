def bubble_sort(li):
    l = len(li)
    for i in range(l-1):
        for j in range(0, l-i-1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


li = [4, 2, 3, 1, 7, 5, 8, 9, 6, 0]
bubble_sort(li)
print(li)