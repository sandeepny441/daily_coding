Find pair with given sum in the array

def get_pair_count(nums, target_sum):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    total_double = 0
    for num in nums:
        complement = target_sum - num
        if complement in count:
            total_double += count[complement]
            if complement == num:
                total_double -= 1
    return total_double // 2

------------------------------------------------------------------------------------------------
