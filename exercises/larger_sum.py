def larger_sum(lst1, lst2):
    sum_1 = 0
    sum_2 = 0
    for index_x in lst1:
        sum_1 += index_x
    for index_y in lst2:
        sum_2 += index_y

    if sum_1 >= sum_2:
        return lst1
    else:
        return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))
