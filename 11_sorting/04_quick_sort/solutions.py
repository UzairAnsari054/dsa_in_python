def quick_sort(list1):
    if len(list1) <= 1:
        return list1
    else:
        pivot = list1[0]
        lesser = [x for x in list1[1:] if x<=pivot]
        greater = [x for x in list1[1:] if x>pivot]
        return quick_sort(lesser)+[pivot]+quick_sort(greater)
    
l1 = [23,45,12,2,112,334,53,84]
my_list = quick_sort(l1)
print(my_list)


        
