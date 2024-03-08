def insertion_sorting(list1):
    for i in range(1, len(list1)):
        temp = list1[i]

        j = i-1
        while j >= 0 and temp < list1[j]:
            list1[j+1] = list1[j]  
            j-=1 
        list1[j+1] = temp

myList = [13,5,34,53,559,32]
insertion_sorting(myList)
print(myList)

