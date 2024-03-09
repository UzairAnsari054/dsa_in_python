def merge_sort(list):
    if len(list) > 1:
        mid  = len(list) // 2
        left_list = list[:mid]
        right_list = list[mid:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i+=1
            else:
                list[k] = right_list[j]
                j+=1
            k+=1

        while i < len(left_list):
            list[k] = left_list[i]
            i+=1
            k+=1
        while j < len(right_list):
            list[k] = right_list[j]
            j+=1
            k+=1

myList = [75,29,83,42,16,90,56,34,20,71,88,92,7]
merge_sort(myList)
print(myList)