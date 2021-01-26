def max_num(nums):
    max_num = nums[0]
    for num in nums:
        if max_num < num:
            max_num = num
    return max_num

print(max_num([50, -10, 0, 75, 20]))    