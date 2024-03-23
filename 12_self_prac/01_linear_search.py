nums = [1,2,3,4,5,6]

def linear_search_1(nums):
    targetNum = 3
    index = 0

    for num in nums:
        if num == targetNum:
            return num
        index+=1
    return -1

def linear_search_2(nums):
    targetNum = 3
    index = 0

    for num in range(len(nums)):
        if num == targetNum:
            return num
        index+=1
    return -1

a = linear_search_1(nums)
b = linear_search_2(nums)
# print(a)
# print(b)


    
alphabets = ["a","b","c","d"]
def linear_search_3(alphabets):
    for alphabet in range(len(alphabets)):
        print(alphabet)
    
def linear_search_4(alphabets):
    for alphabet in alphabets:
        print(alphabet)
        
linear_search_3(alphabets)
linear_search_4(alphabets)

# Findings:
# for alphabet in range(len(alphabets)):
#     This will return the indexes starting from 0 to lengtg of alphabets

# for alphabet in alphabets:
#     This will return the alphabets from start to end