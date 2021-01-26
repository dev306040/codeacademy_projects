def over_nine_thousand(lst):
    sum = 0
    for num in lst:
        sum += num
        if sum > 9000:
            break
    return sum
    # elif sum < 9000:
    #    return sum
    #else:
    #    return lst

print(over_nine_thousand([8000, 900, 120, 5000]))
#print(over_nine_thousand([1000, 400, 120, 2000]))
#print(over_nine_thousand([]))
