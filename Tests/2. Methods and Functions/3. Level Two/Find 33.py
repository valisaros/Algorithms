# Given a list of ints, return True if array contains a 3 next to a 3

def has_33(nums):
    for i in range(0, len(nums) - 1):
        if nums[i] == 3 and nums[i-1] == 3:          # nums[i:i+2] == [3,3]
            return True

    return False
