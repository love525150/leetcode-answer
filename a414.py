'''
给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
'''

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        none = -2147483649
        first = none
        second = none
        third = none
        for i in range(len(nums)):
            current = nums[i]
            if current > first:
                third = second
                second = first
                first = current
            elif current < first and current > second:
                third = second
                second = current
            elif current < second and current > third:
                third = current
        result = min(first, second, third)
        if third == none or second == none:
            result = first
        return result