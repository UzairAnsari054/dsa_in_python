def bubble_sort(list):
    for r in range(1, len(list)):
        for i in range(len(list)-r):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]

def modified_bubble_sort(list):
    for r in range(1, len(list)):
        flag = False
        for i in range(len(list) - r):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                flag = True
        if not flag:
                break

l1 = [9,7,5,3,2,6,8,1]
# bubble_sort(l1)
# print(l1)

modified_bubble_sort(l1)
print(l1)


            

