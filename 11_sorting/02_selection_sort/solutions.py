def selection_sorting(data_list):
    n = len(data_list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data_list[j] < data_list[min_index]:
                min_index = j
        data_list[i], data_list[min_index] = data_list[min_index], data_list[i]
    
l1 = [64,35,21,4,13,134]
selection_sorting(l1)
print(l1)
