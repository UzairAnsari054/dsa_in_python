def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]

        j = i-1
        while j>=0 and list[j]>temp:
            list[j+1] = list[j]
            j-=1
        list[j+1] = temp

myList = [13,5,34,53,559,32]
insertion_sort(myList)
print(myList)

