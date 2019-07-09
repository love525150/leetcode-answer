'''
给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

你找到的子数组应是最短的，请输出它的长度。
'''
'''
解题思路：排序再跟原数组对比
'''
class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        sorted_list = sorted(nums)
        i = 0
        j = len(nums) - 1
        head_exit = False
        tail_exit = False
        while i < j and (not head_exit or not tail_exit):
            if not head_exit and nums[i] == sorted_list[i]:
                i += 1
            else:
                head_exit = True
            if not tail_exit and nums[j] == sorted_list[j]:
                j -= 1
            else:
                tail_exit = True
        
        return j - i + 1 if j > i else 0