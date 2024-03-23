def binary(nums, target):
    minIndex = 0
    maxIndex = len(nums) - 1

    while(minIndex <= maxIndex):
        middleIndex = (minIndex+maxIndex) // 2
        if target == nums[middleIndex]:
            return middleIndex
        elif target < middleIndex:
            maxIndex = middleIndex - 1 
        else:
            minIndex = middleIndex + 1
        return -1 

nums = [1,2,3,4,5,6]
res = binary(nums, 7)
print(res)


