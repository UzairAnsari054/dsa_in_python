# Bubble sort pushes the greater value to the end
# 1st loop represents how many rounds will happen i.e, len(list) - 1 or range(1, len(list))
# 2nd loop represents how many comparisons will happen in each round i.e, len(list) - currentRound. Because each round will give us the greatest value for that round at the end of list & so after each round there will be 1 less comparison needed

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