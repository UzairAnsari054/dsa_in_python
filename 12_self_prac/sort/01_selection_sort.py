def selection_sort(nums):
    for i in range(len(nums)):
        minIndex = i
        for j in range(i+1, len(nums)):
            if (nums[minIndex] > nums[j]):
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]



nums = [3,6,5,1,2,4]
selection_sort(nums)
print(nums)





