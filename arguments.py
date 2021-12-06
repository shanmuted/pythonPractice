def my_min(*nums):
    result = nums[0]
    for num in nums:
        if num < result:
            result = num
    return result

my_min([4, 5, 6, 7, 2])
