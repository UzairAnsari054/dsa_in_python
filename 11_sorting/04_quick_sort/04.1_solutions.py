def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[0]
        lesser = [x for x in list[1:] if x <= pivot]
        greater = [x for x in list[1:] if x > pivot]
        return quick_sort(lesser) + [pivot] + quick_sort(greater)
    
l1 = [23,45,12,2,112,334,53,84]
my_list = quick_sort(l1)
print(my_list)

