def bubble_sorrting(data_list):
    for r in range(1, len(data_list)):
        for i in range(len(data_list)-r):
            if data_list[i] > data_list[i+1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]

def modified_bubble_sorrting(data_list):
    flag = False
    for r in range(1, len(data_list)):
        flag = False
        for i in range(len(data_list)-r):
            if data_list[i] > data_list[i+1]:
                data_list[i], data_list[i+1] = data_list[i+1], data_list[i]
                flag = True
        if not flag:
            break




l = [34,65,1,35,330,455]
ml = [34,65,1,35,330,455]
bubble_sorrting(l)
modified_bubble_sorrting(ml)
print(l)
print(ml)