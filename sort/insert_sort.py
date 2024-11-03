def insert_sort(nums):
    length = len(nums)
    for i in range(1, length):
        j = i - 1
        temp = nums[i]
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = temp


nums = [3, 5, 1, 2, 8, 6, 9, 7, 4]
insert_sort(nums)
print(nums)