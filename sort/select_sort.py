def select_sort(nums):
    for i in range(0, len(nums)):
        m = nums[i]
        index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < m:
                m = nums[j]
                index = j

        nums[i], nums[index] = nums[index], nums[i]


nums = [2, 6, 1, 7, 4, 5, 9, 8, 3]
select_sort(nums)
print(nums)