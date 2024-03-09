def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
        
l1 = [64,35,21,4,13,134]
selection_sort(l1)
print(l1)
