## NONE WORKING FUNCTION
#def same_values(lst1, lst2):
    # index = 0
    # num_same_at_positiion = []
    # while (index < len(lst1) and index < len(lst2)):
    #     if lst1[index] == lst2[index]:
    #         num_same_at_positiion.append(lst1[index])
    # return num_same_at_positiion

# Working functions
def same_values(lst1, lst2):
    lst3 = []
    for position in range(len(lst1)):
        if lst1[position] == lst2[position]:
            lst3.append(position)
    return lst3


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))